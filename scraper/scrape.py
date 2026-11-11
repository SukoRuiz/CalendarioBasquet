#!/usr/bin/env python3
"""Descarga los calendarios de los equipos del CNB Vilanova desde cnbvilanova.com
y genera los JSON que lee la web estática (docs/).

Solo usa la librería estándar. Uso:  python scraper/scrape.py
"""
import datetime as dt
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "data"            # generado en cada ejecución (no se versiona)
CACHE = ROOT / "cache"                  # se versiona: pabellones geocodificados y equipos conocidos
BASE = "https://cnbvilanova.com"
REPO = os.environ.get("GITHUB_REPOSITORY", "local")
UA = f"Mozilla/5.0 (compatible; CalendarioBasquet/1.0; +https://github.com/{REPO})"
PAUSA = 1.0                             # segundos entre peticiones al club


# ---------------------------------------------------------------- utilidades

def fetch(url: str) -> str:
    """Devuelve el HTML como str 'latin-1' (1 byte = 1 carácter) para poder
    re-decodificar cada fragmento: la web mezcla UTF-8 y Latin-1."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for intento in range(3):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read().decode("latin-1")
        except Exception as e:  # noqa: BLE001
            if intento == 2:
                raise
            print(f"  reintento {url}: {e}", file=sys.stderr)
            time.sleep(5)


def txt(fragmento: str) -> str:
    """Texto limpio de un fragmento HTML, arreglando la codificación mixta."""
    s = re.sub(r"<[^>]+>", " ", fragmento)
    b = s.encode("latin-1")
    try:
        s = b.decode("utf-8")
    except UnicodeDecodeError:
        s = b.decode("cp1252", errors="replace")
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, ValueError):
        return default


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- equipos

TEAM_LINK = re.compile(r'team\?id=(\d+)"\s*>\s*([^<]+?)\s*<')


def descubrir_equipos(conocidos: dict) -> dict:
    """Equipos del club que aparecen en el calendario mensual (mes actual y siguiente)."""
    hoy = dt.date.today()
    meses = {hoy.month, (hoy.month % 12) + 1}
    for m in sorted(meses):
        page = fetch(f"{BASE}/calendari-club/?month={m:02d}")
        for tid, nombre in TEAM_LINK.findall(page):
            conocidos.setdefault(tid, {})["nombre"] = txt(nombre)
        time.sleep(PAUSA)
    return conocidos


# ---------------------------------------------------------------- calendario

def parse_lado(bloque: str) -> dict:
    m = re.search(r'team\?id=(\d+)"\s*>(.*?)</a>', bloque, re.S)
    if m:
        return {"id": m.group(1), "nombre": txt(m.group(2))}
    m = re.search(r'match-card-team-name">(.*?)</div>', bloque, re.S)
    return {"id": None, "nombre": txt(m.group(1)) if m else "?"}


def parse_partido(card: str, team_id: str) -> dict | None:
    lados = re.split(r'<div class="match-card-team">', card)[1:3]
    if len(lados) < 2:
        return None
    local, visitante = parse_lado(lados[0]), parse_lado(lados[1])

    fecha = re.search(r'<div style="([^"]*)"\s*class="common-text match-card-date">(.*?)</div>', card, re.S)
    fecha_txt = txt(fecha.group(2)) if fecha else ""
    m = re.match(r"(\d\d)/(\d\d)/(\d{4})(?:\s+(\d\d:\d\d))?", fecha_txt)
    if not m:
        return None
    dia = f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    hora = m.group(4) or ""

    estado = re.search(r'match-card-state common-text">(.*?)</div>', card, re.S)
    estado_txt = txt(estado.group(1)) if estado else ""
    rojo = bool(fecha and "red" in fecha.group(1))

    res = [txt(r) for r in re.findall(r'match-card-result">(.*?)</div>', card, re.S)]
    marcador = [int(r) for r in res] if len(res) == 2 and all(r.isdigit() for r in res) else None

    venue = lat = lon = None
    mm = re.search(r'maps\?q=loc:\s*(-?[\d.]+)\s*,\s*(-?[\d.]+)[^"]*"', card)
    if mm:
        lat, lon = float(mm.group(1)), float(mm.group(2))
    links = card.split("match-card-links", 1)[-1]
    mv = re.search(r'common-link-text">(.*?)</div>', links, re.S)
    if mv and "group=" not in links[: links.find(mv.group(0))]:
        venue = txt(mv.group(1))

    mid = re.search(r"match\?id=(\d+)", card)
    stats = re.search(r'href="(https://www\.basquetcatala\.cat/estadistica/[^"]+)"', card)

    es_local = local["id"] == team_id
    rival = visitante if es_local else local
    return {
        "id": mid.group(1) if mid else None,
        "fecha": dia,
        "hora": hora,
        "local": local["nombre"],
        "visitante": visitante["nombre"],
        "enCasa": es_local,
        "rival": rival["nombre"],
        "marcador": marcador,
        "cambio": rojo or bool(estado_txt),
        "estado": estado_txt,
        "pabellon": venue,
        "lat": lat,
        "lon": lon,
        "estadisticas": stats.group(1) if stats else None,
    }


def parse_calendario(page: str, team_id: str) -> dict:
    cuerpo = page.split('class="team-calendar-content"', 1)[-1]
    cards = cuerpo.split('<div class="match-card-content">')[1:]
    partidos = [p for p in (parse_partido(c, team_id) for c in cards) if p]
    grupo = re.search(r'resultsandstanding\?group=(\d+)">.*?common-link-text">(.*?)</div>', cuerpo, re.S)
    nombre = re.search(rf'team\?id={team_id}"\s*>(.*?)</a>', cuerpo, re.S)
    return {
        "nombre": txt(nombre.group(1)) if nombre else None,
        "categoria": txt(grupo.group(2)) if grupo else "",
        "grupo": grupo.group(1) if grupo else None,
        "partidos": partidos,
    }


# ---------------------------------------------------------------- ciudades

def ciudad(lat: float, lon: float, cache: dict) -> str | None:
    """Población a partir de coordenadas (OpenStreetMap Nominatim, 1 petición/s, con caché)."""
    key = f"{lat:.5f},{lon:.5f}"
    if key in cache:
        return cache[key]
    url = ("https://nominatim.openstreetmap.org/reverse?format=jsonv2&zoom=10&accept-language=ca"
           f"&lat={lat}&lon={lon}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
        a = d.get("address", {})
        nombre = a.get("city") or a.get("town") or a.get("village") or a.get("municipality") or d.get("name")
    except Exception as e:  # noqa: BLE001  (se reintentará en la próxima ejecución)
        print(f"  geocodificación fallida {key}: {e}", file=sys.stderr)
        nombre = None
    time.sleep(1.1)
    if nombre:
        cache[key] = nombre
    return nombre


# ---------------------------------------------------------------- main

def main() -> int:
    conocidos = load_json(CACHE / "equipos.json", {})
    pabellones = load_json(CACHE / "pabellones.json", {})

    conocidos = descubrir_equipos(conocidos)
    print(f"{len(conocidos)} equipos")

    resumen, fallos = [], 0
    for tid in sorted(conocidos, key=lambda t: conocidos[t].get("nombre", "")):
        try:
            cal = parse_calendario(fetch(f"{BASE}/team-calendar/?id={tid}"), tid)
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR {tid}: {e}", file=sys.stderr)
            fallos += 1
            continue
        finally:
            time.sleep(PAUSA)
        if not cal["partidos"]:
            print(f"  {tid}: sin partidos, se omite")
            continue

        info = conocidos[tid]
        info["nombre"] = cal["nombre"] or info.get("nombre")
        info["categoria"] = cal["categoria"]

        for p in cal["partidos"]:
            p["ciudad"] = ciudad(p["lat"], p["lon"], pabellones) if p["lat"] is not None else None
        # Ciudad del rival = ciudad del pabellón donde juega como local contra nosotros
        casa_rival = {p["rival"]: p["ciudad"] for p in cal["partidos"] if not p["enCasa"] and p["ciudad"]}
        for p in cal["partidos"]:
            p["ciudadRival"] = casa_rival.get(p["rival"]) or (None if p["enCasa"] else p["ciudad"])
        # Pabellón habitual del equipo (para saber si un partido "en casa" es en otro sitio)
        habitual = Counter(p["pabellon"] for p in cal["partidos"] if p["enCasa"] and p["pabellon"])

        save_json(OUT / "equipos" / f"{tid}.json", {
            "id": tid,
            "nombre": info["nombre"],
            "categoria": cal["categoria"],
            "grupo": cal["grupo"],
            "pabellonHabitual": habitual.most_common(1)[0][0] if habitual else None,
            "partidos": cal["partidos"],
        })
        resumen.append({"id": tid, "nombre": info["nombre"], "categoria": cal["categoria"],
                        "partidos": len(cal["partidos"])})
        print(f"  {tid} {info['nombre']}: {len(cal['partidos'])} partidos")

    if fallos > len(conocidos) // 2 or not resumen:
        print(f"Demasiados fallos ({fallos}); no se publica nada.", file=sys.stderr)
        return 1

    save_json(OUT / "equipos.json", resumen)
    save_json(OUT / "estado.json", {"actualizado": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                    "fallos": fallos})
    save_json(CACHE / "equipos.json", dict(sorted(conocidos.items())))
    save_json(CACHE / "pabellones.json", dict(sorted(pabellones.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
