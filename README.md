# Simulador web de movilidad urbana – TFM

Este repositorio contiene el código del Trabajo Fin de Máster orientado al **análisis y simulación de escenarios de movilidad urbana** en la ciudad de Toledo. El sistema integra:

- Un **frontend React + Vite** con mapa interactivo (Leaflet) para fijar origen/destino y explorar rutas.
- Un **backend FastAPI** que actúa como capa de orquestación sobre:
  - Tres instancias de **OSRM** en local (coche, bici y a pie).
  - Una instancia de **OpenTripPlanner (OTP)** en local con la red viaria de Castilla-La Mancha y el GTFS urbano de Toledo.
  - Scripts de preprocesado y modelos de **elección modal** entrenados sobre el dataset **LPMC (London Passenger Mode Choice)**.

El objetivo final es disponer de un simulador capaz de combinar tiempos y distancias reales de red (OSRM/OTP) con preferencias aprendidas a partir del LPMC para estimar qué modo de transporte escogería un usuario en Toledo (walk, cycle, pt, drive).

Nota de organizacion:
Actualmente existe ademas una capa de orquestacion en la raiz `F:/TFM`, con `docker-compose.yml`, pensada para coordinar frontend, backend, OSRM y OTP desde un unico punto de entrada. Este README sigue siendo valido como referencia tecnica del simulador, pero el arranque unificado se documenta en `F:/TFM/README.md`.

---

## 1. Estructura del repositorio

A alto nivel la estructura relevante es:

```text
TFM/
├─ movilidad-urbana-sim/
│  ├─ backend/               # API FastAPI (OSRM, OTP, GTFS Toledo)
│  ├─ frontend/              # Aplicación React + Leaflet
│  └─ README.md              # Este archivo
├─ lpmc/
│  ├─ data/
│  │  ├─ raw/                # LPMC_dataset.csv original
│  │  ├─ processed/          # Versión procesada "tipo profesor"
│  │  └─ preprocessed/       # LPMC_train.csv / LPMC_test.csv generados por mis scripts
│  ├─ models/                # xgb_lpmc_baseline.joblib, xgb_lpmc_scaler.joblib
│  ├─ 01_explore.py          # Exploración inicial del dataset
│  ├─ 02_preprocess.py       # Preprocesado LPMC (replica 0-Process-LPMC.py)
│  ├─ 03_train_xgb_baseline.py
│  └─ 04_inspect_and_infer.py
└─ ...
```

Dentro de `movilidad-urbana-sim`:

```text
backend/
├─ app/
│  ├─ api/
│  │  ├─ routes_osrm.py      # Endpoints de enrutado con OSRM
│  │  ├─ routes_otp.py       # Endpoints de enrutado con OTP
│  │  ├─ routes_gtfs.py      # Endpoints de exploración GTFS (paradas, rutas, horarios)
│  │  └─ ...
│  ├─ core/
│  │  └─ config.py           # Configuración básica FastAPI/CORS
│  └─ main.py                # Punto de entrada FastAPI
└─ ...

frontend/
├─ src/
│  ├─ components/
│  │  └─ MapView.tsx         # Mapa Leaflet + rutas + paradas GTFS
│  ├─ App.tsx                # UI principal del simulador
│  └─ ...
└─ ...
```

---

## 2. Requisitos previos

### 2.1. Software base

- Docker / Docker Desktop (para levantar OSRM y OTP).
- Python 3.11+ (proyecto probado con 3.11/3.12).
- Node.js 20+ y pnpm o npm (para el frontend).
- Git (para clonar el repositorio).

### 2.2. Datos externos necesarios

1. **Red viaria**: fichero `.osm.pbf` de Castilla-La Mancha (o el área que se quiera usar). En este TFM se usa:

   - `clm.osm.pbf` (Castilla-La Mancha), descargado desde Geofabrik.

2. **GTFS urbano de Toledo**: fichero zip con el feed GTFS. En el proyecto se usa:

   - `GTFS_Urbano_Toledo.zip`

3. **Dataset LPMC original** (no se versiona en Git):
   - `LPMC_dataset.csv` colocado en `lpmc/data/raw/`.

---

## 3. Puesta en marcha de los servicios de enrutado

### 3.1. OSRM en local (3 perfiles: coche, bici, a pie)

Se utilizan tres contenedores OSRM separados, cada uno con su perfil y un puerto distinto:

- `5000` – Coche (`car`).
- `5001` – Bicicleta (`bike`).
- `5002` – A pie (`foot`).

Supongamos que la estructura es:

```text
TFM/
└─ osrm/
   ├─ clm.osm.pbf
   └─ profiles/
      ├─ car.lua
      ├─ bike.lua
      └─ foot.lua
```

#### 3.1.1. Preparar los ficheros `.osrm` (una vez)

Desde `TFM/osrm`:

```bash
# Coche
docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend:latest osrm-extract -p /data/profiles/car.lua /data/clm.osm.pbf

docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend:latest osrm-partition /data/clm.osrm

docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend:latest osrm-customize /data/clm.osrm
```

Para bici y a pie, si se quiere afinar al máximo se pueden generar `.osrm` separados con otros perfiles. En el PoC actual se utiliza el mismo `.osrm` pero se exponen tres servidores con diferentes perfiles.

#### 3.1.2. Levantar los servidores OSRM

```bash
# Coche (perfil car) en 5000
docker run --rm -t -p 5000:5000 -v "${PWD}:/data" osrm/osrm-backend:latest \
  osrm-routed --algorithm mld /data/clm.osrm

# Bici (perfil bike) en 5001
docker run --rm -t -p 5001:5000 -v "${PWD}:/data" osrm/osrm-backend:latest \
  osrm-routed --algorithm mld --max-table-size 1000 /data/clm.osrm \
  --profile /data/profiles/bike.lua

# A pie (perfil foot) en 5002
docker run --rm -t -p 5002:5000 -v "${PWD}:/data" osrm/osrm-backend:latest \
  osrm-routed --algorithm mld --max-table-size 1000 /data/clm.osrm \
  --profile /data/profiles/foot.lua
```

El backend FastAPI asume por defecto estos puertos:

- `http://localhost:5000/route/v1/car/...`
- `http://localhost:5001/route/v1/bike/...`
- `http://localhost:5002/route/v1/foot/...`

Si se cambian, hay que actualizar la configuración en `routes_osrm.py` (o en el módulo de configuración).

### 3.2. OpenTripPlanner (OTP) en local

Para OTP se ha seguido la versión **2.5.0** desde la imagen oficial de Docker.

#### 3.2.1. Directorio de trabajo

```text
TFM/
└─ otp-toledo/
   ├─ clm.osm.pbf
   ├─ GTFS_Urbano_Toledo.zip
   └─ graph.obj           # se genera en el paso de build
```

#### 3.2.2. Construir el grafo

Desde `TFM/otp-toledo`:

```bash
docker run --rm -v "${PWD}:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --build --save
```

Esto detecta `clm.osm.pbf` y `GTFS_Urbano_Toledo.zip`, construye el grafo y genera `graph.obj` en el mismo directorio.

#### 3.2.3. Servir OTP

```bash
docker run --rm -v "${PWD}:/var/opentripplanner" -p 8080:8080 opentripplanner/opentripplanner:2.5.0 --load --serve
```

La interfaz de **Debug UI** estará disponible en:

- `http://localhost:8080`

Y el endpoint de planificación que usa el backend es:

- `http://localhost:8080/otp/routers/default/plan`

---

## 4. Backend FastAPI

### 4.1. Instalación de dependencias

Desde `TFM/movilidad-urbana-sim/backend`:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Las dependencias principales incluyen:

- `fastapi`, `uvicorn`
- `httpx`
- `pydantic`
- `polyline`
- `pandas` (para GTFS y futuros usos)
- `scikit-learn`, `xgboost`, `joblib` (para el modelo LPMC, en la siguiente fase)

### 4.2. Lanzar el backend

```bash
uvicorn app.main:app --reload
```

Por defecto se sirve en:

- `http://127.0.0.1:8000`

Endpoints principales (ejemplos):

- `POST /api/osrm/routes`
  - Body: `{ "origin": {lat, lon}, "destination": {lat, lon}, "profiles": ["driving","cycling","foot"] }`
  - Devuelve distancias, duraciones y geometrías por modo (OSRM).

- `POST /api/otp/routes`
  - Body: `{ "origin": {lat, lon}, "destination": {lat, lon}, "itinerary_index": 0 }`
  - Llama a OTP, ordena los itinerarios por duración, permite paginar (`itinerary_index`) y devuelve:
    - Ruta completa concatenada.
    - Lista de **segmentos** por modo (`segments`), con distinción visual entre tramos a pie y en bus.
    - Índice y número total de itinerarios (`itinerary_index`, `total_itineraries`).

- `GET /api/gtfs/stops?limit=5000`
  - Devuelve todas las paradas GTFS, incluyendo referencia a las rutas que pasan por cada una.

- `GET /api/gtfs/routes`
  - Devuelve la lista de líneas de transporte público.

- `GET /api/gtfs/routes/{route_id}`
  - Devuelve paradas ordenadas y shape de la línea GTFS seleccionada.

- `GET /api/gtfs/routes/{route_id}/schedule?date=YYYY-MM-DD`
  - Devuelve horarios agregados por dirección (nº de viajes, primeras/últimas salidas, etc.).

En una fase posterior se añadirá un endpoint de inferencia de elección modal, que llamará al modelo entrenado sobre LPMC.

---

## 5. Frontend React + Leaflet

### 5.1. Instalación y arranque

Desde `TFM/movilidad-urbana-sim/frontend`:

```bash
pnpm install   # o npm install
pnpm dev       # o npm run dev
```

La aplicación se servirá por defecto en `http://localhost:5173`.

### 5.2. Funcionalidad actual

- El mapa (Leaflet, `MapView.tsx`) muestra:
  - Origen y destino (marcadores personalizados).
  - La ruta seleccionada según el modo (`Coche`, `Bici`, `A pie`, `Transporte público`).
  - Paradas GTFS de Toledo (puntos azules).
  - Paradas de la línea GTFS seleccionada (círculos naranjas).
  - Segmentos OTP:
    - Tramos a pie como líneas grises discontinuas.
    - Tramos en bus como líneas naranjas continuas.

- El panel lateral permite:
  - Activar/desactivar la visualización de paradas GTFS.
  - Seleccionar una línea concreta desde desplegable o clicando una parada en el mapa.
  - Calcular rutas OSRM+OTP para el origen/destino actual.
  - Cambiar de modo (`Coche`, `Bici`, `A pie`, `Transporte público`), resaltando la ruta correspondiente.
  - Ver una tabla con distancias y duraciones por modo.
  - Paginador de itinerarios OTP (`Anterior / Siguiente`) ordenados por duración.

En el bloque de **transporte público (GTFS)** se muestran además:
- Nombre de la línea seleccionada y número de paradas.
- Selector de fecha `date` para los horarios.
- Resumen de horarios por dirección (headsign, nº de viajes, primera y última salida, listado de salidas).

---

## 6. Preprocesado y modelo LPMC (carpeta `lpmc/`)

Aunque el modelo LPMC aún no está integrado en el backend, ya se ha dejado preparada una pipeline reproducible en `TFM/lpmc`.

### 6.1. Scripts

1. `01_explore.py`
   - Carga el fichero `data/raw/LPMC_dataset.csv` (original).
   - Muestra shape, primeras filas, tipos de datos y estadísticas básicas.

2. `02_preprocess.py`
   - Replica la lógica del script del profesor `0-Process-LPMC.py`:
     - One-hot de `purpose`.
     - Agrupación y one-hot de `fueltype`.
     - Mapeo de `travel_mode` a {0: walk, 1: cycle, 2: pt, 3: drive}.
     - Eliminación de columnas auxiliares: `trip_id`, `person_n`, `trip_n`, fechas desglosadas, campos de coste redundantes, etc.
     - División en train/test según `survey_year` (años 1–2 train, año 3 test).
   - Guarda:
     - `data/preprocessed/LPMC_train.csv`
     - `data/preprocessed/LPMC_test.csv`

3. `03_train_xgb_baseline.py`
   - Carga train/test ya preprocesados.
   - Separa `X` e `y` (variable objetivo = `travel_mode`).
   - Aplica un `StandardScaler` a un subconjunto de variables numéricas relevantes
     (`day_of_week`, `start_time_linear`, `age`, `car_ownership`, `distance`, etc.).
   - Entrena un XGBoost multicategoría con hiperparámetros de referencia.
   - Evalúa accuracy en train y test (≈ 0.83 / 0.73) y guarda:
     - `models/xgb_lpmc_baseline.joblib`
     - `models/xgb_lpmc_scaler.joblib`

4. `04_inspect_and_infer.py`
   - Carga el modelo y el scaler.
   - Reaplica el mismo escalado sobre el test.
   - Realiza predicciones y muestra:
     - Ejemplos individuales con probabilidades por clase.
     - Matriz de confusión (en consola y con `ConfusionMatrixDisplay`).

Estas rutas y ficheros están pensados para que, en una fase posterior, el backend pueda cargar `joblib` y exponer un endpoint `/api/lpmc/predict` que, dado el escenario de Toledo (duraciones y costes por modo, día de la semana, hora, etc.), devuelva la probabilidad de elección modal para ese caso.

---

## 7. Flujo de trabajo típico para el simulador

1. **Arrancar servicios externos**:
   - OSRM (tres contenedores para coche/bici/a pie).
   - OTP con grafo de Toledo.

2. **Levantar backend FastAPI** (`uvicorn app.main:app --reload`).

3. **Levantar frontend React** (`pnpm dev`).

4. **Interactuar con la aplicación**:
   - Fijar origen y destino haciendo clic alterno en el mapa.
   - Pulsar en `Calcular rutas` para obtener tiempos y distancias OSRM/OTP.
   - Alternar modos, navegar entre itinerarios de transporte público y examinar horarios GTFS.

5. **(Opcional, para experimentos de elección modal)**:
   - Ejecutar scripts de `lpmc/` para recrear el experimento con LPMC.
   - Usar `04_inspect_and_infer.py` para probar el modelo sobre el test de Londres.

---

## 8. Trabajo futuro e integración con el modelo LPMC

El siguiente paso natural del TFM es:

1. Definir un esquema de **traslado de variables LPMC → Toledo**:
   - Qué atributos están disponibles en el simulador (distancias/tiempos por modo, costes aproximados, día/hora, características sociodemográficas supuestas del usuario, etc.).
   - Cómo mapearlos a las columnas que espera el modelo XGBoost.

2. Implementar un endpoint en el backend (`/api/lpmc/predict`) que:
   - Tome un escenario de Toledo (origen/destino + contexto).
   - Llame a OSRM/OTP para obtener los tiempos y costes por modo.
   - Construya el vector de entrada compatible con `xgb_lpmc_baseline`.
   - Devuelva las probabilidades de elegir walk / cycle / pt / drive.

3. Incorporar las probabilidades al frontend:
   - Visualizar, por ejemplo, un gráfico de barras con la probabilidad de elección modal para el escenario actual.
   - Permitir comparar escenarios (cambios en frecuencias de bus, carriles bici, etc.) viendo cómo varía la elección modal prevista.

Con esto, el simulador pasará de ser una herramienta descriptiva (rutas y tiempos) a una herramienta **predictiva**, basada en preferencias aprendidas a partir del LPMC.
