# Runbook

Guia operativa del entorno local del TFM en Windows/PowerShell.

## Rutas reales

- repo raiz: `F:/TFM`
- simulador: `F:/TFM/movilidad-urbana-sim`
- OSRM: `F:/TFM/osrm-clm`
- OTP: `F:/TFM/otp-toledo`
- LPMC: `F:/TFM/lpmc`

## Datos esperados

## Origen de los datos

- GTFS urbano de Toledo: NAP del Ministerio de Transportes y Movilidad Sostenible.
- Red viaria de base: OpenStreetMap a traves del extracto de Castilla-La Mancha publicado por Geofabrik.
- Perfiles OSRM utilizados en el preprocesado: `car.lua`, `bicycle.lua` y `foot.lua` incluidos en la imagen oficial de `osrm/osrm-backend`.

### OSRM

Cada perfil debe tener su propio dataset preparado:

- `F:/TFM/osrm-clm/car/clm.osm.pbf`
- `F:/TFM/osrm-clm/bike/clm.osm.pbf`
- `F:/TFM/osrm-clm/foot/clm.osm.pbf`
- `clm.osrm` y `clm.osrm.*` en cada carpeta

### OTP

En `F:/TFM/otp-toledo`:

- `clm.osm.pbf`
- `GTFS_Urbano_Toledo.zip`
- `graph.obj`

### GTFS backend

El backend lee el GTFS extraido en:

- `F:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo/`

Si actualizas el zip:

```powershell
Expand-Archive -Path "f:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo.zip" -DestinationPath "f:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo" -Force
```

## Preprocesado OSRM

Solo cuando cambie el `.osm.pbf`.

Los comandos usan los perfiles oficiales incluidos en la imagen:

- `/opt/car.lua`
- `/opt/bicycle.lua`
- `/opt/foot.lua`

```powershell
# CAR
docker run --rm -t -v "f:/TFM/osrm-clm/car:/data" osrm/osrm-backend:latest osrm-extract -p /opt/car.lua /data/clm.osm.pbf
docker run --rm -t -v "f:/TFM/osrm-clm/car:/data" osrm/osrm-backend:latest osrm-partition /data/clm.osrm
docker run --rm -t -v "f:/TFM/osrm-clm/car:/data" osrm/osrm-backend:latest osrm-customize /data/clm.osrm

# BIKE
docker run --rm -t -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:latest osrm-extract -p /opt/bicycle.lua /data/clm.osm.pbf
docker run --rm -t -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:latest osrm-partition /data/clm.osrm
docker run --rm -t -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:latest osrm-customize /data/clm.osrm

# FOOT
docker run --rm -t -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:latest osrm-extract -p /opt/foot.lua /data/clm.osm.pbf
docker run --rm -t -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:latest osrm-partition /data/clm.osrm
docker run --rm -t -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:latest osrm-customize /data/clm.osrm
```

## Build OTP

Solo cuando cambien OSM o GTFS:

- OSM base: extracto de Castilla-La Mancha.
- GTFS base: feed urbano de Toledo descargado del NAP.

```powershell
docker run --rm -v "f:/TFM/otp-toledo:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --build --save
```

## Arranque diario

### Opcion recomendada

```powershell
cd f:/TFM
docker compose up --build
```

### Arranque manual

```powershell
# OSRM
docker run -d --name osrm-car  -p 5000:5000 -v "f:/TFM/osrm-clm/car:/data"  osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm
docker run -d --name osrm-bike -p 5001:5000 -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm
docker run -d --name osrm-foot -p 5002:5000 -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm

# OTP
docker run -d --name otp-toledo -p 8080:8080 -v "f:/TFM/otp-toledo:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --load --serve

# Backend
cd f:/TFM/movilidad-urbana-sim/backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload

# Frontend
cd f:/TFM/movilidad-urbana-sim/frontend
npm run dev
```

## URLs y puertos

- backend: `http://127.0.0.1:8000`
- health: `http://127.0.0.1:8000/health`
- frontend: `http://127.0.0.1:5173`
- otp debug: `http://127.0.0.1:8080`
- otp plan: `http://localhost:8080/otp/routers/default/plan`
- osrm car: `http://127.0.0.1:5000`
- osrm bike: `http://127.0.0.1:5001`
- osrm foot: `http://127.0.0.1:5002`

## Endpoints backend

- `POST /api/osrm/routes`
- `POST /api/otp/routes`
- `GET /api/gtfs/stops?limit=5000`
- `GET /api/gtfs/routes`
- `GET /api/gtfs/routes/{route_id}`
- `GET /api/gtfs/routes/{route_id}/schedule?date=YYYY-MM-DD`

## LPMC

Pipeline base:

```powershell
cd f:/TFM/lpmc
python 01_explore.py
python 02_preprocess.py
python 03_train_xgb_baseline.py
python 04_inspect_and_infer.py
```

## Parada y logs

```powershell
docker stop osrm-car osrm-bike osrm-foot otp-toledo
docker rm osrm-car osrm-bike osrm-foot otp-toledo
docker ps
docker logs -f osrm-car
docker logs -f osrm-bike
docker logs -f osrm-foot
docker logs -f otp-toledo
```
