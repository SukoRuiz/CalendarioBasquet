# Calendario CNB Vilanova

Web estática con los partidos de los equipos del CNB Vilanova: próximos, jugados (con resultado) y todos.
Marca en rojo con **!** los partidos cambiados, distingue local/fuera, muestra pabellón + población
y enlaza a Google Maps ("Cómo llegar" en los partidos fuera de casa).

## Cómo funciona

```
cnbvilanova.com ──(cada 2 h)──> GitHub Action: scraper/scrape.py ──> docs/data/*.json ──> GitHub Pages
```

- **`scraper/scrape.py`** (Python, sin dependencias) lee `calendari-club` para descubrir los equipos
  y `team-calendar/?id=…` para cada calendario. La población de cada pabellón se obtiene una sola vez de
  OpenStreetMap a partir de sus coordenadas y se guarda en `cache/pabellones.json`.
- **`docs/index.html`** es la web: lee los JSON y no depende de ningún servidor.
- **`.github/workflows/actualizar.yml`** ejecuta el scraper cada 2 h (y con cada push) y publica en Pages.
  Si la web del club falla, la Action falla y sigue publicada la versión anterior.

## Favoritos

- **Comunes (todos los navegadores):** `docs/favoritos.json`. Se editan en GitHub (la web tiene un enlace
  "Editar favoritos comunes"); al guardar, la web se republica en un par de minutos.
- **Personales:** la ☆ junto al desplegable añade o quita equipos solo en ese navegador.

El id de cada equipo aparece en la URL de la web, p. ej. `…/#89776` (SM2).

## Puesta en marcha (una vez)

1. Crear un repositorio en GitHub y subir esta carpeta a la rama `main`.
2. *Settings → Pages → Build and deployment → Source:* **GitHub Actions**.
3. *Actions →* "Actualizar calendarios" → **Run workflow** (la primera vez, para no esperar 2 h).
4. La web queda en `https://<usuario>.github.io/<repositorio>/`.

Nota: GitHub pausa las tareas programadas de un repositorio tras 60 días sin actividad; si pasa,
basta con volver a activarlas desde la pestaña *Actions*.

## Probar en local

```bash
python scraper/scrape.py
python -m http.server 5173 --directory docs   # y abrir http://127.0.0.1:5173
```
