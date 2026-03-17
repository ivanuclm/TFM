# Memoria técnica del simulador de movilidad urbana (PoC TFM)

Esta memoria recoge la evolución de la **prueba de concepto** del TFM, las decisiones de diseño tomadas y los principales hitos técnicos alcanzados. Sirve como documentación viva para el profesor y como referencia para futuros desarrollos.

---

## 1. Objetivo de la prueba de concepto

El objetivo general del TFM es desarrollar un **simulador web de movilidad urbana** para la ciudad de Toledo que integre:

- Servicios de enrutado sobre red viaria y transporte público (OSRM y OTP).
- Un modelo de **elección modal** basado en Machine Learning (dataset LPMC).
- Una interfaz web interactiva que permita explorar escenarios de viaje y analizar resultados.

La PoC se ha centrado en construir una arquitectura funcional **backend + frontend** capaz de:

1. Consultar OSRM en local para obtener rutas y métricas por modo (coche, bici, a pie).
2. Consultar OTP en local para obtener itinerarios de transporte público usando el GTFS urbano de Toledo.
3. Unificar ambos servicios bajo una API propia FastAPI.
4. Mostrar los resultados en un mapa interactivo, con información de distancias, tiempos y detalles de los tramos.

Paralelamente, se ha preparado una pipeline independiente para el dataset **LPMC** replicando el preprocesado del profesor y entrenando un modelo base con XGBoost.

---

## 2. Primeras decisiones sobre enrutado con OSRM

### 2.1. Problema del demoserver oficial

Inicialmente se probó el **demoserver oficial de OSRM**:

- `https://router.project-osrm.org/route/v1/{profile}/...`

Sin embargo, este servicio presenta varias limitaciones para un TFM que puede requerir muchas consultas:

- Límites de uso y políticas de fair-use.
- Disponibilidad no garantizada.
- Imposibilidad de modificar perfiles de enrutado o parámetros internos.

Por ello se decidió montar una instancia propia en local usando **Docker**.

### 2.2. Montaje de OSRM local

Se descargó el fichero `clm.osm.pbf` (Castilla-La Mancha) desde Geofabrik y se creó un directorio específico `TFM/osrm`. A partir de ahí se siguieron los pasos estándar de OSRM:

1. `osrm-extract` con el perfil de coche (`car.lua`).
2. `osrm-partition` y `osrm-customize` para preparar el grafo.
3. `osrm-routed` para levantar el servidor.

Legalmente se decidió exponer **tres perfiles**:

- Coche: puerto `5000`.
- Bici: puerto `5001`.
- A pie: puerto `5002`.

En la PoC se reutiliza el mismo `.osrm` pero variando el perfil lógico (`car`, `bike`, `foot`) en cada servidor. Esto permite tener tiempos coherentes por modo sin necesidad de múltiples `.osrm` pesados.

### 2.3. Capa intermedia en FastAPI

Para desacoplar el frontend de OSRM se creó un endpoint:

```python
# /api/osrm/routes  (routes_osrm.py)

class Point(BaseModel):
    lat: float
    lon: float

class RouteResult(BaseModel):
    profile: str          # driving / cycling / foot
    distance_m: float
    duration_s: float
    geometry: list[Point]

class RouteResponse(BaseModel):
    origin: Point
    destination: Point
    results: list[RouteResult]
```

El endpoint recibe:

```json
{
  "origin": { "lat": ..., "lon": ... },
  "destination": { "lat": ..., "lon": ... },
  "profiles": ["driving", "cycling", "foot"]
}
```

Y devuelve, para cada perfil, la distancia, duración y geometría de la ruta. Internamente:

- Construye la URL según el puerto de cada perfil.
- Llama a OSRM (`/route/v1/{profile}/{lon_o},{lat_o};{lon_d},{lat_d}`).
- Decodifica la polyline de OSRM a una lista de puntos lat/lon.

Esta API se pensó desde el inicio para ser estable y reutilizable por el modelo LPMC en una fase posterior.

---

## 3. Interfaz web inicial con Leaflet

### 3.1. Setup del frontend

Se creó una aplicación React con Vite, TypeScript y Tailwind CSS (estilos personalizados). El componente principal:

- `App.tsx` – orquesta el estado global (origen, destino, modo seleccionado, resultados de la API).
- `MapView.tsx` – encapsula el mapa Leaflet y la interacción de clic en el mapa.

### 3.2. Interacción básica

Comportamiento definido:

1. Al hacer clic en el mapa se alterna entre fijar **origen** y **destino**.
2. El botón **"Calcular rutas"** llama al endpoint `/api/osrm/routes` con los tres perfiles.
3. Se muestran en una tabla las distancias y duraciones para coche, bici y a pie.
4. Un conjunto de botones (“Coche”, “Bici”, “A pie”) permite seleccionar qué geometría se pinta en el mapa.

La ruta seleccionada se muestra con una `Polyline` de Leaflet sobre el mapa base de OpenStreetMap.

### 3.3. Decisiones de UX

- Se optó por marcadores personalizados SVG para origen (verde con flecha) y destino (rojo con cuadrado).
- La ruta activa resalta en azul sobre el mapa.
- La tabla y los botones se agruparon en una tarjeta lateral, mejorando la legibilidad.

En este punto la PoC ya disponía de un flujo completo **frontend → API propia → OSRM**.

---

## 4. Integración del transporte público con OTP y GTFS de Toledo

El siguiente gran bloque fue añadir **transporte público** real usando el GTFS urbano de Toledo y **OpenTripPlanner (OTP)**.

### 4.1. Construcción del grafo OTP

Se creó un directorio `TFM/otp-toledo` con:

- `clm.osm.pbf` – mismo fichero que para OSRM.
- `GTFS_Urbano_Toledo.zip` – feed GTFS de la red urbana de autobuses de Toledo.

Con la imagen oficial de `opentripplanner/opentripplanner:2.5.0` se ejecutó:

```bash
docker run --rm \
  -v "${PWD}:/var/opentripplanner" \
  opentripplanner/opentripplanner:2.5.0 \
  --build --save
```

OTP detectó automáticamente el PBF y el GTFS, construyó el grafo y generó `graph.obj`. Finalmente se levantó el servidor:

```bash
docker run --rm \
  -v "${PWD}:/var/opentripplanner" \
  -p 8080:8080 \
  opentripplanner/opentripplanner:2.5.0 \
  --load --serve
```

La **Debug UI** (`http://localhost:8080`) permitió verificar que:

- El grafo se cargaba correctamente.
- Existían itinerarios que mezclaban tramo a pie + bus para los pares origen/destino usados en el simulador.

### 4.2. Endpoint `/api/otp/routes`

Se diseñó un endpoint análogo al de OSRM, pero centrado en un único modo “transit”:

```python
class OtpRouteRequest(BaseModel):
    origin: Point
    destination: Point
    itinerary_index: int | None = None
```

La lógica principal:

1. Construye los parámetros OTP (`fromPlace`, `toPlace`, `date`, `time`, `mode=TRANSIT,WALK`, etc.).
2. Llama a `http://localhost:8080/otp/routers/default/plan` con `numItineraries=5`.
3. Ordena los itinerarios por duración total.
4. Selecciona el itinerario:
   - Si se ha pasado `itinerary_index`, usa ese.
   - En caso contrario, escoge el primero que tenga **al menos un leg de transporte público** (bus), con `_pick_itinerary_with_transit`.
5. Construye:
   - `segments`: un array de segmentos por leg.
   - `geometry`: concatenación de todas las geometrías de los legs.

```python
class TransitSegment(BaseModel):
    mode: str
    distance_m: float
    duration_s: float
    geometry: list[Point]
    route_id: str | None = None
    route_short_name: str | None = None
    route_long_name: str | None = None
    agency_name: str | None = None
    from_stop_name: str | None = None
    to_stop_name: str | None = None
    departure: str | None = None
    arrival: str | None = None
```

Se extraen, cuando están presentes en OTP, los metadatos de cada leg:

- Nombre corto y largo de la línea.
- Agencia.
- Parada de origen y destino.
- Hora de salida y llegada (convertidas a HH:MM).

El resultado final (`TransitResult`) incluye además `itinerary_index` y `total_itineraries`, lo que permite paginar desde el frontend.

### 4.3. Visualización diferenciada de tramos (a pie vs bus)

En `MapView.tsx` se añadió soporte para recibir `otpSegments` y pintar cada uno:

- Tramos `mode === "WALK"`:
  - Línea gris discontinua (`dashArray: "6 6"`).
- Tramos de bus (`mode === "BUS"` y otros modos de tránsito):
  - Línea naranja continua, algo más gruesa.

Esto aporta una visualización rica de la ruta de transporte público:

- Se ve claramente por dónde se camina hasta la parada, entre intercambios, y desde la parada final.
- Se distingue visualmente el tramo de autobús.

### 4.4. Paginador de itinerarios OTP

Como OTP puede devolver múltiples itinerarios válidos, se implementó un **paginador** en el panel lateral:

```tsx
const [transitItineraryIndex, setTransitItineraryIndex] = useState(0);

<button onClick={() => { /* itinerario anterior */ }}>◀ Anterior</button>
<span>Itinerario {transitItineraryIndex + 1} de {totalItineraries}</span>
<button onClick={() => { /* itinerario siguiente */ }}>Siguiente ▶</button>
```

Cada cambio de página:

- Actualiza `transitItineraryIndex`.
- Llama de nuevo a `/api/otp/routes` con el nuevo índice.
- Redibuja la ruta y los segmentos.

Se decidió ordenar siempre los itinerarios por **duración total** de menor a mayor, de modo que el itinerario 1 suele ser el más rápido.

---

## 5. Integración de GTFS Toledo para exploración de red

Además del planificador OTP, se añadieron endpoints específicos para explorar información GTFS directamente desde el backend:

- `GET /api/gtfs/stops?limit=5000`
- `GET /api/gtfs/routes`
- `GET /api/gtfs/routes/{route_id}`
- `GET /api/gtfs/routes/{route_id}/schedule?date=YYYY-MM-DD`

### 5.1. Carga y modelado GTFS

Se utiliza `pandas` para leer los ficheros GTFS (`stops.txt`, `routes.txt`, `trips.txt`, `stop_times.txt`, etc.) y se construyen vistas adaptadas a la aplicación:

- Paradas con sus coordenadas y las rutas que pasan por cada una.
- Lista de rutas con `short_name`, `long_name`, color y agencia.
- Secuencia ordenada de paradas y shape de cada ruta (para pintarla en el mapa).
- Horarios agregados por dirección:

```json
{
  "route_id": "30011",
  "date": "2025-12-11",
  "directions": [
    {
      "direction_id": 0,
      "headsign": "Benquerencia",
      "trip_count": 42,
      "first_departure": "06:05:00",
      "last_departure": "22:30:00",
      "departures": ["06:05:00", "06:20:00", ...]
    },
    ...
  ]
}
```

### 5.2. Visualización en frontend

- Todas las paradas GTFS se muestran como pequeños puntos azules.
- Al hacer clic en una parada se abre un `Popup` con:
  - Nombre y código de parada.
  - Lista de líneas que pasan por ella, cada una como un pequeño botón.
- Al pulsar un botón de línea se actualiza `selectedTransitRouteId` y se disparan los queries:
  - `/api/gtfs/routes/{route_id}` para shape y paradas.
  - `/api/gtfs/routes/{route_id}/schedule?date=...` para horarios.

La **línea seleccionada** se dibuja en el mapa en naranja, con sus paradas resaltadas. Esta funcionalidad es independiente de OTP pero complementa la visión del transporte público.

---

## 6. Evolución del estado del simulador

En resumen, el simulador ha pasado por los siguientes estados:

1. **PoC OSRM pura**:
   - Únicamente rutas coche/bici/a pie vía OSRM.
   - Sin transporte público ni GTFS.

2. **Simulador híbrido OSRM + OTP (andando)**:
   - Se integró OTP, pero las primeras consultas devolvían rutas puramente a pie, ya que OTP encontraba caminos caminando más rápidos para ciertos casos.
   - Se ajustaron parámetros (`walkReluctance`, `maxWalkDistance`) y lógica `_pick_itinerary_with_transit` para priorizar itinerarios que realmente incluyeran bus.

3. **Simulador con OTP segmentado y paginación**:
   - Se añadió la noción de **segmento** en el backend, diferenciando WALK y BUS por leg.
   - El frontend empezó a pintar tramos a pie en discontinua y tramos de bus en continuo.
   - Se introdujo el paginador de itinerarios con ordenación por duración.

4. **Integración completa de GTFS**:
   - Visualización de toda la red de paradas y líneas.
   - Selección de líneas desde mapa y desplegable.
   - Consulta de horarios por fecha y dirección.

En paralelo se desarrolló la carpeta `lpmc/` para el preprocesamiento y entrenamiento sobre el dataset de Londres.

---

## 7. Preprocesamiento y modelo LPMC

Aunque se detalla en el README, aquí se resume el razonamiento:

1. El profesor proporciona código (`0-Process-LPMC.py`) que define **qué columnas del dataset original se usan realmente**.
2. Se replicó este preprocesado en `02_preprocess.py`, respetando:
   - One-hot de `purpose`.
   - Agrupación de `fueltype` en categorías más generales (Petrol, Diesel, Hybrid, Average).
   - Conversión de `travel_mode` a 0/1/2/3 (walk, cycle, pt, drive).
   - Eliminación de columnas que no se usarán en el modelo.
   - División temporal train/test según `survey_year`.

3. Sobre ese resultado se entrenó un **XGBoost multicategoría** (`03_train_xgb_baseline.py`):
   - Escalando únicamente las variables numéricas seleccionadas.
   - Obteniendo accuracies razonables (≈ 0.83 train, ≈ 0.73 test).
   - Guardando el modelo como `.joblib` y el `StandardScaler` asociado.

4. El script `04_inspect_and_infer.py` permite:
   - Ver ejemplos con probabilidades por clase.
   - Generar una matriz de confusión y verificar que el rendimiento es coherente con el paper de referencia.

Este bloque deja preparado el terreno para integrar un endpoint de inferencia en FastAPI y conectarlo con el simulador de Toledo.

---

## 8. Plan de integración futura con Toledo

El objetivo a corto/medio plazo es:

1. **Diseñar un mapeo de variables** entre:
   - El espacio de atributos de LPMC (edad, día de la semana, tiempos y costes por modo, etc.).
   - Lo que el simulador puede observar o suponer sobre un usuario de Toledo.

2. **Crear un endpoint `/api/lpmc/predict`** que:
   - Dado un origen/destino y un conjunto de supuestos (perfil del usuario, precio del billete, coste de combustible, etc.).
   - Consulte OSRM y OTP para obtener tiempos y distancias actuales.
   - Construya el vector de entrada para el modelo XGBoost.
   - Devuelva probabilidades de elección modal.

3. **Integrar la predicción en el frontend**:
   - Mostrar las probabilidades en tiempo real al mover origen/destino.
   - Permitir comparar escenarios (mejora de frecuencias de bus, creación de carriles bici, encarecimiento del aparcamiento, etc.).

---

## 9. Conclusiones de la PoC

La prueba de concepto ha alcanzado los siguientes hitos clave:

- Arquitectura cliente-servidor robusta con **FastAPI + React**.
- Integración completa con **OSRM local** para coche, bici y a pie.
- Integración con **OTP 2.5.0** sobre grafo de Toledo (OSM + GTFS), incluyendo:
  - Segmentación de rutas por leg.
  - Paginación y ordenación de itinerarios.
  - Distinción visual de tramos a pie y en bus.
- Exploración avanzada de la red GTFS (paradas, rutas, horarios).
- Pipeline reproducible para el dataset **LPMC**, con:
  - Preprocesado alineado con el código del profesor.
  - Modelo XGBoost base entrenado y evaluado.
  - Ficheros `.joblib` listos para integrar en el backend.

A partir de aquí, el trabajo se centra en conectar ambas piezas: usar el modelo de elección modal de Londres para simular la elección de modo en Toledo, y extender el simulador con funcionalidades de análisis de escenarios y soporte a la toma de decisiones en planificación urbana.

Esta memoria se actualizará a medida que se vayan cerrando nuevos hitos del TFM.
