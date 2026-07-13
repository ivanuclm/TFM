# Guion de defensa v2 — TFM Simulador de Movilidad Urbana

> Incorpora el feedback del tutor tras el primer ensayo (que se fue a **26:40**).
> **El recorte gordo es la DEMO: de 11 min a 4-5 min.** El resto del ritmo estaba bien.

## Mecánica de diapositivas (aplicar en todas)
- **Número de diapositiva** sutil abajo a la derecha (gris, pequeño).
- **Portadillas de capítulo** (5 s cada una): Estado del arte, Metodología, Arquitectura, Resultados. Solo el título grande centrado.
- **Objetivos** en "cajitas" (una por objetivo), no como lista de viñetas.
- **Arquitectura**: quitar el título "Arquitectura del sistema" de arriba (ya lo dice la portadilla) y **centrar el esquema**.
- **DEMO**: solo la palabra "DEMO". Sin enlace a vídeo (el vídeo lo pones tú; mejor en vivo).
- Tras "Gracias", **duplicar la diapositiva de inicio** al final para dejarla de fondo durante las preguntas.
- **Diapositivas de reserva ocultas** al final (tras la portada duplicada): diagramas de detalle por si sobra tiempo o en preguntas. Botón derecho → Ocultar diapositiva.

## Timeline objetivo (~20:00)

| Bloque | Dur. | Fin acumulado |
|---|---|---|
| Portada + Introducción | 1:25 | 1:25 |
| Objetivos | 1:00 | 2:25 |
| *(portadilla)* Estado del arte + datos + elección modal | 2:05 | 4:30 |
| *(portadilla)* Metodología | 1:10 | 5:40 |
| *(portadilla)* Arquitectura | 1:30 | 7:10 |
| *(portadilla)* Resultados (OSRM · OTP · GTFS · LPMC) | 6:50 | 14:00 |
| **DEMO** | 4:00 | 18:00 |
| Conclusiones | 1:00 | 19:00 |
| Trabajo futuro | 1:00 | 20:00 |

Regla de oro del tutor: *"estás tan contento con tu criatura que te olvidas del tiempo"*. Cronómetro visible y disciplina en la demo.

---

## 1 · Portada (0:10)
Buenos días. Soy Iván Hernández y presento mi TFM, "Simulador web de escenarios de movilidad urbana mediante técnicas de IA", dirigido por José Ángel Martín Baos.

## 2 · Introducción — imagen a tamaño completo (1:15)
*(Imagen de atasco a sangre completa, sin título.)*
La movilidad urbana está en plena transformación. El tráfico rodado concentra buena parte de las emisiones y la contaminación urbana, y las administraciones han pasado de recomendar a **obligar**: la Ley 7/2021 impone Zonas de Bajas Emisiones. Peatonalizar, ampliar una ZBE o cambiar frecuencias y tarifas son decisiones caras y difíciles de revertir. La pregunta es: ¿cuántos dejarían el coche si el bus fuera más barato o más frecuente? En el fondo, lo que construimos es un **gemelo digital del comportamiento de los viajeros**: una réplica sobre la que ensayar políticas y anticipar el reparto modal antes de aplicarlas en la ciudad real.

## 3 · Objetivos (1:00) — en cajitas
Objetivo general: un prototipo de simulador web que integra ML y enrutado para analizar el impacto de las políticas en el reparto modal. Cuatro cajitas: **(1)** modelos de elección modal; **(2)** enrutado OSRM y OTP; **(3)** app web interactiva; **(4)** escenarios what-if. Los iré tocando todos.

## — Portadilla: ESTADO DEL ARTE (0:05)
*(Título grande. "Vamos a situar los antecedentes.")*

## 4 · Datos abiertos y enrutado (1:15)
*(diag_datos_enrutado.png)*
Todo se apoya en datos abiertos: OpenStreetMap para la red viaria y GTFS para el transporte público. Sobre ellos, dos motores complementarios: OSRM (rutas viarias, muy rápido) y OpenTripPlanner (multimodal). La salida son las **variables de viaje** (tiempo, distancia, transbordos, coste) que alimentan al modelo.

## 5 · Elección modal (1:15) — OJO al matiz de racionalidad
*(diag_rum.png)*
La elección de modo se modela con teoría de utilidad aleatoria: cada viajero asigna una utilidad a cada modo (U = V observable + ε aleatorio) y elige la mayor. **Los decisores SÍ son racionales** (si no, se cae todo el marco de utilidad). Lo que ocurre es que hay **variables latentes**, no observables o no recogidas en la encuesta: un coche viejo, no tener cochera, una mala experiencia pasada que le marcó. Esa parte de la decisión no está en los datos. El ML estima estas probabilidades mejor que los modelos clásicos, y es el fundamento de nuestro módulo de IA.

## — Portadilla: METODOLOGÍA (0:05)

## 6 · Metodología (1:05)
*(sprints_timeline_pres.png — S14 renombrado "Revisión y cierre")*
Scrum adaptado a una persona: el tutor como Product Owner, yo como Scrum Master y Developer. 14 sprints de diciembre a julio. En el Gantt se ve el **solapamiento** entre la línea de infraestructura y la de IA: se avanzó en paralelo.

## — Portadilla: ARQUITECTURA (0:05)

## 7 · Arquitectura (1:25) — dedicarle un pelín más
*(Esquema de arquitectura centrado, sin título encima.)*
Visión global. Regla de oro: el frontend **nunca** habla directamente con OSRM ni OTP; todo pasa por una API propia en FastAPI con cuatro routers (osrm, otp, gtfs, lpmc). Frontend React + Leaflet. Todo orquestado con Docker Compose, reproducible en un comando. Me detengo un momento en cómo fluye una consulta: el usuario marca origen y destino, el backend pide rutas a los motores, deriva las variables de viaje y se las pasa al modelo, que devuelve las probabilidades por modo. Ahora entramos en cada pieza.

## — Portadilla: RESULTADOS (0:05)

## 8 · OSRM (1:00)
*(RutasOSRM.png)*
Enrutado viario con OSRM local y **tres perfiles** (coche, bici, a pie), cada uno en su contenedor, bajo `/api/osrm`. Aquí, las tres rutas del mismo origen-destino sobre el mapa: cada modo elige su trazado.

## 9 · OTP (1:00)
*(Captura del panel Rutas con itinerario de bus.)*
Transporte público con OpenTripPlanner sobre el GTFS de Toledo, bajo `/api/otp`. Calcula itinerarios puerta a puerta combinando tramos a pie y en autobús, con horarios reales.

## 10 · GTFS: cruce de ficheros (1:00) — explicar un poco mejor (+20 s)
*(diag/cruce GTFS.)*
El GTFS son varios ficheros que hay que cruzar por sus claves. Para saber **qué líneas pasan por una parada** encadeno stops → stop_times → trips → routes (por stop_id, trip_id, route_id). Para el **horario de una ruta en una fecha** añado el filtro de calendar_dates por service_id. Sobre esto se construye el panel de red, bajo `/api/gtfs`.

## 11 · LPMC: datos y entrenamiento (1:15) — bloques que van apareciendo
*(Pipeline LPMC; anima cada bloque al hablar: dataset → features → validación → modelo.)*
El modelo se entrena con el dataset LPMC. Las entradas son de **ruta** (OSRM/OTP) y **sociodemográficas** (edad, carnet, coches, motivo, coste). Detalle clave: **GroupKFold por hogar**, para que viajes del mismo hogar no caigan a la vez en train y test. Y un bug que corregí: las duraciones venían en segundos y el dataset las usa en horas.

## 12 · LPMC: tres modelos y resultados (1:15) — cierre del matiz de racionalidad
*(_borrador_dnn.png + tabla de métricas.)*
Comparé tres modelos sobre las mismas variables: XGBoost, Random Forest y una red neuronal en PyTorch. **XGBoost es el mejor** y es el modelo por defecto. Accuracy y GMPCA no son altísimos, y esto es esperable por dos motivos: primero, las **variables latentes** que mencioné, que influyen en la decisión y no están en la encuesta; segundo, los modelos de ML **extrapolan mal** fuera del dominio con el que se entrenaron. No es que el modelo sea malo: parte de la decisión, sencillamente, no es observable.

## 13 · Ajustes de conocimiento experto (0:55)
*(diag_ajustes.png)*
Un modelo "a secas" no basta: inyecto conocimiento del dominio. Cuando OTP no da un bus real, penalizo las variables de transporte público (μ+5σ) para que el modelo descarte el bus por sí mismo; un recargo al coche en trayectos muy cortos; y una limitación fuera del rango de los datos. Esto diferencia el simulador de un simple `.fit()`.

## 14 · La interfaz (0:20) — rápido y a la demo
*(FRONTEND_VistaGeneral.jpeg)*
Todo se controla desde aquí: rail lateral con Rutas, Red, Predicción IA y Ajustes, sobre el mapa de Toledo. Y lo mejor es verlo:

## 15 · DEMO (4:00) — Steve Jobs: parece improvisado, está todo ensayado
Guion cerrado, cronometrado. **Menos detalle en rutas/GTFS (ya conocen Google Maps), MÁS tiempo en inferencia, que es lo novedoso.**

- **(0:40) Rutas.** Origen-destino de un commuter en Toledo → se ven los 4 modos con sus colores. Comenta rápido que el peatón atraviesa zonas que el coche no. No te detengas.
- **(0:30) Bus.** Enseña un itinerario de bus (líneas, paradas). Que se vea, sin pararte en tiempos de parada ni detalles.
- **(2:00) Inferencia — el plato fuerte.** Preset **Commuter** → inferir. Luego el mismo con y **sin coche** → se ve cómo cambia la probabilidad. Repite con preset **Estudiante**. Ese contraste (con/sin coche) es el mensaje. No te enredes explicando cada parámetro.
- **(0:30) Capas y ajustes.** En 20 s: cambia el mapa base para que se vea que funciona, menciona ajustes, y cierras. **Nada de cambiar fechas.**

Antes de empezar: `docker compose up` caliente. Ten un **vídeo de respaldo** a mano (lo grabas tú cuando lo tengas muy ensayado).

## 16 · Conclusiones (1:00)
*(4 iconos, uno por objetivo.)*
Objetivos cumplidos, prototipo funcional de extremo a extremo: modelos de elección modal entrenados y validados; enrutado OSRM+OTP con datos reales de Toledo; app web interactiva; y escenarios what-if que muestran el cambio en el reparto modal. En una frase: un gemelo digital para anticipar el efecto de una política antes de aplicarla.

## 17 · Trabajo futuro (1:00)
*(4 iconos.)*
Estimación de emisiones de CO₂; extender a más ciudades; calibrar con datos locales de Toledo (el LPMC es de Londres); y despliegue en la nube. Muchas gracias.

## 18 · Gracias (preguntas)
Gracias por su atención, quedo a su disposición.

## 19 · Portada duplicada (fondo durante preguntas)

---

## Diapositivas de reserva OCULTAS (tras la 19)
Para preguntas o si sobra tiempo. Marcar como ocultas.
- Pipeline LPMC en detalle (features completas / tab:lpmc_features).
- Cruce de ficheros GTFS en detalle.
- Arquitectura de la DNN (torchview).
- Tabla de métricas por modelo (train/test).
- Documentación OpenAPI (`/docs`).
