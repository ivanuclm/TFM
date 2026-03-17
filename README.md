# TFM

Monorepo de trabajo del TFM con tres bloques principales:

- `latex/`: memoria y recursos en LaTeX.
- `movilidad-urbana-sim/`: simulador web de movilidad urbana.
- `lpmc/`: scripts y artefactos del modelo de eleccion modal.

Ademas contiene los datos y la infraestructura local necesarios para ejecutar los servicios de enrutado:

- `osrm-clm/`: datasets preparados para OSRM.
- `otp-toledo/`: datos y grafo de OpenTripPlanner.
- `docker-compose.yml`: arranque coordinado de frontend, backend, OSRM y OTP.

## Documentacion raiz

La documentacion util queda centralizada aqui:

- `README.md`: mapa del repositorio y punto de entrada.
- `RUNBOOK.md`: operacion diaria, comandos y puertos.
- `MEMORIA_TECNICA.md`: arquitectura y evolucion tecnica del simulador.

La documentacion interna de `movilidad-urbana-sim/` se ha reducido a un README corto para evitar duplicidad.

## Estructura

```text
TFM/
|- latex/
|- movilidad-urbana-sim/
|  |- backend/
|  |- frontend/
|- lpmc/
|- osrm-clm/
|  |- car/
|  |- bike/
|  |- foot/
|- otp-toledo/
|- papers/
|- docker/
|- docker-compose.yml
|- README.md
|- RUNBOOK.md
`- MEMORIA_TECNICA.md
```

## Arranque rapido

Desde `F:/TFM`:

```powershell
docker compose up --build
```

Servicios esperados:

- frontend: `http://127.0.0.1:5173`
- backend: `http://127.0.0.1:8000`
- osrm-car: `http://127.0.0.1:5000`
- osrm-bike: `http://127.0.0.1:5001`
- osrm-foot: `http://127.0.0.1:5002`
- otp: `http://127.0.0.1:8080`

## Requisitos de datos

Antes del arranque deben existir ya los artefactos pesados, que no se versionan en Git:

- `osrm-clm/car/clm.osrm` y derivados
- `osrm-clm/bike/clm.osrm` y derivados
- `osrm-clm/foot/clm.osrm` y derivados
- `otp-toledo/graph.obj`
- modelos en `lpmc/models/`
- GTFS extraido en `movilidad-urbana-sim/backend/data/gtfs/GTFS_Urbano_Toledo/`

## Origen de datos y perfiles

Los recursos base del sistema proceden de estas fuentes:

- GTFS urbano de Toledo: descarga desde el NAP del Ministerio de Transportes y Movilidad Sostenible.
- Geografia viaria base: extracto OSM de Castilla-La Mancha descargado desde Geofabrik.
- Perfiles de enrutado OSRM: perfiles base de la imagen oficial de `osrm/osrm-backend`, usando `car.lua`, `bicycle.lua` y `foot.lua`.

Sobre esos insumos se generan localmente:

- los datasets `.osrm` para coche, bici y a pie;
- el `graph.obj` de OTP;
- la carpeta GTFS extraida que consume el backend.

## Estado del versionado

El historial heredado que se conserva en el monorepo es el de `movilidad-urbana-sim/`, importado mediante `git subtree`.

Los backups de repos Git antiguos no deben formar parte del repo. El `.gitignore` ya los excluye.

## Criterio de documentacion

- Lo operativo y transversal va a la raiz.
- La documentacion del subproyecto debe limitarse a detalles internos que no dupliquen la raiz.
- Los datos pesados, binarios y artefactos generados permanecen fuera de Git.
