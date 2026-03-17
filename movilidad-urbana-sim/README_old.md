# Simulador de movilidad urbana (PoC)

Prueba de concepto para el Trabajo Fin de Máster sobre un **simulador web de escenarios de movilidad urbana**. El objetivo de esta PoC es disponer de una base técnica sólida:

- Backend en **FastAPI** que consulta servicios OSRM (locales y remotos) para distintos modos de transporte.
- Frontend en **Vite + React + TypeScript** con **Leaflet** para la visualización sobre mapa.
- Comparación de rutas para **coche, bici y a pie**, con distancias, tiempos e itinerario dibujado en el mapa.
- Capa adicional de **paradas de transporte público** a partir de un feed **GTFS** real.

> ⚠️ Nota: esta PoC no integra todavía el modelo de Machine Learning (LPMC). Se centra en la parte de trayectos y enrutado, y en una primera integración con datos GTFS. El modelo se conectará en fases posteriores del TFM.

---

## 1. Arquitectura general

El proyecto está dividido en dos carpetas principales:

- `backend/` – API REST en FastAPI.
- `frontend/` – aplicación web en React/Vite.

### Backend (FastAPI)

- Framework: **FastAPI** (Python 3.11).
- Cliente HTTP: **httpx**.
- Modelos de datos: **Pydantic**.
- Endpoints principales:
  - `POST /api/osrm/routes` → cálculo de rutas para coche, bici y a pie.
  - `GET  /api/gtfs/stops`  → listado de paradas de transporte público desde un feed GTFS.

El endpoint `/api/osrm/routes` recibe un origen, un destino y una lista de perfiles (`driving`, `cycling`, `foot`), y devuelve para cada uno:

- distancia en metros,
- duración en segundos,
- geometría de la ruta como lista de puntos `{lat, lon}`.

### Frontend (Vite + React)

- Bundler/dev server: **Vite**.
- UI: **React** + **TypeScript**.
- Gestión de peticiones y estado de red: **@tanstack/react-query**.
- Mapas: **Leaflet** + **react-leaflet**.

La interfaz permite:

1. Hacer clic en el mapa para fijar alternadamente **origen** y **destino**.
2. Pulsar el botón **“Calcular rutas OSRM”** para consultar el backend.
3. Visualizar una tabla con distancias y tiempos para coche, bici y a pie.
4. Seleccionar el modo (Coche/Bici/A pie) y ver la ruta correspondiente dibujada sobre el mapa.
5. Visualizar paradas de transporte público desde un feed GTFS real (por ejemplo, CRTM).

---

## 2. Decisiones sobre servicios OSRM

### 2.1. Por qué no usar solo el demoserver oficial de OSRM

Durante las primeras pruebas se utilizó el demoserver oficial de OSRM:

- `https://router.project-osrm.org/route/v1/{profile}/...`

Aunque la API permite indicar distintos perfiles (`driving`, `cycling`, `foot`), la propia comunidad de OSRM indica en sus issues que **el demoserver solo tiene cargado el dataset del perfil de coche**. En la práctica esto se traduce en que:

- las peticiones con `cycling` o `foot` devuelven exactamente la misma distancia y duración que `driving`;
- por tanto, no sirven para analizar comparativamente distintos modos de transporte, que es justo el objetivo del TFM.

Enlaces de interés:

- https://github.com/Project-OSRM/osrm-backend/issues/4868
- https://github.com/Project-OSRM/osrm-backend/wiki/Demo-server
- https://project-osrm.org/docs/v5.5.1/api/#general-options

### 2.2. Uso de `routing.openstreetmap.de`

Para disponer de rutas diferenciadas por modo sin montar todavía una infraestructura propia, se optó inicialmente por usar las instancias OSRM públicas de FOSSGIS:

- `https://routing.openstreetmap.de/routed-car`
- `https://routing.openstreetmap.de/routed-bike`
- `https://routing.openstreetmap.de/routed-foot`

Estas instancias:

- exponen la API OSRM v5,
- cuentan con perfiles separados para coche, bici y peatón,
- y son suficientes para una PoC académica con tráfico moderado.

### 2.3. Estrategia híbrida: OSRM local para coche, remoto para bici y a pie

Tras validar la PoC, se dio un paso más y se montó una instancia propia de OSRM para el modo **coche**, utilizando:

- un extracto OSM de **Castilla-La Mancha** descargado desde Geofabrik (`castilla-la-mancha-251209.osm.pbf`),
- la imagen oficial `osrm/osrm-backend`,
- y el perfil `/opt/car.lua`.

El flujo seguido fue el clásico con Docker:

```bash
# 1. Extracción (perfil car)
docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/clm.osm.pbf

# 2. Particionado (MLD)
docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend osrm-partition /data/clm.osrm

# 3. Customización de pesos
docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend osrm-customize /data/clm.osrm

# 4. Servidor OSRM local
docker run -t --name osrm-car-clm -p 5000:5000 -v "${PWD}:/data" osrm/osrm-backend osrm-routed --algorithm mld /data/clm.osrm
```

Con esto, la PoC utiliza ahora una **estrategia híbrida**:

- `driving` → OSRM local (Castilla-La Mancha) en `http://127.0.0.1:5000`.
- `cycling` y `foot` → `https://routing.openstreetmap.de/routed-bike` y `.../routed-foot` respectivamente.

Esta combinación mantiene:

- control total sobre coche (modo central en muchos escenarios de movilidad),
- y cobertura amplia para bici y a pie sin necesidad de montar más contenedores.

A nivel de código, estas decisiones están encapsuladas en `app/services/osrm_client.py`, donde se define un diccionario `OSRM_BASE_URLS` por perfil. Cambiar de estrategia (por ejemplo, montar también bici y pie en local o volver temporalmente al servicio remoto) se reduce a modificar esas URLs base.

### 2.4. Consideraciones éticas y de buen uso

`routing.openstreetmap.de` es una infraestructura comunitaria mantenida por FOSSGIS. En este TFM:

- el uso es moderado y de carácter académico;
- se evita lanzar experimentos masivos que pudieran sobrecargar el servicio;
- el modo que previsiblemente generará más tráfico (coche) se ha migrado a una instancia local propia;
- en caso de necesitar un volumen mayor para bici y pie, se valorará montar instancias OSRM específicas o usar otras soluciones dedicadas.

Este enfoque respeta el espíritu colaborativo de la comunidad OpenStreetMap y alinea el proyecto con buenas prácticas en el uso de recursos compartidos.

---

## 3. Integración inicial con GTFS

Como primera aproximación a los datos de transporte público, el backend incluye un servicio de lectura de feeds **GTFS** (General Transit Feed Specification). En la PoC se ha utilizado un feed del **Consorcio Regional de Transportes de Madrid (CRTM)** para autobuses urbanos de la Comunidad de Madrid, aunque la lógica es reutilizable para otros feeds (por ejemplo, uno específico de Ciudad Real).

### 3.1. Colocación del feed GTFS

Se espera que el fichero ZIP GTFS esté en:

```text
backend/data/gtfs/google_transit_M9.zip
```

(con un nombre similar; se puede ajustar en `gtfs_loader.py` si es necesario).

Se recomienda añadir esta ruta al `.gitignore` para no subir el ZIP al repositorio:

```gitignore
data/gtfs/*.zip
```

### 3.2. Lectura de `stops.txt` y endpoint `/api/gtfs/stops`

El servicio `app/services/gtfs_loader.py`:

- abre el ZIP GTFS,
- localiza el fichero `stops.txt`,
- y lo parsea con la librería estándar `csv`, extrayendo por cada parada:

  - `stop_id`
  - `stop_code`
  - `stop_name`
  - `stop_desc`
  - `stop_lat`
  - `stop_lon`

Los datos se exponen a través del endpoint:

```http
GET /api/gtfs/stops?limit=500
```

Parámetros:

- `limit` (opcional, por defecto 500, máximo 5000): número máximo de paradas a devolver.

La respuesta es un JSON con una lista de objetos:

```json
[
  {
    "id": "1234",
    "code": "09568",
    "name": "ESTACIÓN-EST.ARANJUEZ",
    "desc": "Descripción opcional",
    "lat": 40.03,
    "lon": -3.61
  },
  ...
]
```

En el frontend, estos datos se consumen con React Query y se representan como `CircleMarker` de Leaflet sobre el mapa, con un `Tooltip` que muestra el nombre y código de cada parada.

Esta integración demuestra que el sistema es capaz de leer feeds GTFS reales y visualizarlos, preparando el terreno para integraciones posteriores con motores de enrutado de transporte público como OpenTripPlanner.

---

## 4. Requisitos previos

### 4.1. Backend

- **Python 3.11** (o similar) instalado y accesible en la línea de comandos.
- **Docker Desktop** para levantar la instancia OSRM local (al menos para el modo coche).

### 4.2. Frontend

- **Node.js 24.x LTS** (se ha usado la versión 24.11.x).
- `git` para clonar el repositorio.

Opcional pero recomendable:

- Navegadores: **Chrome** o **Firefox** para desarrollo y demo.
- Evitar extensiones agresivas en el navegador (ver sección de problemas conocidos).

---

## 5. Clonado del repositorio

```bash
git clone https://github.com/ivanuclm/movilidad-urbana-sim.git
cd movilidad-urbana-sim
```

---

## 6. Puesta en marcha del backend (FastAPI)

1. Ir a la carpeta del backend:

   ```bash
   cd backend
   ```

2. Crear y activar un entorno virtual (Windows PowerShell):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   En Linux/WSL:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

   (Si no existe el `requirements.txt`, se pueden instalar los paquetes básicos: `fastapi`, `uvicorn[standard]`, `httpx`, `pydantic-settings`, `python-dotenv`, etc.)

4. (**Opcional pero recomendado**) Colocar un feed GTFS en `backend/data/gtfs/` si se desea ver paradas de transporte público en el mapa (consultar sección 3).

5. Ejecutar la API con Uvicorn:

   ```bash
   uvicorn app.main:app --reload
   ```

   Por defecto, la API quedará escuchando en:

   - `http://127.0.0.1:8000`

6. Comprobar que la API responde:

   - `http://127.0.0.1:8000/health` → debería devolver `{"status":"ok"}`.
   - `http://127.0.0.1:8000/docs` → interfaz Swagger/OpenAPI para probar los endpoints `/api/osrm/routes` y `/api/gtfs/stops`.

Ejemplo de cuerpo para probar `/api/osrm/routes` en Swagger:

```json
{
  "origin": { "lat": 38.986, "lon": -3.927 },
  "destination": { "lat": 38.99, "lon": -3.92 },
  "profiles": ["driving", "cycling", "foot"]
}
```

---

## 7. Puesta en marcha de OSRM local (perfil coche)

> Si no se desea montar OSRM local todavía, se puede cambiar temporalmente el backend para que `driving` vuelva a apuntar a `https://routing.openstreetmap.de/routed-car`. Sin embargo, la configuración recomendada para el TFM es tener coche en local.

### 7.1. Descarga del extracto OSM

1. Descargar desde Geofabrik un extracto adecuado, por ejemplo **Castilla-La Mancha** desde:

   - https://download.geofabrik.de/europe/spain.html

2. Guardar el fichero `.osm.pbf`, por ejemplo:

   ```text
   F:\TFM\osrm-clm\castilla-la-mancha-251209.osm.pbf
   ```

### 7.2. Construcción del dataset OSRM con Docker

Desde la carpeta donde se encuentra el `.osm.pbf`:

```bash
cd F:\TFM\osrm-clm
```

Ejecutar, uno a uno, los siguientes comandos (ejemplo en PowerShell, adaptables a otras rutas):

```bash
# 1. Extracción
docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend   osrm-extract -p /opt/car.lua /data/castilla-la-mancha-251209.osm.pbf

# 2. Particionado
docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend   osrm-partition /data/castilla-la-mancha-251209.osrm

# 3. Customización
docker run --rm -t -v "${PWD}:/data" osrm/osrm-backend   osrm-customize /data/castilla-la-mancha-251209.osrm
```

### 7.3. Levantar el servidor OSRM

Finalmente, arrancar el servidor:

```bash
docker run -t --name osrm-car-clm -p 5000:5000 -v "${PWD}:/data" osrm/osrm-backend   osrm-routed --algorithm mld /data/castilla-la-mancha-251209.osrm
```

Con esto, OSRM quedará servido en:

- `http://127.0.0.1:5000`

El backend asume por defecto que esta URL está disponible para el perfil `driving`. Si el contenedor no está levantado, las peticiones de coche fallarán, mientras que bici y a pie seguirán funcionando (ya que usan `routing.openstreetmap.de`).

---

## 8. Puesta en marcha del frontend (Vite + React)

1. En otra terminal, ir a la carpeta del frontend:

   ```bash
   cd frontend
   ```

2. Instalar dependencias de Node:

   ```bash
   npm install
   ```

3. Lanzar el servidor de desarrollo de Vite:

   ```bash
   npm run dev
   ```

   Vite mostrará algo como:

   ```text
   VITE v7.x.x  ready in XXX ms

     ➜  Local:   http://localhost:5173/
   ```

4. Abrir el navegador en:

   - `http://localhost:5173/`

Deberías ver el **Simulador de movilidad urbana (PoC)** con:

- mapa de OpenStreetMap,
- marcadores de origen (pin verde ▶) y destino (pin rojo ■),
- botones `Coche`, `Bici`, `A pie`,
- botón “Calcular rutas OSRM”,
- tabla con las métricas por modo,
- y, si el backend GTFS está configurado, paradas de transporte público representadas sobre el mapa.

---

## 9. Flujo de uso de la demo

1. Haz clic en el mapa:
   - primer clic → mueve el **origen**,
   - segundo clic → mueve el **destino**,
   - siguientes clics → alternan origen/destino.
2. Pulsa **“Calcular rutas OSRM”**:
   - el frontend llama al backend,
   - FastAPI consulta:
     - OSRM local (Castilla-La Mancha) para coche,
     - `routing.openstreetmap.de` para bici y a pie,
   - se pinta la ruta de coche por defecto.
3. Cambia de modo usando los botones:
   - **Coche**, **Bici**, **A pie**,
   - el mapa actualiza la polilínea y la tabla resalta la fila del modo escogido.
4. Activa o desactiva la visualización de paradas GTFS si la interfaz lo permite, para ver la red de transporte público sobre el mapa.

---

## 10. Problemas conocidos (navegadores y extensiones)

Durante el desarrollo se detectó un problema concreto usando **Microsoft Edge**:

- En algunas configuraciones, la página aparecía completamente en blanco.
- En la consola del navegador se veían errores como:
  - `Failed to load module script: Expected a JavaScript-or-Wasm module script but the server responded with a MIME type of "text/html".`
  - `Uncaught SyntaxError: Unexpected token '<' (at main.tsx:...)`.
- Estos errores estaban relacionados con extensiones y componentes de Edge que inyectan scripts (por ejemplo, el sistema de seguimiento de precios, “shopping”, etc.).

En cambio, el mismo proyecto funcionaba sin problemas en **Google Chrome**.

### Recomendaciones

Si al arrancar el frontend:

- la página se muestra en blanco;
- no aparecen ni el contenido de la plantilla de Vite (logos de Vite/React) ni el mapa;

entonces:

1. Prueba a abrir la aplicación en **otro navegador** (Chrome o Firefox).
2. O abre una ventana en modo **Incógnito / InPrivate**, donde no se cargan las extensiones.
3. Si usas Edge, desactiva temporalmente extensiones relacionadas con “shopping”, “price tracking” o similares.

Para la defensa del TFM se recomienda utilizar un navegador limpio (sin extensiones que modifiquen páginas) para evitar interferencias en la demo.

---

## 11. Próximos pasos

Esta PoC deja preparados:

- El backend de rutas (OSRM) listo para ser usado como **fuente de variables de trayecto**.
- El backend de transporte público con capacidad para leer feeds GTFS reales y exponer paradas.
- El frontend con:
  - selección interactiva origen–destino,
  - visualización de rutas por perfil,
  - incorporación de capas de transporte público,
  - y un layout tipo panel muy adecuado para añadir el **perfil del viajero** y el **modelo de elección modal**.

Los siguientes desarrollos previstos para el TFM son:

1. Integrar el dataset **LPMC (London Passenger Mode Choice)** y los modelos de Machine Learning proporcionados por el director.
2. Añadir al frontend un formulario de **perfil de viajero** y controles de políticas (coste del coche, tarifas, frecuencia de bus, etc.).
3. Conectar ambos mundos mediante un nuevo endpoint de predicción, combinando:
   - variables del usuario,
   - variables del trayecto derivadas de OSRM,
   - y parámetros de escenario.
4. Extender el simulador con métricas agregadas, gráficos y, en su momento, integración con datos GTFS y OTP para rutas de transporte público.

Con estos pasos, la base técnica que proporciona este repositorio se convertirá en el núcleo del simulador de movilidad urbana que se presentará en la defensa del TFM.
