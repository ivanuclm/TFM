# Urban Mobility Simulator for Toledo

> **Documentación en español:** [README.es.md](./README.es.md)

Web-based simulator for urban mobility scenarios in Toledo, Spain. Computes
multimodal routes, visualises the public transport network and predicts travel
mode choice using machine learning — all within a single Docker Compose stack.

Developed as a Master's thesis project at the University of Castilla-La Mancha
(ESIIAB, UCLM).

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-UI-3178C6?logo=typescript&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-Map-199900?logo=leaflet&logoColor=white)

![Simulator main view](docs/app-preview.png)

---

## Features

The interface is built around a fixed sidebar rail that gives access to six
functional panels overlaid on a full-screen map of Toledo.

**Routes panel**
- Set origin and destination by right-clicking on the map or editing the
  coordinate fields directly in the panel.
- Compute car, cycling and walking routes simultaneously via three local OSRM
  instances (colour-coded polylines with contrast casing for light-coloured lines).
- Plan public transport journeys with OpenTripPlanner 2.x (Toledo urban GTFS,
  Feb–May 2026); navigate between alternative itineraries and inspect a
  stop-by-stop diagram with departure times, map fly-to and transfer markers.
- Auto-recalculation: once the first calculation is done, changing either
  endpoint reruns all routes automatically.

**GTFS Network panel**
- Browse bus lines in an accordion grouped by line name; each line shows its
  route colour, both directions and a stop diagram in line-poster style.
- Timetable with next-departure highlighting: past departures in grey, upcoming
  in blue, next one in bold. Shows a notice when the line does not run on the
  selected date.

**AI Prediction panel**
- Three built-in trip profiles — Commuter, Student, Family — that pre-fill the
  form and set the global date/time to a representative scenario.
- Run mode-choice inference (XGBoost, Random Forest or DNN) and see
  probabilities for walk, cycle, public transport and drive.
- Compare all three models on the same scenario, or inspect the full feature
  vector (raw and scaled) via the debug modal.

**Layers panel**
- Six basemap options: CartoDB Voyager (default), CartoDB Positron,
  OpenStreetMap, OpenTopoMap, Esri World Imagery (satellite) and PNOA aerial
  (IGN Spain, 25 cm resolution in urban areas, no token required).

**Settings panel**
- Toggle bus stop markers on/off.
- Dynamic model selector: any `{name}_lpmc.joblib` + `{name}_lpmc_scaler.joblib`
  placed in `lpmc/models/` is detected at runtime without restarting any
  container.
- Collapsible instructions for adding custom models (sklearn `predict_proba`
  interface or PyTorch via `TorchModalWrapper`).

**Global date/time control**
- A single date/time picker pinned to the top-left of the map governs all
  panels simultaneously: OTP itineraries, GTFS timetables and the AI trip
  profile. Constrained to the valid range of the GTFS feed (22 Feb – 22 May 2026).

**Map controls**
- Fractional zoom (steps of 0.25) via custom React buttons replacing the
  default Leaflet controls. Separate clear buttons for routes, bus layer or
  everything including O/D markers.
- Right-click context menu: set origin, set destination, or copy coordinates
  to clipboard.

---

## Prerequisites

| Requirement | Notes |
|---|---|
| [Git](https://git-scm.com/) | Required. |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Required. Provides Docker Engine and Compose v2. |
| [Git LFS](https://git-lfs.com/) | Required to download large binary files (models, routing graphs, GTFS). |

---

## Quick start

```bash
git lfs install                  # one-time setup — must run BEFORE cloning
git clone https://github.com/ivanuclm/movilidad-urbana.git
cd movilidad-urbana
docker compose up --build
```

Open **http://127.0.0.1:5173** once all services are ready.

> **First run takes ~15–20 minutes** while OSRM compiles the routing graphs
> for car, cycling and foot profiles from the included OSM extract. Subsequent
> runs start in seconds.

### What `docker compose up` does automatically

1. **`gtfs-init`** — extracts the GTFS zip (from LFS) into the backend data
   directory. Skipped on re-runs.
2. **`osrm-setup`** — runs `osrm-extract → osrm-partition → osrm-customize`
   for each routing profile using the shared OSM PBF (from LFS). Already-compiled
   profiles are skipped.
3. **`otp-build`** — builds the OTP routing graph (`graph.obj`) from the GTFS
   feed and the OSM extract. Skipped if `graph.obj` already exists.
4. All application services start once the init containers finish.

### If you cloned without Git LFS installed

The large binary files will be missing (only LFS pointer files on disk).
Fix it with:

```bash
git lfs install
git lfs pull
docker compose up --build
```

---

## Common operations

```bash
docker compose up                # start all services (fast after first run)
docker compose up --build        # rebuild images and start (after code changes)
docker compose build frontend && docker compose up  # rebuild only the frontend (after adding npm packages)
docker compose down              # stop and remove containers
docker compose logs -f backend   # stream backend logs
docker compose logs -f osrm-setup  # check graph compilation progress
docker compose logs -f otp       # OpenTripPlanner logs
docker compose ps                # list container status
```

---

## Services

| Service | URL |
|---|---|
| Simulator | http://127.0.0.1:5173 |
| Backend API | http://127.0.0.1:8000 |
| API docs (OpenAPI) | http://127.0.0.1:8000/docs |
| OpenTripPlanner | http://127.0.0.1:8080 |
| OSRM — car | http://127.0.0.1:5001 |
| OSRM — cycling | http://127.0.0.1:5002 |
| OSRM — foot | http://127.0.0.1:5003 |

---

## API endpoints

All routing and inference requests go through the FastAPI backend. Full
interactive documentation is available at http://127.0.0.1:8000/docs.

```
GET  /health
POST /api/osrm/routes
POST /api/otp/routes
GET  /api/gtfs/stops
GET  /api/gtfs/routes
GET  /api/gtfs/routes/{route_id}
GET  /api/gtfs/routes/{route_id}/schedule?date=YYYY-MM-DD
POST /api/lpmc/predict
POST /api/lpmc/compare
POST /api/lpmc/debug-features
GET  /api/lpmc/models
```

---

## Architecture

The frontend never talks directly to OSRM or OTP — all requests go through the
FastAPI backend, which acts as an orchestration layer with four routers:

```
Browser (React + Leaflet)
        │  HTTP
        ▼
FastAPI backend ─┬─► OSRM car      (port 5001)  ┐
                 ├─► OSRM cycling  (port 5002)  ├─ /api/osrm
                 ├─► OSRM foot     (port 5003)  ┘
                 ├─► OTP           (port 8080)  ── /api/otp · /api/gtfs
                 └─► LPMC models   (in-process) ── /api/lpmc
```

OSRM requires one process per routing profile, hence three separate containers.
LPMC models are loaded into memory inside the backend process; no additional
service is needed.

### Repository layout

```
.
├── movilidad-urbana-sim/
│   ├── backend/          FastAPI (Python 3.12)
│   └── frontend/         React + Vite + TypeScript + Leaflet
├── osrm-clm/
│   └── *.osm.pbf         Castilla-La Mancha OSM extract (Git LFS, ~97 MB)
├── otp-toledo/
│   ├── graph.obj         Pre-built OTP graph (Git LFS, ~117 MB)
│   └── GTFS_Urbano_Toledo_2026.zip   Toledo urban GTFS (Git LFS, ~14 MB)
├── lpmc/
│   ├── models/           Trained models (Git LFS)
│   └── *.py              Training and tuning scripts
├── latex/                Academic thesis (LaTeX source + compiled PDF)
├── docker/               Dockerfiles (backend, frontend)
├── scripts/              Setup helpers
└── docker-compose.yml
```

### Files stored in Git LFS

| File | Size | Purpose |
|---|---|---|
| `osrm-clm/*.osm.pbf` | ~97 MB | OSM road network (CLM region) |
| `otp-toledo/graph.obj` | ~117 MB | Pre-built OTP routing graph |
| `otp-toledo/GTFS_Urbano_Toledo_2026.zip` | ~14 MB | Toledo urban GTFS feed |
| `lpmc/models/xgb_lpmc.joblib` | ~16 MB | XGBoost mode choice model |
| `lpmc/models/rf_lpmc.joblib` | ~398 MB | Random Forest mode choice model |
| `lpmc/models/dnn_lpmc.pt` | ~0.2 MB | DNN mode choice model (PyTorch) |

The RF model is large but included for convenience: GitHub Free provides 10 GiB
of LFS storage and 10 GiB/month of transfer, which comfortably covers typical
evaluator use. If LFS bandwidth becomes a concern, models can be distributed as
release assets instead.

---

## Travel mode choice models

Three models are included via Git LFS and ready to use out of the box.

| Model | File | CV accuracy | CV GMPCA | Test accuracy | Test GMPCA |
|---|---|---|---|---|---|
| XGBoost | `xgb_lpmc.joblib` | 75.5 % | 52.5 % | **74.4 %** | **51.6 %** |
| Random Forest | `rf_lpmc.joblib` | 74.9 % | 51.5 % | 74.1 % | 50.6 % |
| DNN (PyTorch) | `dnn_lpmc.pt` | 75.2 % | 51.3 % | 74.3 % | 50.4 % |

Metrics are 5-fold cross-validation grouped by household on the training set,
and evaluation on the held-out test set (temporal split by survey wave).
XGBoost is the default (`LPMC_MODEL_VARIANT=xgb` in `docker-compose.yml`).
`/api/lpmc/compare` runs all three models on the same scenario.

### Retraining from scratch

The full pipeline runs six scripts. Python 3.10+ must be installed locally.
The LPMC dataset is freely available:

- Paper: https://doi.org/10.1680/jsmic.17.00018
- CSV: https://www.emerald.com/jsmic/article-supplement/408759/csv/dataset/

Place the downloaded file at `lpmc/data/raw/LPMC_dataset.csv`.

```bash
cd lpmc
pip install -r requirements.txt
python 01_explore.py           # exploratory analysis
python 02_preprocess.py        # feature engineering
python 03_train_xgb.py         # XGBoost → models/xgb_lpmc.joblib
python 04_train_rf.py          # Random Forest → models/rf_lpmc.joblib  (~15 min)
python 05_train_dnn.py         # DNN → models/dnn_lpmc.pt + scaler
python 06_compare_models.py    # comparison table
docker compose restart backend
```

All three models use `GroupKFold(n_splits=5)` with `household_id` as the
grouping key (never used as a feature). Durations from OSRM and OTP are
converted from seconds to hours before inference to match the LPMC dataset units.

---

## Troubleshooting

### OSRM graphs corrupted or incomplete

Delete the profile directories and let `docker compose up` rebuild them:

```bash
# Linux / macOS / Git Bash
rm -rf osrm-clm/car osrm-clm/bike osrm-clm/foot

# Windows PowerShell
Remove-Item -Recurse -Force osrm-clm\car, osrm-clm\bike, osrm-clm\foot
```

### GTFS extraction failed

```bash
# Linux / macOS / Git Bash
rm -rf movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo_2026

# Windows PowerShell
Remove-Item -Recurse -Force "movilidad-urbana-sim\backend\data\gtfs\GTFS_Urbano_Toledo_2026"
```

### OTP returns no transit itineraries

The GTFS feed covers **22 Feb – 22 May 2026** only. Dates outside that range
return walk-only results. Use the global date/time picker in the interface to
select a date within the valid window.

### OTP graph missing after clone without LFS

Run `git lfs pull` to download `graph.obj`. Alternatively, the `otp-build`
init service will rebuild it automatically on the next `docker compose up`
(requires the OSM extract and GTFS zip to be present).

---

## Rebuilding data (advanced)

### Rebuild OTP graph manually

```bash
docker run --rm \
  -v "$(pwd)/otp-toledo:/var/opentripplanner" \
  opentripplanner/opentripplanner:2.5.0 \
  --build --save
```

### Rebuild OSRM graphs manually

```bash
# Example for car profile (repeat with bicycle.lua and foot.lua)
docker run --rm -v "$(pwd)/osrm-clm/car:/data" osrm/osrm-backend:latest \
  osrm-extract -p /opt/car.lua /data/clm.osm.pbf
docker run --rm -v "$(pwd)/osrm-clm/car:/data" osrm/osrm-backend:latest \
  osrm-partition /data/clm.osrm
docker run --rm -v "$(pwd)/osrm-clm/car:/data" osrm/osrm-backend:latest \
  osrm-customize /data/clm.osrm
```

Lua profiles (`car.lua`, `bicycle.lua`, `foot.lua`) are bundled inside the
official `osrm/osrm-backend` Docker image — no separate download needed.

---

## Data sources

| Dataset | Source |
|---|---|
| Toledo urban GTFS (Feb–May 2026) | [NAP — Ministerio de Transportes](https://nap.transportes.gob.es/Files/Detail/1377) |
| OSM road network (Castilla-La Mancha) | [Geofabrik](https://download.geofabrik.de/europe/spain/castilla-la-mancha.html) |
| LPMC dataset | [Hillel et al. (2018)](https://doi.org/10.1680/jsmic.17.00018) — free access, [download CSV](https://www.emerald.com/jsmic/article-supplement/408759/csv/dataset/) |

---

## Academic context

**Title:** Web-based simulator for urban mobility scenarios using Artificial
Intelligence techniques

**Programme:** Master's Degree in Computer Engineering (Máster Universitario
en Ingeniería Informática), ESIIAB — University of Castilla-La Mancha (UCLM)

**Key references:**
- Hillel et al. (2018) — LPMC dataset
- Martín-Baos et al. (2023) — ML for travel mode choice (Transportation Research Part C)
- Chen & Guestrin (2016) — XGBoost

---

## License

Source code: MIT. Data files are subject to their respective original licenses
(see Data sources above).
