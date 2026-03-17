# CHEATSHEET - comandos rapidos (Windows / PowerShell)

## Rutas reales del proyecto

- Repo: `F:/TFM/movilidad-urbana-sim`
- OSRM: `F:/TFM/osrm-clm`
- OTP: `F:/TFM/otp-toledo`
- LPMC: `F:/TFM/lpmc`

## Estructura de datos esperada

- OSRM:
  - `F:/TFM/osrm-clm/car/clm.osm.pbf`
  - `F:/TFM/osrm-clm/bike/clm.osm.pbf`
  - `F:/TFM/osrm-clm/foot/clm.osm.pbf`
- OTP:
  - `F:/TFM/otp-toledo/clm.osm.pbf`
  - `F:/TFM/otp-toledo/GTFS_Urbano_Toledo.zip`
- GTFS para backend:
  - ZIP: `F:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo.zip`
  - carpeta extraida: `F:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo/`

## Preprocesado OSRM (solo cuando cambie el .pbf)

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

## Lanzar OSRM (uso normal)

```powershell
docker run -d --name osrm-car  -p 5000:5000 -v "f:/TFM/osrm-clm/car:/data"  osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm
docker run -d --name osrm-bike -p 5001:5000 -v "f:/TFM/osrm-clm/bike:/data" osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm
docker run -d --name osrm-foot -p 5002:5000 -v "f:/TFM/osrm-clm/foot:/data" osrm/osrm-backend:latest osrm-routed --algorithm mld /data/clm.osrm
```

## OTP (build y serve)

```powershell
# Solo cuando cambien OSM o GTFS
docker run --rm -v "f:/TFM/otp-toledo:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --build --save

# Uso diario
docker run -d --name otp-toledo -p 8080:8080 -v "f:/TFM/otp-toledo:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --load --serve
```

## GTFS backend (si actualizas el ZIP)

```powershell
Expand-Archive -Path "f:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo.zip" -DestinationPath "f:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo" -Force
```

## Backend y frontend

```powershell
# Backend
cd f:/TFM/movilidad-urbana-sim/backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload

# Frontend (otra terminal)
cd f:/TFM/movilidad-urbana-sim/frontend
npm run dev
```

## URLs y puertos

- Backend: `http://127.0.0.1:8000`
- Health: `http://127.0.0.1:8000/health`
- Frontend: `http://localhost:5173`
- OTP debug: `http://localhost:8080`
- OTP plan usado por backend: `http://localhost:8080/otp/routers/default/plan`
- OSRM usados por backend:
  - `http://127.0.0.1:5000`
  - `http://127.0.0.1:5001`
  - `http://127.0.0.1:5002`

## Parar y revisar

```powershell
docker stop osrm-car osrm-bike osrm-foot otp-toledo
docker rm osrm-car osrm-bike osrm-foot otp-toledo
docker ps
docker logs -f osrm-car
docker logs -f osrm-bike
docker logs -f osrm-foot
docker logs -f otp-toledo
```
