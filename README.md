# Simulador de Movilidad Urbana para Toledo

Repositorio principal del TFM y de la aplicación desarrollada en él. El proyecto integra una interfaz web cartográfica, un backend de orquestación, motores locales de enrutado y un bloque de modelado de elección modal para analizar alternativas de viaje en el entorno urbano de Toledo.

## Qué hace la aplicación

La aplicación permite:

- seleccionar origen y destino sobre un mapa interactivo;
- calcular rutas para coche, bicicleta y desplazamientos a pie mediante OSRM;
- consultar itinerarios de transporte público urbano mediante OpenTripPlanner y GTFS;
- visualizar rutas, segmentos y paradas sobre el mapa;
- servir de base para integrar inferencia de elección modal a partir del bloque LPMC.

## Arquitectura general

El proyecto se organiza en los siguientes bloques:

- `movilidad-urbana-sim/`: aplicación web del simulador.
  - `frontend/`: React + Vite + Leaflet.
  - `backend/`: FastAPI como capa de orquestación y API propia.
- `osrm-clm/`: datasets locales preparados para OSRM por perfil.
- `otp-toledo/`: datos y grafo local de OpenTripPlanner.
- `lpmc/`: scripts, modelos y artefactos del bloque de elección modal.
- `latex/`: memoria académica y figuras del TFM.
- `docker/` y `docker-compose.yml`: infraestructura de contenedores para levantar el sistema completo.

## Puesta en marcha

Desde `F:/TFM`:

```powershell
docker compose up --build
```

Servicios esperados:

- frontend: `http://127.0.0.1:5173`
- backend: `http://127.0.0.1:8000`
- backend health: `http://127.0.0.1:8000/health`
- osrm-car: `http://127.0.0.1:5000`
- osrm-bike: `http://127.0.0.1:5001`
- osrm-foot: `http://127.0.0.1:5002`
- otp: `http://127.0.0.1:8080`
- otp plan: `http://127.0.0.1:8080/otp/routers/default/plan`

## Datos necesarios

El repositorio no versiona en Git los artefactos pesados generados localmente. Antes de arrancar deben existir, como mínimo:

- `osrm-clm/car/clm.osrm` y `clm.osrm.*`
- `osrm-clm/bike/clm.osrm` y `clm.osrm.*`
- `osrm-clm/foot/clm.osrm` y `clm.osrm.*`
- `otp-toledo/graph.obj`
- modelos en `lpmc/models/`
- GTFS extraído en `movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo_2026/`

Importante:

- `osrm-clm/` y `otp-toledo/` sí son usados por Docker a través de los volúmenes montados en [`docker-compose.yml`](./docker-compose.yml).
- El backend no abre esos directorios directamente; consume OSRM y OTP por HTTP.
- El GTFS que usa el backend para paradas, líneas y horarios se lee desde `movilidad-urbana-sim/backend/data/gtfs/...`, no desde `otp-toledo/`.

## Fuentes de datos y referencias

Fuentes externas utilizadas en el proyecto:

- GTFS urbano de Toledo desde el NAP del Ministerio de Transportes y Movilidad Sostenible: <https://nap.mitma.es/>
- Extracto OSM de Castilla-La Mancha desde Geofabrik: <https://download.geofabrik.de/europe/spain/castilla-la-mancha.html>
- Documentación oficial de OSRM: <https://project-osrm.org/docs/>
- Repositorio oficial de OSRM: <https://github.com/Project-OSRM/osrm-backend>
- Documentación oficial de OpenTripPlanner: <https://docs.opentripplanner.org/>
- Imagen oficial de OpenTripPlanner en Docker Hub: <https://hub.docker.com/r/opentripplanner/opentripplanner>

Perfiles OSRM utilizados:

- `car.lua`
- `bicycle.lua`
- `foot.lua`

Estos perfiles proceden de la imagen oficial `osrm/osrm-backend`.

## Preparación de OSRM

Cada perfil necesita su propio `clm.osm.pbf` y su propio dataset generado.

Estructura esperada:

- `osrm-clm/car/clm.osm.pbf`
- `osrm-clm/bike/clm.osm.pbf`
- `osrm-clm/foot/clm.osm.pbf`

Comandos de preprocesado, solo cuando cambie el `.osm.pbf`:

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

## Preparación de OTP

En `otp-toledo/` deben estar disponibles:

- `clm.osm.pbf`
- `GTFS_Urbano_Toledo_2026.zip`
- `graph.obj`

Si cambian OSM o GTFS, regenera el grafo:

```powershell
docker run --rm -v "f:/TFM/otp-toledo:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --build --save
```

El arranque habitual del contenedor OTP usa `--load --serve`, por lo que necesita que `graph.obj` ya exista.

## Preparación del GTFS del backend

El backend espera el GTFS descomprimido en:

- `movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo_2026/`

Si actualizas el ZIP, vuelve a extraerlo:

```powershell
Expand-Archive -Path "f:/TFM/otp-toledo/GTFS_Urbano_Toledo_2026.zip" -DestinationPath "f:/TFM/movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo_2026" -Force
```

## Arranque manual

Solo tiene sentido si no usas `docker compose`.

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

## Endpoints principales

- `POST /api/osrm/routes`
- `POST /api/otp/routes`
- `GET /api/gtfs/stops`
- `GET /api/gtfs/routes`
- `GET /api/gtfs/routes/{route_id}`
- `GET /api/gtfs/routes/{route_id}/schedule`

## Bloque LPMC

Pipeline base:

```powershell
cd f:/TFM/lpmc
python 01_explore.py
python 02_preprocess.py
python 03_train_xgb_baseline.py
python 04_inspect_and_infer.py
```

## Memoria del TFM

La memoria académica extensa del trabajo se mantiene en:

- `latex/`

## Versionado

- Los datos pesados y regenerables no se suben al repositorio Git normal.
- El `.gitignore` ya excluye artefactos como `*.osrm`, `graph.obj`, `*.osm.pbf`, zips y modelos.
- Si necesitas compartir esos artefactos, es preferible usar una fuente externa, Git LFS o instrucciones de reconstrucción, no commits binarios pesados en GitHub.
