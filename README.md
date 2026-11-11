# Calendario CNB Vilanova

Web con los partidos de los equipos del CNB Vilanova: próximos, jugados (con resultado) y todos.
Marca en rojo con **!** los partidos cambiados, distingue local/fuera, muestra pabellón + población
y enlaza a Google Maps ("Cómo llegar" en los partidos fuera de casa).

## 🔗 Acceso rápido

| | Enlace |
|---|---|
| 🏀 **Web** | **https://sukoruiz.github.io/CalendarioBasquet/** |
| 🧪 Enlace de prueba (SM2) | https://sukoruiz.github.io/CalendarioBasquet/#89776 |
| ⭐ Editar favoritos comunes | [docs/favoritos.json](https://github.com/SukoRuiz/CalendarioBasquet/edit/main/docs/favoritos.json) |
| 🔄 Actualizar ahora | [Actualizar calendarios → Run workflow](https://github.com/SukoRuiz/CalendarioBasquet/actions/workflows/actualizar.yml) |
| 📋 Historial de actualizaciones | [Actions](https://github.com/SukoRuiz/CalendarioBasquet/actions) |

## Uso de la web

- **Elegir equipo:** desplegable de arriba. Los favoritos aparecen primero, marcados con ★.
- **Pestañas:** *Próximos* (el siguiente partido destacado), *Jugados* (con marcador y Victoria/Derrota) y *Todos*.
- **Cambios:** fecha y hora en rojo con **!** y la etiqueta CAMBIADO.
- **Fuera de casa:** pabellón, población y botón **Cómo llegar** (Google Maps).
- **Enlace directo a un equipo:** añade `#<id>` a la dirección, p. ej. `…/CalendarioBasquet/#89773` (SM1).
  La web recuerda en cada navegador el último equipo consultado.

## Favoritos

Hay dos tipos:

- **Comunes** (los ven todos los navegadores): están en
  [`docs/favoritos.json`](https://github.com/SukoRuiz/CalendarioBasquet/edit/main/docs/favoritos.json).
  1. Abre el enlace con la cuenta **SukoRuiz** (también está al pie de la web: "Editar favoritos comunes").
  2. Añade o quita ids en la lista, entre comillas y separados por comas:
     ```json
     "equipos": ["89776", "89773"]
     ```
  3. Pulsa **Commit changes**. La web se republica sola en 1–2 minutos.
- **Personales** (solo en ese navegador): botón ☆ junto al desplegable. Los favoritos comunes muestran ★ fija.

### Ids de los equipos (temporada 2026-27)

| Id | Equipo | Categoría |
|---|---|---|
| [89773](https://sukoruiz.github.io/CalendarioBasquet/#89773) | CNB VILANOVA VIMA GESTIÓ SM1 | 1A. TERRITORIAL SÈNIOR MASCULÍ |
| [89776](https://sukoruiz.github.io/CalendarioBasquet/#89776) | CNB VILANOVA AKO SM2 | 3A. TERRITORIAL SÈNIOR MASCULÍ |
| [88863](https://sukoruiz.github.io/CalendarioBasquet/#88863) | CNB VILANOVA AKO S25M | C.T. SOTS-25 MASCULÍ NIVELL B |
| [88871](https://sukoruiz.github.io/CalendarioBasquet/#88871) | CNB VILANOVA AKO SF1 | 1A. TERRITORIAL SÈNIOR FEMENÍ |
| [88876](https://sukoruiz.github.io/CalendarioBasquet/#88876) | CNB VILANOVA AKO SF2 | 2A. TERRITORIAL SÈNIOR FEMENÍ |
| [89775](https://sukoruiz.github.io/CalendarioBasquet/#89775) | CNB VILANOVA AKO JM1 | C.C. JÚNIOR MASCULÍ INTERTERRITORIAL |
| [88862](https://sukoruiz.github.io/CalendarioBasquet/#88862) | CNB VILANOVA AKO-VIMA GESTIÓ JM2 | C.C. JÚNIOR MASCULÍ PREFERENT 1R. ANY |
| [89774](https://sukoruiz.github.io/CalendarioBasquet/#89774) | CNB VILANOVA AKO JM3 | C.T. BCN U17 - JÚNIOR MASCULÍ 1R. ANY PROMOCIÓ |
| [88865](https://sukoruiz.github.io/CalendarioBasquet/#88865) | CNB VILANOVA AKO JF | C.T. BCN U17 - JÚNIOR FEMENÍ 1R ANY PROMOCIÓ |
| [88866](https://sukoruiz.github.io/CalendarioBasquet/#88866) | CNB VILANOVA AKO CM1 | C.C. CADET MASCULÍ INTERTERRITORIAL |
| [88873](https://sukoruiz.github.io/CalendarioBasquet/#88873) | CNB VILANOVA AKO CM2 | C.T. CADET MASCULÍ PROMOCIÓ · NIVELL A |
| [91944](https://sukoruiz.github.io/CalendarioBasquet/#91944) | CNB VILANOVA AKO CM3 | C.T. CADET MASCULÍ PROMOCIÓ · NIVELL C |
| [91945](https://sukoruiz.github.io/CalendarioBasquet/#91945) | CNB VILANOVA AKO CM4 | C.T. CADET MASCULÍ PROMOCIÓ · NIVELL B |
| [92365](https://sukoruiz.github.io/CalendarioBasquet/#92365) | CNB VILANOVA AKO CM5 | C.T. CADET MASCULÍ PROMOCIÓ · NIVELL C |
| [89777](https://sukoruiz.github.io/CalendarioBasquet/#89777) | CNB VILANOVA AKO CF1 | C.T. CADET FEMENÍ PROMOCIÓ · NIVELL B |
| [88875](https://sukoruiz.github.io/CalendarioBasquet/#88875) | CNB VILANOVA AKO CF2 | C.T. CADET FEMENÍ PROMOCIÓ · NIVELL C |
| [88870](https://sukoruiz.github.io/CalendarioBasquet/#88870) | CNB VILANOVA AKO INF 1ER ANY | C.C. INFANTIL MASCULÍ PREFERENT 1R. ANY |
| [88869](https://sukoruiz.github.io/CalendarioBasquet/#88869) | CNB VILANOVA AKO IM1 | C.T. INFANTIL MASCULÍ PROMOCIÓ · NIVELL A |
| [88874](https://sukoruiz.github.io/CalendarioBasquet/#88874) | CNB VILANOVA AKO IM2 | C.T. INFANTIL MASCULÍ PROMOCIÓ · NIVELL C |
| [88872](https://sukoruiz.github.io/CalendarioBasquet/#88872) | CNB VILANOVA AKO IF | C.T. INFANTIL FEMENÍ PROMOCIÓ · NIVELL C |
| [88868](https://sukoruiz.github.io/CalendarioBasquet/#88868) | CNB VILANOVA AKO PIM2 | C.T. PRE-INFANTIL MASCULÍ · NIVELL C |
| [88867](https://sukoruiz.github.io/CalendarioBasquet/#88867) | CNB VILANOVA AKO PIM3 | C.T. PRE-INFANTIL MASCULÍ · NIVELL B |
| [88864](https://sukoruiz.github.io/CalendarioBasquet/#88864) | CNB VILANOVA AKO PIF | C.T. PRE-INFANTIL FEMENÍ · NIVELL C |

La lista se completa sola con los equipos que aparecen en la web del club; si un equipo nuevo no está
aquí, su id es el número que sale en la dirección de la web al seleccionarlo.

## Actualización de los datos

- **Automática:** una vez al día, a las 05:07 UTC (6:07 en invierno, 7:07 en verano). GitHub puede retrasarla un rato.
- **Al momento:** [Actualizar calendarios](https://github.com/SukoRuiz/CalendarioBasquet/actions/workflows/actualizar.yml)
  → botón **Run workflow** → **Run workflow** (verde). Tarda 1–2 minutos.
- **También** se actualiza cada vez que se guarda un cambio en el repositorio (p. ej. al editar los favoritos).
- La web indica arriba a la derecha cuándo fue la última actualización.
- Si la web del club falla, la actualización se marca en rojo en [Actions](https://github.com/SukoRuiz/CalendarioBasquet/actions)
  y sigue publicada la versión anterior.

> GitHub pausa las tareas programadas tras 60 días sin actividad en el repositorio. Si pasa, aparece un aviso
> en [Actions](https://github.com/SukoRuiz/CalendarioBasquet/actions/workflows/actualizar.yml) con un botón para reactivarla.

## Cómo funciona

```
cnbvilanova.com ──(1 vez al día)──> GitHub Action: scraper/scrape.py ──> docs/data/*.json ──> GitHub Pages
```

- **`scraper/scrape.py`** (Python, sin dependencias) lee `calendari-club` para descubrir los equipos
  y `team-calendar/?id=…` para cada calendario. La población de cada pabellón se obtiene una sola vez de
  OpenStreetMap a partir de sus coordenadas y se guarda en `cache/pabellones.json`.
- **`docs/index.html`** es la web: lee los JSON y no depende de ningún servidor.
- **`docs/favoritos.json`** son los favoritos comunes.
- **`.github/workflows/actualizar.yml`** ejecuta el scraper y publica en GitHub Pages.

## Probar en local

```bash
python scraper/scrape.py
python -m http.server 5173 --directory docs   # y abrir http://127.0.0.1:5173
```
