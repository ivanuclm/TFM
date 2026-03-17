# Simulador web de movilidad urbana (TFM)

README operativo actualizado al estado real del proyecto en `F:/TFM`.
Si necesitas el texto antiguo, esta en `README_old.md`.

## 1) Estado actual del repositorio

Este repo (`F:/TFM/movilidad-urbana-sim`) tiene ahora:

- `backend/`: FastAPI con endpoints OSRM, OTP y GTFS.
- `frontend/`: React + Vite + Leaflet.
- `CHEATSHEET.md`: comandos rapidos para levantar todo.

La parte de IA esta en `F:/TFM/lpmc` (fuera de esta carpeta), con scripts y notebooks para LPMC + XGBoost.

## 2) Rutas reales que se usan

- Repo web: `F:/TFM/movilidad-urbana-sim`
- OSRM (datos CLM): `F:/TFM/osrm-clm`
- OTP (Toledo): `F:/TFM/otp-toledo`
- IA/LPMC: `F:/TFM/lpmc`

### 2.1 OSRM

Carpetas esperadas:

- `F:/TFM/osrm-clm/car`
- `F:/TFM/osrm-clm/bike`
- `F:/TFM/osrm-clm/foot`

Cada una debe tener:

- `clm.osm.pbf`
- `clm.osrm` + `clm.osrm.*` (tras extract/partition/customize)

### 2.2 OTP

En `F:/TFM/otp-toledo`:

- `clm.osm.pbf`
- `GTFS_Urbano_Toledo.zip`
- `graph.obj` (se crea con `--build --save`)

### 2.3 GTFS que lee el backend

El backend NO lee directamente el zip de OTP. Lee la carpeta extraida en:

- `F:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo/`

Si actualizas el zip en backend:

```powershell
Expand-Archive -Path "f:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo.zip" -DestinationPath "f:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo" -Force
```

## 3) Puertos y URLs que espera tu codigo

Segun `backend/app/services/osrm_client.py` y `backend/app/api/routes_otp.py`:

- OSRM coche: `http://127.0.0.1:5000`
- OSRM bici: `http://127.0.0.1:5001`
- OSRM pie: `http://127.0.0.1:5002`
- OTP plan: `http://localhost:8080/otp/routers/default/plan`

Nota importante OSRM:

- Tu cliente llama a `/route/v1/driving/...` en las 3 instancias.
- Por eso cada contenedor debe exponer un dataset ya preparado para su perfil (car/bike/foot), aunque el path sea `driving`.

## 4) Preprocesado de datos de enrutado

### 4.1 Preparar `clm.osm.pbf` en cada carpeta de OSRM

Si solo tienes uno en la raiz (`F:/TFM/osrm-clm/clm.osm.pbf`), copialo:

```powershell
Copy-Item "f:/TFM/osrm-clm/clm.osm.pbf" "f:/TFM/osrm-clm/car/clm.osm.pbf" -Force
Copy-Item "f:/TFM/osrm-clm/clm.osm.pbf" "f:/TFM/osrm-clm/bike/clm.osm.pbf" -Force
Copy-Item "f:/TFM/osrm-clm/clm.osm.pbf" "f:/TFM/osrm-clm/foot/clm.osm.pbf" -Force
```

### 4.2 Preprocesar OSRM (solo cuando cambia OSM)

```powershell
# CAR
docker run --rm -t -v "f:/TFM/osrm-clm/car:/data" osrm/osrm-backend:v5.27.0 osrm-extract -p /opt/car.lua /data/clm.osm.pbf
docker run --rm -t -v "f:/TFM/osrm-clm/car:/data" osrm/osrm-backend:v5.27.0 osrm-partition /data/clm.osrm
docker run --rm -t -v "f:/TFM/osrm-clm/car:/data" osrm/osrm-backend:v5.27.0 osrm-customize /data/clm.osrm

# BIKE
docker run --rm -t -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:v5.27.0 osrm-extract -p /opt/bicycle.lua /data/clm.osm.pbf
docker run --rm -t -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:v5.27.0 osrm-partition /data/clm.osrm
docker run --rm -t -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:v5.27.0 osrm-customize /data/clm.osrm

# FOOT
docker run --rm -t -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:v5.27.0 osrm-extract -p /opt/foot.lua /data/clm.osm.pbf
docker run --rm -t -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:v5.27.0 osrm-partition /data/clm.osrm
docker run --rm -t -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:v5.27.0 osrm-customize /data/clm.osrm
```

### 4.3 Build OTP (solo cuando cambian OSM o GTFS)

```powershell
docker run --rm -v "f:/TFM/otp-toledo:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --build --save
```

## 5) Arranque diario de servicios

### 5.1 OSRM

```powershell
docker run -d --name osrm-car  -p 5000:5000 -v "f:/TFM/osrm-clm/car:/data"  osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm
docker run -d --name osrm-bike -p 5001:5000 -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm
docker run -d --name osrm-foot -p 5002:5000 -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm
```

### 5.2 OTP

```powershell
docker run -d --name otp-toledo -p 8080:8080 -v "f:/TFM/otp-toledo:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --load --serve
```

### 5.3 Backend (FastAPI)

```powershell
cd f:/TFM/movilidad-urbana-sim/backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

API:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/docs`

### 5.4 Frontend (React + Vite)

```powershell
cd f:/TFM/movilidad-urbana-sim/frontend
npm run dev
```

Frontend:

- `http://localhost:5173`

## 6) Endpoints principales backend

- `POST /api/osrm/routes`
- `POST /api/otp/routes`
- `GET /api/gtfs/stops?limit=5000`
- `GET /api/gtfs/routes`
- `GET /api/gtfs/routes/{route_id}`
- `GET /api/gtfs/routes/{route_id}/schedule?date=YYYY-MM-DD`

## 7) Dependencias backend (estado real)

Existe `requirements.txt` en `backend/` para facilitar dockerizacion y recreacion del entorno.

Si creas un entorno nuevo desde cero:

```powershell
cd f:/TFM/movilidad-urbana-sim/backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi "uvicorn[standard]" httpx polyline
```

## 8) IA (LPMC) - ubicacion y ejecucion rapida

Carpeta:

- `F:/TFM/lpmc`

Datos actuales detectados:

- `data/raw/LPMC_dataset.csv`
- `data/processed/LPMC_processed.csv`
- `data/preprocessed/LPMC_train.csv`
- `data/preprocessed/LPMC_test.csv`

Modelos detectados:

- `models/xgb_lpmc_baseline.joblib`
- `models/xgb_lpmc_tuned.joblib`
- `models/xgb_lpmc_scaler.joblib`

Pipeline base:

```powershell
cd f:/TFM/lpmc
python 01_explore.py
python 02_preprocess.py
python 03_train_xgb_baseline.py
python 04_inspect_and_infer.py
```

## 9) Parar contenedores y debug

```powershell
docker stop osrm-car osrm-bike osrm-foot otp-toledo
docker rm osrm-car osrm-bike osrm-foot otp-toledo
docker ps

docker logs -f osrm-car
docker logs -f osrm-bike
docker logs -f osrm-foot
docker logs -f otp-toledo
```

## 10) Incoherencias antiguas ya resueltas en este README

- Se elimina referencia a `backend/core/config.py` (no existe en tu repo actual).
- Se elimina dependencia de `requirements.txt` como requisito obligatorio.
- Se corrige la arquitectura OSRM real (3 instancias locales en 5000/5001/5002).
- Se separa claramente GTFS de OTP y GTFS que consume FastAPI.
- Se dejan rutas absolutas alineadas con tu entorno (`F:/TFM/...`).
