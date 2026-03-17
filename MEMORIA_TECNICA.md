# Memoria Tecnica del Simulador

Resumen tecnico del simulador web de movilidad urbana desarrollado como aplicacion del TFM.

## Objetivo

El sistema integra:

- un frontend React + Vite + Leaflet;
- un backend FastAPI como capa de orquestacion;
- OSRM local para coche, bici y a pie;
- OpenTripPlanner con GTFS urbano de Toledo;
- una pipeline separada para eleccion modal con LPMC y XGBoost.

El objetivo es combinar tiempos y distancias de red con un modelo de eleccion modal para estimar la preferencia entre `walk`, `cycle`, `pt` y `drive`.

## Fuentes de datos

Los datos y recursos de partida del sistema son:

- GTFS urbano de Toledo obtenido desde el NAP del Ministerio de Transportes y Movilidad Sostenible.
- Base geografica OSM de Castilla-La Mancha descargada desde Geofabrik.
- Perfiles de enrutado de OSRM tomados de la imagen oficial `osrm/osrm-backend`, concretamente `car.lua`, `bicycle.lua` y `foot.lua`.

A partir de esas fuentes se generan localmente los artefactos operativos del sistema:

- datasets `.osrm` por modo;
- `graph.obj` para OpenTripPlanner;
- GTFS extraido en el backend para consulta directa de paradas, lineas y horarios.

## Arquitectura

### Frontend

`movilidad-urbana-sim/frontend/`

Responsabilidades principales:

- seleccionar origen y destino en mapa;
- solicitar rutas OSRM y OTP al backend;
- visualizar rutas, segmentos y paradas GTFS;
- comparar tiempos y distancias por modo.

### Backend

`movilidad-urbana-sim/backend/`

Responsabilidades principales:

- exponer endpoints propios para no acoplar el frontend a OSRM y OTP;
- consultar tres instancias OSRM independientes;
- consultar OTP para transporte publico;
- cargar y servir informacion GTFS de Toledo.

Endpoints relevantes:

- `POST /api/osrm/routes`
- `POST /api/otp/routes`
- `GET /api/gtfs/stops`
- `GET /api/gtfs/routes`
- `GET /api/gtfs/routes/{route_id}`
- `GET /api/gtfs/routes/{route_id}/schedule`

### Servicios externos

- OSRM coche: puerto `5000`
- OSRM bici: puerto `5001`
- OSRM pie: puerto `5002`
- OTP: puerto `8080`

## Evolucion tecnica

### Fase 1: OSRM

Se construyo primero el bloque de rutas por carretera y modos no motorizados:

- usando el extracto de Castilla-La Mancha de Geofabrik como base OSM;
- aplicando los perfiles `car.lua`, `bicycle.lua` y `foot.lua` de OSRM;
- calculo de rutas locales con OSRM;
- endpoint unificado en FastAPI;
- visualizacion en Leaflet de origen, destino y geometria seleccionada.

### Fase 2: OTP

Se incorporo OpenTripPlanner con OSM + GTFS de Toledo:

- utilizando el mismo extracto OSM de Castilla-La Mancha y el GTFS urbano de Toledo descargado del NAP;
- construccion de `graph.obj`;
- consulta del endpoint `plan`;
- seleccion del mejor itinerario de transporte publico;
- paginacion entre itinerarios.

### Fase 3: Segmentacion y GTFS

Se enriquecio el simulador con:

- segmentos por leg para distinguir `WALK` y `BUS`;
- visualizacion diferenciada en el mapa;
- consulta de paradas, lineas y horarios GTFS;
- exploracion de la red de bus urbano desde la interfaz.

### Fase 4: LPMC

En `lpmc/` se dejo preparada una pipeline reproducible:

- exploracion del dataset original;
- preprocesado alineado con el material del profesor;
- entrenamiento de un baseline XGBoost multiclase;
- guardado de modelo y `scaler` con `joblib`.

## Estado actual

El simulador ya funciona como aplicacion integrada del TFM:

- compara tiempos y distancias por modo;
- consulta transporte publico real con OTP;
- explora lineas y horarios GTFS;
- deja preparado el siguiente paso: integrar inferencia de eleccion modal.

## Siguiente integracion natural

1. definir el mapeo entre variables LPMC y el escenario de Toledo;
2. crear un endpoint `/api/lpmc/predict` en FastAPI;
3. obtener tiempos y distancias actuales desde OSRM/OTP;
4. construir el vector de entrada del modelo;
5. mostrar probabilidades de eleccion modal en el frontend.

## Criterio de mantenimiento

Esta memoria tecnica es un resumen operativo del estado del simulador.

La memoria academica extensa del TFM sigue en `latex/`.
