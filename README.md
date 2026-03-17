# TFM - Workspace Raiz

Este directorio raiz agrupa los bloques principales del TFM:

- `latex/`: memoria en LaTeX
- `movilidad-urbana-sim/`: frontend + backend del simulador
- `lpmc/`: scripts, modelos y artefactos de eleccion modal
- `osrm-clm/`: datos y perfiles de OSRM
- `otp-toledo/`: datos y grafo de OpenTripPlanner
- `papers/`: bibliografia y material de apoyo local

## Estado actual

Todavia existen repositorios Git anidados en:

- `latex/.git`
- `movilidad-urbana-sim/.git`
- `prediction-behavioural-analysis-ml-travel-mode-choice/.git`

Este README y la infraestructura Docker de la raiz preparan la migracion a un monorepo, pero no eliminan ni modifican esos repositorios internos.

## Arranque unificado con Docker Compose

Desde `F:/TFM`:

```powershell
docker compose up --build
```

Servicios que se levantan:

- `frontend`: `http://127.0.0.1:5173`
- `backend`: `http://127.0.0.1:8000`
- `osrm-car`: `http://127.0.0.1:5000`
- `osrm-bike`: `http://127.0.0.1:5001`
- `osrm-foot`: `http://127.0.0.1:5002`
- `otp`: `http://127.0.0.1:8080`

Imagenes usadas:

- `osrm/osrm-backend:latest`
- `opentripplanner/opentripplanner:2.5.0`

## Requisitos de datos

Antes de usar `docker compose`, deben existir ya los datos y artefactos pesados:

- `osrm-clm/car/clm.osrm` y derivados
- `osrm-clm/bike/clm.osrm` y derivados
- `osrm-clm/foot/clm.osrm` y derivados
- `otp-toledo/graph.obj`
- modelos de `lpmc/models/`
- GTFS extraido en `movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo/`

La infraestructura Docker de esta raiz no genera esos artefactos; solo orquesta los servicios una vez preparados.

## Migracion recomendada a monorepo

Cuando quieras unificar el control de cambios, el orden razonable es:

1. hacer copia de seguridad o confirmar que los repos internos estan limpios;
2. crear un Git unico en `F:/TFM`;
3. eliminar o archivar los `.git` internos;
4. versionar solo codigo, configuracion, memoria y scripts;
5. mantener fuera de Git los datos pesados y artefactos generados.

Hasta completar esa migracion, usa esta raiz como capa de coordinacion y documentacion.
