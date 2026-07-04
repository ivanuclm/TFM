Acabo de revisar los capitulos 3, 4 y 5 tras los últimos cambios aplicados.

Te apunto aquí todos los comentarios que he ido apuntando y cambios que hay que realizar.

Empiezo por los ch4.tex y ch5.tex por si hay que hacer cambios estructurales y porque son mas o menos dependientes. El ch3.tex lo vemos luego tranquilamente. También te iré comentando cosas que me dejo pendientes como TODO para mi, y preguntas que me surgen tras leerlo para que revisemos o me des la respuesta y decido.

---

PETICIONES GENERALES

- Reducir el uso de "Lo que", "ya que", "lo que garantiza", "Lo que compromete"...
- Reducir el uso de ":", que es abusivo
- Revisar el uso de ";"
- Revisar que no nos pasemos con algunas enumeraciones
- Revisar que utilizamos una nomenclatura coherente y consistente a lo largo de todo el capítulo para referirnos a las líneas de bus, rutas, trayectos, etc. Buscar algo que funcione bien. Consulta conmigo antes de hacerlo.
- Usar "utilizado" en vez de "empleado" en todas sus formas verbales
- El verbo "garantizar" se usa demasiado
- En general reducir latinoamericanismos, es una tesis en castellano (Español de España)
- La palabra "variante" no sé si es la más correcta para referirnos a los distintos modelos que utilizamos. No lo veo como variantes de un modelo, lo veo como 3 modelos distintos. Cuidado con eso
- Diseña conmigo, hazme todas las preguntas que puedas, proponme cosas, llevemoslo al nivel académico.
- En general revisar que repetimos lo minimo posible entre ch4 y ch5. La idea es que ch4 tenga exclusivamente los temas de arquitectura del sistema y ch5 toda la implementación, decisiones, morralla... Si aún así hay que repetir cosas, estaría bien que en ch4 se presenten y en ch5 se desarrollen, (o si son cosas más de arquitectura, pues solo en ch4 y así podemos referenciarlo libremente en ch5).
- Si lo necesitas, consulta las figuras que ya estamos usando para analizarlas, aunque hay alguna desactualizada como la de OTP
- Revisar que no utilizamos la palabra "ensamble" "ensamble de modelos", "ensemble", "ensemble de modelos", y las formas verbales de "ensamblar", porque parece una traducción de inglés a español y no está muy aceptado por la RAE.
- Revisar que no adelantamos cosas Frontend en Backend y similares, podemos explicar la lógica pero no meternos en como se renderizan las cosas, los botones de la interfaz, etc. en partes de backend. Lo mismo para partes de Implementación en Arquitectura, etc. Y viceversa por supuesto.
- Revisar si nos falta/sobra alguna figura, tabla, lista, ecuación, algoritmo, bloque de código...
- Ten mucho cuidado, no traduzcas del inglés al español, escribe en español directamente (pudiendo utilizar algun prestamo linguistico o algun termino en ingles directamente).
- Revisar las distintas formas a las que nos referimos al Google Polyline: "Polilínea" "polyline", "trazado", etc... Ten cuidado, citalo y explicalo en el sitio correcto para no andar repitiendo, y cojamos un mismo término para todo el documento.
- Todas las veces que llamamos a una sección, figura, tabla, etc seguido del /ref{...}, el tipo de elemento tiene que ir en mayúscula: "se aborda en la Sección~\ref{subsec:impl_lpmc_entrenamiento}."; "La Figura~\ref{fig:panel_ajustes} muestra...", ya sabes, siempre la primera mayúscula para esos casos.
- Tambien cuidado con las veces que decimos "modo" a secas para "modo de transporte", (o de otra cosa). Especificar bien, que en castellano se confunde.
- Mucho cuidado a lo largo de todo el documento con el uso de "rail" "raíl" "\textit{rail}", etc. Siempre de la misma forma. Si lo usamos en inglés, con cursiva. Si es en español, quizá buscar algo alternativo? Como cinta o barra lateral o algo?
-Revisar los nombres de los paneles del "rail", ver si están bien en la memoria conforme a lo que tenemos en el código, y ver si conviene alargarlos un poco ("Rutas OSRM/OTP", "Red GTFS" o "Feed GTFS", "IA" o "LPMC" o algo así, y el resto están bien)
-Recuerda, cita primero en el texto la figura, antes de que aparezca. Toda la explicación de la figura en el texto, no en el caption. El caption corto y directo, tal y como está ahora
---

TAREAS PENDIENTES EN CÓDIGO

- Poner en el panel IA al principio los datos de viaje solo lectura.
- Revisar si lo de Path.parents es una chapuza o está bien
- Revisar si la comprobación REGEX de nombre de modelo es overkill o está bien o qué

---

ANTES DE EMPEZAR:

A continuación pongo el número de cada apartado en Markdown utilizando "#" para el nivel junto a su título.
Voy a ir pegando aquí bloques de código LaTeX entre comillas ("así") y a continuación haré comentarios sobre ese bloque con líneas que empezarán por ">". Esos son los comentarios del autor para reestructurar y arreglar toda la memoria e ir terminando ya.

Todos los bloques que empiecen por ">" se referirán siempre al bloque de texto copiado y pegado "entrecomillado" que tengan encima (o el más próximo, si justo encima tienen otro bloque de comentario ">"). Se entiende?

El objetivo es terminar todos los capítulos de la memoria, actualmente priorizando ch4 y ch5 y anexos. Posteriormente, haré un repaso al ch3, luego conclusiones y trabajo futuro etc en ch6, y lo que falta de introducción en ch1, resumen y abstract, y poco más. La idea es que el documento tenga una estructura final ordenada, con sentido, sin saltos raros y evitando repeticiones, acotando cada sección a su contexto (arquitectura, desarrollo, etc.) y haciendo los cambios que sean necesarios en la forma que tenemos los apartados, etc. para que la lectura tenga sentido y no nos dejemos nada. Ya cuando tengamos todo veo el límite de páginas y recorto si hace falta, pero actualmente lo que necesitamos es plasmar todo el contenido de manera ordenada y sin líos ni repeticiones ni saltos ni lenguaje inconsistente, todo en castellano (Español de España), concretamente castellano-manchego para que sea un español más del centro, más general, menos latinoamericanismos ni traducciones del inglés, siguiendo el vocabulario aprobado por la RAE, y sobretodo para un TFM de este contexto.

A lo largo del documento te hago preguntas, o planteo dudas, solicito sugerencias de estructura. Atiende todas mis dudas, preguntame todo lo que indique pregunta, ofreceme ejemplos, sugerencias, y sobretodo lo que tú recomiendas. No tienes límite de tiempo. Si se agota el límite de uso de Claude no pasa nada, te reactivaré cuando vuelva a tener tokens o generaré una nueva sesión desde cero.

No te preocupes por el tamaño final del TFM, o las páginas resultantes tras nuestros cambios, mejor que sobre que no que falte, así recorto.

# CAPÍTULO 4

---

## 4.1 VISIÓN GENERAL
"\begin{figure}[htbp]
  \centering
  % \includegraphics[width=0.92\textwidth]{figures/arch_general.pdf}
  \includegraphics[width=\textwidth]{figs/ARQUITECTURA_pytorch_final.pdf}
  \caption{Arquitectura general del simulador de movilidad urbana.}
  \label{fig:arch_general}
\end{figure}"

>TODO: Actualizar este diagrama, poner mejor la foto de las paradas que devuelve el /api/GTFS y revisar si hacen falta nuevos routers o explicar mejor los contenedores o incluir alguna de las fuentes en Docker-Compose, además de poner mejor las fuentes. También, revisar si incluimos TanStack Query en el panel de Front-end, así como Lucide, buscar la imagen de React-Leaflet, etc. Revisar las lineas de comando osrm-extract y demás.

---

## 4.2 Infraestructura y orquestación

"\begin{figure}[htbp]
  \centering
  % \includegraphics[width=0.92\textwidth]{figures/arch_docker.pdf}
  \missingfigure{Diagrama de servicios Docker Compose: frontend :5173, backend :8000, osrm-car :5001, osrm-bike :5002, osrm-foot :5003, otp :8080, y servicios de inicialización gtfs-init, osrm-setup y otp-build. Volúmenes montados en OSRM y OTP.}
  \caption{Servicios Docker Compose y puertos expuestos.}
  \label{fig:arch_docker}
\end{figure}"

>TODO: Hacer este diagrama, no se si es necesario, habria que poner todos los servicios actuales y mostrar el docker-compose como esta montado y puertos expuestos, dependencias, etc. También, igual lo muevo tras el párrafo que hay justo después de la tabla, o quito la tabla en favor del diagrama o algo así aunque no me disgusta el diagrama. Recomiéndame que hacer y qué poner en cada sitio.

"La Tabla~\ref{tab:servicios_docker} resume los servicios definidos, sus puertos y su función en el sistema.

\begin{table}[htbp]
  \caption{Servicios Docker Compose del simulador.}
  \label{tab:servicios_docker}
  \centering
  \begin{tabular}{llp{7cm}}
    \hline
    \textbf{Servicio} & \textbf{Puerto} & \textbf{Función} \\
    \hline
    \texttt{frontend}   & 5173 & Interfaz web React servida por Vite. \\
    \texttt{backend}    & 8000 & API FastAPI, orquestación y lógica de negocio. \\
    \texttt{osrm-car}   & 5001 & Motor OSRM con perfil de vehículo a motor. \\
    \texttt{osrm-bike}  & 5002 & Motor OSRM con perfil de bicicleta. \\
    \texttt{osrm-foot}  & 5003 & Motor OSRM con perfil peatonal. \\
    \texttt{otp}        & 8080 & OpenTripPlanner 2.x con grafo multimodal de Toledo. \\
    \hline
  \end{tabular}
\end{table}"

>En esta tabla habría que incluir los servicios de inicialización?

"...Estos artefactos pesados se versionan mediante Git LFS (\textit{Large File Storage}), de modo que un clon del repositorio dispone de ellos sin necesidad de reconstruirlos. Para cubrir el caso de un clon sin LFS o de una actualización de los datos de origen, la orquestación incorpora además varios servicios de inicialización idempotentes que se ejecutan una sola vez antes de levantar el sistema..."

>Esta es la primera mención a Git LFS. No sé si deberíamos poner aquí la explicación detallada o en el ch5.tex; también sé que se menciona más veces máws adelante y en algunas se explica lo que es, entonces no quiero repetir cosas pero me gusta que estén explicadas desde el principio.

>Revisar que esté bien puesto lo de que se hace automático con docker compose pero todos los pasos se pueden hacer manual por si cambian las fuentes o algo (OSRM, OTP, LPMC..., cada cosa en su sitio claro, sin adelantar mucho.)

>También había pensado en poner la figura que mencionaba antes justo después de ese párrafo, donde temrina con " El procedimiento completo, tanto automático como manual, se describe en el anexo~\ref{anx:despliegue}.", no sé como lo ves, o si no es necesario figura directamente. Y en caso de si ser necesaria, que pondríamos?

---

## 4.3 Backend: capa de orquestación.

"\begin{table}[htbp]
  \caption{Endpoints principales de la API REST del backend.}
  \label{tab:endpoints_api}
  \centering
  \begin{tabular}{llp{6.5cm}}
    \hline
    \textbf{Método} & \textbf{Ruta} & \textbf{Descripción} \\
    \hline
    POST & \texttt{/api/osrm/routes}                  & Rutas viarias multimodales (OSRM). \\
    POST & \texttt{/api/otp/routes}                   & Itinerario de transporte público (OTP). \\
    GET  & \texttt{/api/gtfs/stops}                   & Listado de paradas con filtro bbox. \\
    GET  & \texttt{/api/gtfs/routes}                  & Listado de líneas de la red. \\
    GET  & \texttt{/api/gtfs/routes/\{id\}}           & Detalle de ruta: paradas y trazado. \\
    GET  & \texttt{/api/gtfs/routes/\{id\}/schedule}  & Horarios de una línea por fecha. \\
    POST & \texttt{/api/lpmc/predict}                 & Inferencia de elección modal con el modelo activo. \\
    POST & \texttt{/api/lpmc/compare}                 & Inferencia simultánea con XGBoost, RF y DNN. \\
    POST & \texttt{/api/lpmc/debug-features}          & Vector de características antes/después del escalado. \\
    GET  & \texttt{/api/lpmc/models}                  & Modelos disponibles y variante por defecto. \\
    GET  & \texttt{/health}                           & Comprobación de disponibilidad. \\
    \hline
  \end{tabular}
\end{table}"

>Revisar que la tabla esté actualizada, de nuevo estamos usando distinta nomenclatura de "línea", "ruta", etc. y además ponemos "filtro bbox" sin explicar que es boundingbox ni nada. Tambien no adelantarnos al capitulo 5.

"El router \texttt{/api/otp} consulta el planificador multimodal y gestiona la paginación de itinerarios alternativos. La respuesta incluye el desglose por tramos (\textit{legs}), con tipo de modo, geometría, parada de inicio y fin, y agencia operadora cuando el tramo es de transporte público. Los itinerarios se ordenan por duración y se selecciona automáticamente el primero que incluya al menos un tramo de transporte público; si ninguno lo incluye, se devuelve el de menor duración."

>Aquí mencionar que son hasta 5 itinerarios lo que devuelve no? Porque es como adelantarse a la paginación sin explicar que vienen varios índices.

"El router \texttt{/api/gtfs} expone información estática de la red de transporte: listado de paradas con sus líneas asociadas, listado de rutas, detalle de ruta con paradas ordenadas y trazado geométrico, y resumen de horarios por fecha. Estos datos se leen directamente del feed GTFS descomprimido en el backend, sin depender de OpenTripPlanner, lo que permite consultar la red aunque el grafo OTP no esté disponible."

>De nuevo, nomenclatura de líneas/rutas

"El router \texttt{/api/lpmc} recibe las coordenadas de origen y destino junto con el perfil sociodemográfico del viajero, construye el vector de variables de entrada al modelo consultando OSRM y OTP internamente, convierte las duraciones a horas para coincidir con las unidades del dataset de entrenamiento, aplica el escalado parcial y ejecuta la inferencia. El endpoint \texttt{/predict} usa el modelo activo; \texttt{/compare} ejecuta los tres modelos (XGBoost, Random Forest, DNN) sobre el mismo viaje y devuelve sus probabilidades comparadas; \texttt{/debug-features} expone el vector de características antes y después del escalado para validación del pipeline."

>Habría que explicar que el /compare lo hace en secuencial, por temas de CPU etc, aunque igual es adelantarse mucho. También revisar la explicación del /debug-feature que no está mal pero por si hay alguno nuevo, estar actualizados al estado real del código.

>En cualquier caso, me da un poco de miedo que estemos repitiendo con el ch5.tex, o que estemos adelantando, quizá no habría que ponerlo aqui, o al menos no haga falta volverse loco con endpoints o sí? Aunque sea explicar a que se dedica cada router sin entrar mucho en profundiad? No sé.

>También te quería preguntar si ponemos estos routers como lista o algo o de manera más estructurada.

---

## 4.4 Frontend: interfaz cartográfica


"El frontend está desarrollado con React, Vite y TypeScript. La aplicación se estructura en dos componentes principales: \texttt{App}, que concentra el estado global y la lógica de negocio del cliente, y \texttt{MapView}, que encapsula la representación cartográfica mediante React-Leaflet."

>Quizá explicar mejor React-Leaflet, que es una librería, o directamente el uso de Leaflet. También lo de Lucide-React. 

"texttt{App} gestiona los puntos de origen y destino, el modo de transporte activo, los resultados de rutas, la capa GTFS y el perfil de usuario para la inferencia. Las peticiones al backend se realizan con TanStack Query (\texttt{useQuery} y \texttt{useMutation}), que proporciona caché, gestión de estados de carga y reintento automático." 

>Tanstack Query también requeriría más presentación, no sé si aquí o más adelante en el ch5.tex

"El estado local de React es suficiente para el alcance del prototipo: no existe flujo de datos compartido entre componentes independientes que justifique una biblioteca adicional de gestión de estado."

>Esta frase no me gusta, tampoco sé si la entiendo, lo del estado local. En general igual es innecesario?

"texttt{MapView} recibe el estado relevante como \textit{props} y se encarga exclusivamente de la renderización cartográfica: marcadores de origen y destino, polilíneas de ruta coloreadas según el modo activo, paradas GTFS con popups interactivos y segmentos OTP diferenciados visualmente entre tramos a pie y tramos en vehículo."

>Lo de "props" qué se supone que es? no se explica. Tampoco me gusta lo de "según el modo activo", se puede confundir quiza, decir bien que se refiere a modo de transporte mostrado, recuerda que ahora podemos mostrar varios a la vez con el shift+click (cuidado con eso también, sin adelantar, que esté actualizado todo). Lo de "trampos a pie y tramos en vehículo" quizá decirlo mejor como de camino al bus y entre paradas de autobús. "Paradas GTFS" tambien decirlo mejor.

"Los segmentos de transporte público solo se muestran cuando el modo activo es \textit{transit}, evitando solapamientos visuales con las rutas viarias."

>lo del modo activo es transit a que te refieres? Queda un poco raro, entiendo que es cuando clicas en "Bus" para mostrar las rutas en busm, y lo de "evitando solapamientos visuales con las rutas viarias" es super innecesario, es como justificar de más algo que es sentido común, igual no hace falta ni decir esto, se sobreentiende. Ya sabes que con el ch4 tenemos que hacerlo rollo arquitectura.

"La capa de fondo es configurable entre cuatro basemaps: carto-light (analítico, sin distracciones visuales), OpenStreetMap estándar (cartografía en color), OpenTopoMap (relieve con curvas de nivel) y satélite Esri (imágenes aéreas)."

>Completamente desactualizado, ahora son 6 opciones de basemap (capas), y quizá las explicamos mejor en fuentes o algo si no hay nada a nivel arquitectonico, aunque se puede mencionar algo de que podemos cambiar los tiles como queramos o algo así. Sabes por donde voy? Tambien habria que ponerlos en lista y mejor explicados, pero eso ya en el ch5.

---

## 4.5 Pipeline de inferencia modal

"La inferencia de elección modal es la operación más compleja del sistema porque requiere coordinar tres servicios externos de forma concurrente para construir el vector de entrada al modelo. La Figura~\ref{fig:pipeline_inferencia} ilustra el flujo completo."

>Cuales son esos tres servicios externos? Es realmente la operación más compleja del sistema? También revisar si hay que actualizar algo del pipeline con los nuevos cambios.

>TODO: Revisar la figura de Pipeline de inferencia de eleccion modal, por si me faltan cambios, arreglar lo de Confidence o Probabilities (es solo Probabilities), ver si metemos mas endpoints del backend lpmc o de otra cosa que se utilice? Ver tema scaler etc que esté OK, y dejar solo la formula o la distribución.

"una a cada una de las tres instancias OSRM(conducción, bicicleta, a pie) y una a OpenTripPlanner."

>Quizá decir "y la última a OpenTripPlanner."
 
"Con los resultados se construye el vector de características de ruta, se añaden las variables sociodemográficas del perfil recibido en la petición y se ensambla el vector completo de entrada al modelo." 

>Las variables sociodemográficas del perfil recibido? igual sería más correcto decir directaente las varibales sociodemográficas recibidas en la petición o algo asi. "Ensambla" es incorrecto, usa otro termino mas aceptado por la RAE, como "construye", "monta", etc.

"Las variables continuas que presentaban distribución asimétrica en el conjunto de entrenamiento se normalizan con un escalado parcial aplicado solo a las columnas correspondientes, preservando las variables binarias y de conteo sin transformar."

>Esto es correcto? Quiero decir, está bien hacerlo así? Y lo estamos haciendo así realmente en el código?

"El modelo devuelve un vector de cuatro probabilidades correspondientes a los modos \textit{walk}, \textit{cycle}, \textit{pt} y \textit{drive}; el modo predicho es el de mayor probabilidad."

>Quiero buscar consistencia con los nombres de los modos, están bien? El pipeline devuelve las probabilidades y el modo predicho? O solo las probabilidades y nos fijamos en cual es la mejor?

"El modelo utilizado en \texttt{/predict} se elige mediante el parámetro opcional \texttt{model\_variant} de la propia petición; cuando no se indica, se recurre a la variable de entorno \texttt{LPMC\_MODEL\_VARIANT} (\texttt{xgb} por defecto), lo que mantiene la compatibilidad con clientes que no especifiquen el modelo." 

>Esto sigue siendo correcto? Podriamos mencionar tambien que es para posibilidad de añadir nuevos modelos? O poder cambiar el modelo sin necesidad de modificar mucho el código o algo así, o entrenar uno propio con las libretas de inferencia... Recomiendame.

>También, lo de "lo que mantiene la compatibilidad con clientes que no especifiquen el modelo." lo veo de nuevo innecesario, justificarse de más, no me gusta, se puede quitar.

"Ninguno de los tres modelos recibe \texttt{household\_id} como variable de entrada, ya que ese identificador de hogar no está disponible en tiempo de ejecución; su uso durante el entrenamiento se detalla en la sección~\ref{subsec:impl_lpmc_entrenamiento}."

>Esto no sé si hace falta explicarlo aquí, si lo consideras arquitectura bueno pero yo creo que es más para ch5

---

# CAPÍTULO 5

>Aquí igual tenemos que reestructurar un poco las secciones, los subsections que utilizamos, como dividimos, etc. Vamos a ello.

---

## 5.1 Infraestructura de enrutado viario: OSM

---

### 5.1.1 Origen y características del extracto OSM

"...carreteras y caminos de un territorio junto con sus atributos de velocidad, sentido y accesibilidad por modo."

>por modo de transporte mejor? NO sé

"Se utilizó el extracto de Castilla-La Mancha al ser la región en la que se enmarca el proyecto, escogiendo Toledo como caso de estudio definitivo, tal como se detalla en la sección~\ref{sec:impl_otp}. " 

>Revisar donde tiene mas sentido poner lo de donde enmarcamos el proyecto, si adelantar lo de Toledo, etc. También que Geofabrik llega hasta nivel de comunidad autonoma, no hemos descargado el mapa de solo la provincia de Toledo. No veo mal llamar a la seccion 5.2 directamente.

---

### 5.1.2 Evolución del despliegue

"\textbf{Fase 2: instancias públicas FOSSGIS.} Las instancias públicas mantenidas por FOSSGIS \cite{FOSSGISRouting} sí devuelven rutas diferenciadas por perfil mediante endpoints independientes (\texttt{/routed-car}, \texttt{/routed-bike}, \texttt{/routed-foot}), lo que permitió confirmar el funcionamiento multimodal y ajustar la integración del backend. El inconveniente es que estos servicios aplican limitaciones de uso (\textit{rate limiting}), presentan latencia variable y no permiten fijar la versión de los datos, lo que compromete la reproducibilidad."

>Cuidado con los "lo que", "lo que permitió confirmar el funcionamiento", "lo que compromete la reproducibilidad", etc. Además el funcionamiento no es "multimodal", no? O es por ser los 3 modos de transporte. Para mi multimodal es intercambiar entre varios modos de transporte, por ejemplo como hace OTP para los tramos andando/bus.


"\textbf{Fase 3: instancia local con Docker.} La solución definitiva fue desplegar OSRM localmente mediante la imagen oficial \texttt{osrm/osrm-backend} \cite{OSRMGitHub}, con un contenedor independiente por modo de transporte (conducción, bicicleta y a pie; el transporte público en autobús es responsabilidad de OpenTripPlanner). "

>Entiendo que lo de contenedores independientes es porque está requerido así por OSRM. Podemos mencionarlo? no sé si se dice más adelante o me lo dijiste tu en algun comentario...

---

### 5.1.3 Pipeline de preprocesado por perfil

"Para que OSRM pueda calcular rutas, el extracto \texttt{.osm.pbf} debe transformarse en una estructura de datos interna optimizada para ejecutar consultas y obtener el camino mínimo entre dos puntos del mapa. Este preprocesado se ejecuta una sola vez por perfil y solo hay que repetirlo si se actualiza el extracto de OSM."

>Cuidado, tengamos todo actualizado a que esto ya lo hacen solos los scripts de inicialización, aunque hay que explicarlo claro. Quizá con las modificaciones del ch4 quede más claro, pero bueno.

"Cada perfil define las reglas de movilidad del modo correspondiente: qué tipos de vía
son accesibles, a qué velocidad y con qué restricciones de giro." 

>Esos dos puntos ":" creo que son innecesarios

"Todas las etapas del preprocesado se ejecutan con esa misma imagen, lo que garantiza que el preprocesado sea reproducible en cualquier entorno de ejecución."

>De nuevo "lo que garantiza" repetido...

"\begin{enumerate}
  \item \textbf{Extracción} (\texttt{osrm-extract}): lee el \texttt{.osm.pbf} y construye el grafo viario interno aplicando las reglas del perfil Lua indicado: qué vías son transitables, a qué velocidad y con qué restricciones. El resultado es el fichero \texttt{.osrm} junto con varios auxiliares de índice."
  
>Lo de perfil Lua quizá explicar en algún sitio mejor lo que se refiere con Lua no? no se si es la priemra vez que lo ponemos, ponlo ya sea en el ch4 o aqui. También repetimos el uso de los ":", auqnue aqui no lo veo mal, pero que sea una cosa equilibrada por favor. También lo de "ficheros auxiliares de índice" igual lía, buscamos otra palabra más descriptiva o lo dejamos en auxiliares y ya.

"Las tres etapas generan los ficheros \texttt{clm.osrm} y sus auxiliares, almacenados en directorios separados por perfil (\texttt{osrm-clm/car/}, \texttt{osrm-clm/bike/}, \texttt{osrm-clm/foot/}). Por su tamaño, estos artefactos se versionan mediante Git LFS (\textit{Large File Storage}), una extensión de Git que guarda los ficheros pesados fuera del historial principal y los referencia con punteros ligeros; así un clon del repositorio dispone de los grafos sin necesidad de regenerarlos. El procedimiento completo para reproducirlos se recoge en el anexo~\ref{anx:despliegue}."

>Esta es la segunda mención a Git LFS en el documento, la primera del chapter5, donde la explicamos más a fondo. Quizá esto mejor en el ch4? ni idea.
  
"El preprocesado completo de los tres perfiles sobre el extracto de Castilla-La Mancha tarda \todo{Revisar tiempos} aproximadamente 97 segundos en la máquina de desarrollo." 

>Aqui acordarme del \todo, además habria que actualizar quiza lo que medimos porque ahora se hace automático, aunque puedo medir lo que tardo en ejecutarlo manualmente. 

>También revisar bien los tamaños ("Los artefactos generados ocupan en total unos 2,1~GB: el perfil de conducción produce 291~MB porque solo incorpora la red viaria accesible al tráfico rodado, mientras que los perfiles de bicicleta y peatonal alcanzan los 911~MB cada uno al incluir además senderos, caminos rurales y zonas de acceso restringido al tráfico.")

"\begin{figure}[htbp]
  \centering
  % \missingfigure{Diagrama del pipeline de preprocesado OSRM: \texttt{.osm.pbf} $\to$ \texttt{osrm-extract -p \{perfil\}.lua} $\to$ \texttt{osrm-partition} $\to$ \texttt{osrm-customize} $\to$ \texttt{osrm-routed -{}-algorithm mld}. Indicar que el proceso se repite de forma independiente para los tres perfiles (car, bike, foot), generando tres directorios de artefactos separados.}
  \includegraphics[width=1.0\textwidth]{figs/Pipeline_Preprocesado_OSRM.pdf}

  \caption{Pipeline de preprocesado OSRM por perfil de transporte.}
  \label{fig:osrm_pipeline}
\end{figure}"

>Esta figura creo que está bien, no se si meter algo más o alguna referencia a que docker compose lo hace ya solo pero como el diagrama es del propio pipeline da igual no?

---

### 5.1.4 Despliege y verificación

"Cada uno de los tres contenedores OSRM ejecuta el servidor de enrutado sobre su grafo preprocesado con el algoritmo MLD (Figura~\ref{fig:osrm_pipeline}):
\begin{lstlisting}[language=bash]
osrm-routed --algorithm mld /data/clm.osrm
\end{lstlisting}"

>Entiendo que aqui ya es implícito que va automático con los contenedores.

"Se evita el puerto 5000 en el anfitrión porque en macOS lo ocupa por defecto un servicio del sistema (el receptor AirPlay), lo que impediría el arranque del contenedor; esta publicación de puertos solo se usa para depuración, ya que el backend se comunica con OSRM por la red interna."

>El "ocupa por defecto" lo de ocupa suena a latinoamericano. Otra vez "lo que impepdiría el arranque del contenedor", no se si hace falta, o almenos no usemos "lo que". Tampoco se si "depuración" es el mejor término aquí, realmente sí pero vamos.

"Una respuesta válida devuelve \texttt{"code": "Ok"} junto con la distancia en metros, la duración en segundos y la geometría en formato polilínea~\cite{GooglePolyline}, una cadena de texto con la secuencia de coordenadas de la ruta, que el backend decodifica antes de enviarla al frontend."

>Este es el primer sitio donde mencionamos "polilínea"? Polyline? O lo hemos mencionado ya antes? En dicho caso, hemos expliacdo lo que es antes? O lo estamos haciedno solo aquí? Estamos repitiendo cosas con lo de antes o después? También, hay que citarlo todas las veces? Solo la primera? Falta alguna cita respecto al formato Polyline?

"Si el grafo está incompleto o el perfil es incorrecto, OSRM devuelve \texttt{"code": "NoRoute"} o una ruta degradada, detectable al comparar visualmente los tres trazados en la interfaz." 

>Lo de degradada queda raro. Entiendo que saldrían cortadas las lineas o así raras. Podemos buscar sinonimos de "degradado" aunque realmente esta bien. Un ejemplo que igual sirve de contexto (aunque no se si aqui es el mejor sitio o si siquiera hace falta ponerlo). Como el mapa es de Castilla-La Mancha, si pinchamos un par origen-destino con alguno de los dos puntos o ambos puntos fuera del extracto OSM, la ruta se calcula y dibuja solo para el tramo que incluye las carreteras de Castilla La Mancha, no llegando hasta el punto o los puntos que se encuentren fuera. No creo que sea muy relefvante pero por si viene bien para ponerlo en algun sitio, quiza en 5.1 donde hablabamos del extracto OSM? O aqui con el OSRM que es el calculo de rutas? bueno vamos viendo.


"Los tres trazados ponen de manifiesto las distintas restricciones de cada perfil sobre la red viaria de Toledo."

>Queda un poco raro lo de "ponen de manifiesto", simplemente lo que ya hemos dicho, que el peatón puede acceder a zonas restringidas, la 4ruta en bici prioriza carriles bici y calles tranquilas y la ruta en conducción utiliza las vias principales o incluso autovía para trayectos relativamente largos.

---

## 5.2 Planificación multimodal: OpenTripPlanner

---

### 5.2.1 Fuente de datos GTFS y proceso de selección

"Al enmarcarse el proyecto en Castilla-La Mancha, la búsqueda de feed GTFS de bus urbano se orientó a la región desde el principio, con la ventaja de que el extracto OSM ya estaba disponible por su uso en OSRM (sección~\ref{subsec:impl_osrm_origen}). La fuente empleada fue el Punto de Acceso Nacional de Transporte Multimodal (NAP), gestionado por el Ministerio de Transportes y Movilidad Sostenible, que centraliza feeds GTFS de operadores de toda España \cite{NAPHome}."

>Esto está repetido en subsecciones anteriores o incluso en el ch4 o es impresion mía? Organicemos bien la información y fuentes por favor.

" Aunque su cobertura a nivel nacional es amplia, la disponibilidad de feeds de transporte urbano en Castilla-La Mancha resultó muy limitada, como se detalla a continuación.


Las opciones disponibles en Castilla-La Mancha resultaron ser muy escasas." 

>Esto es mala redacción directamente, estamos repitiendo arriba y abajo. Me gusta más lo de arriba vaya, o ir directo al grano como abajo. En cualquier caso, no repetir tanto.

"El volumen del feed reveló además un problema de paginación:"

>Reveló me suena raro, aunque no está mal del todo

"Con 268 paradas, 56 rutas y 87.751 viajes que cubren unos tres meses de servicio programado, tiene un tamaño ajustado al alcance del simulador, cubre el casco urbano, el polígono industrial y las urbanizaciones periféricas, e incluye geometría de rutas para su representación cartográfica."

>Se repite el "cubre" mucho

---

### 5.2.2 Periodo de validez del feed y selección de fecha.

"Los feeds GTFS del NAP tienen un periodo de validez limitado; para el operador de Toledo (\texttt{GTFS\_Urbano\_Toledo\_2026}), los ficheros publicados cubren del 22 de febrero al 22 de mayo de 2026."

>el \texttt deberia incluir el .zip? (GTFS\_Urbano\_Toledo\_2026.zip)? Luego revisa bien lo del periodo que cubren los ficheros publicados (de nuevo, "cubren" repetido...), porque lo repetimos justo en el parrafo anterior y cada vez lo expresamos distinto. Hacerlo bien de una.

"Si la fecha de consulta cae fuera de ese rango, OTP no devuelve itinerarios de transporte público y el simulador queda sin oferta de bus sobre la que inferir."

>Más que "sin oferta de bus sobre la que inferir", que está bien, llevarlo a que el simulador lo trata como si no hubiera ningun servicio disponible y OTP no devuelve ningun trayecto en bus, solo una opción andando, (seria un pt_available=false, imagino? aunque eso es para trayectos cortos).

"Durante el desarrollo se descargaron varias versiones del feed; en las primeras el operador figuraba como ``Autobuses urbanos Toledo'' y en posteriores había pasado a denominarse UNAUTO S.L. (Grupo Ruiz), aunque el formato de los ficheros GTFS se mantuvo en todas las versiones."

>Esto realmente debería ir en periodo de validez del feed? O en una sección anterior como el 5.2.1 o algo? Aqui podriamos mencionar que el anterior era de diciembre y la version descargada mas reciente es la de febrero-mayo. Y lo de que el formato se mantuvo en todas las versiones es correcto aunque cambiase el periodo de validez y el nombre del feed para llamarse como el operador.

"El mismo feed alimenta los dos subsistemas que consumen GTFS: el grafo de OTP (sección~\ref{subsec:impl_otp_grafo}) y la capa estática de horarios (sección~\ref{sec:impl_gtfs}), de modo que ambos comparten exactamente la misma ventana de validez."

>Esto no está mal porque nos adentramos en lo de la capa estática, pero es posible que estemos repitiendo con los anteriores capitulos? Con el chapter 4 o algo? Si es necesario no pasa nada, pero iugal se puede poner de manera que no repitamos, o que lo llevemos por "como mencionamos anteriormente..."

"La fecha y la hora de consulta no se fijan en el código: se exponen mediante un control global en la interfaz, con un valor por defecto dentro del rango (\texttt{2026-05-21}, \texttt{12:00}) y acotado al intervalo válido del feed."

>Aqui a ver si podemos no usar los dos puntos ":". 


"Al ser un parámetro transversal a toda la simulación, este control único gobierna a la vez los itinerarios multimodales, los horarios de la red y el día y la hora del perfil de inferencia, evitando configuraciones contradictorias entre las distintas vistas; su ubicación y comportamiento en la interfaz se describen en la sección~\ref{subsec:impl_frontend_mapa}."

>Esto alguna cosa me suena rara, como lo de "este control único gobierna", no se si hay alguna palabra mejor que control o alguna manera de conjugar esa frase. También lo de "evitando configuraciones contradictorias entre las mismas vistas". Está bien que vayamos explicando un poco lo del input de fecha pero dejemos cosas para el frontend claro. Decir de manera simple que es universal/transversal a todos los módulos para no tener que configurar una en cada sitio (rutas OTP, horarios GTFS, variables sociodemográficas...). También hay qeu evitar el uso de ":". Además, la separación con ";" del final no la veo correcta del todo, veo mejor casi un punto, y referirnos al control. "La ubicación y el comportamiento de este input en la interfaz se describen en..." o algo así. Revisar también que la sección donde se describe está OK.

"El backend recibe la fecha y la hora en la petición y las traslada a OTP; cuando no se indican, aplica el valor por defecto."

>El ";" me queda raro, aunque igual es correcto.

"Se fijó la hora por defecto a las 12:00 ya que se sitúa en la franja de mayor frecuencia de servicio y evita el horario nocturno, donde la oferta es reducida o inexistente."

>El "ya que..." repetitivo
 
"OTP devuelve los instantes de paso en tiempo universal (epoch UTC) acompañados del desfase horario de la agencia (\texttt{agencyTimeZoneOffset}). El backend suma ese desfase antes de formatear las horas, de modo que los itinerarios se muestran en hora local de Toledo (Europe/Madrid), con el horario de verano resuelto automáticamente según la fecha consultada."

>Esto entiendo por qué lo pones en esta sección pero igual es mejor añadirlo en el backend donde se haga? Tú me dirás.

---

### 5.2.3 Construcción del grafo multimodal 

"El grafo se construye con un único comando Docker ejecutado sobre el directorio \texttt{otp-toledo/}, que debe contener el extracto OSM (\texttt{clm.osm.pbf}) y el feed GTFS (\texttt{GTFS\_Urbano\_Toledo\_2026.zip}):

\begin{lstlisting}[language=bash]
docker run --rm -v "otp-toledo:/var/opentripplanner" opentripplanner/opentripplanner:2.5.0 --build --save
\end{lstlisting}"

>Igual que antes, tema que ahora se hace automático, no repetir, ser consistentes entre secciones, etc, aunque creo que este está bien.

"OTP lee ambos ficheros y serializa el resultado en \texttt{graph.obj}: la red viaria OSM modela los tramos de acceso a pie a las paradas, y el feed GTFS aporta el servicio programado con horarios, paradas y geometría de las líneas."

>De nuevo el uso de ":" innecesario.

"El proceso tarda unos minutos \todo{tiempos} y solo es necesario repetirlo cuando se actualiza el feed; el extracto OSM puede reutilizarse entre versiones. El comando anterior corresponde a la generación manual del grafo."

>El mismo TODO de tiempos que en otras ocasiones, teniendo en cuenta que se hace auto, etc.

"El \texttt{graph.obj} resultante (unos 120\,MB) se versiona mediante Git LFS para que el sistema arranque sin reconstrucción en un clon limpio."

>Tercera mención a Git LFS si no me he dejado ninguna. No está mal, pero evitemos repetir.

"Como salvavidas, la orquestación incluye un servicio de inicialización idempotente (\texttt{otp-build}) que ejecuta \texttt{-{}-build -{}-save} únicamente si el grafo no está presente, de forma análoga a la compilación de los grafos OSRM."

>Lo de "salvavidas" queda raro. Aquí podemos utilizar el inglés "fallback" como término informático no? Beno entiendo que es un fallbuck. Lo de idempotente está bien. Igual en vez "de forma análoga" decimos "de forma similar"?

"Una vez disponible, OTP se lanza en modo de explotación (\texttt{-{}-load -{}-serve}) y queda accesible en el puerto 8080, exponiendo la API REST de planificación \cite{OTPDocs}."

>Lo de modo "explotación" es muy raro no? Puedes explicarmelo bien o buscar otro término? Y lo de planificación explicalo mejor.

---

### 5.2.4 Integración de itinerarios en el backend

"El router \texttt{/api/otp} del backend consulta OTP mediante peticiones HTTP a \texttt{/otp/routers/default/plan} y deserializa la respuesta para extraer los tramos (\textit{legs}) del itinerario seleccionado. OTP devuelve hasta cinco itinerarios alternativos."

>Lo de /otp/routers/default/plan me lo puedes explicar mejor lo que hace exactamente? Y por que llamamos ahi? Y lo de "OTP devuelve hasta cinco itinerarios alternativos" creo que se repite antes hace poco.

" El criterio de selección automática es el siguiente: se elige el primero que incluya al menos un tramo de transporte público (modo distinto de \texttt{WALK}); si ninguno cumple esta condición, se devuelve el de menor duración total. El frontend permite paginar entre las alternativas mediante los botones ``Anterior'' y ``Siguiente'', que transmiten el índice del itinerario deseado al backend, garantizando que el vector de características para la inferencia se calcula siempre sobre el mismo itinerario que se visualiza."

>No está mal aquí, y creo que los ":" y ";" están bien usados, podemos dejarlos aqui y en algun sitio más si quitamos la gran mayoría y los que ya he comentado. Lo único lo de "garantizando que el vector de características...", innecesario. Quiza llevarlo por otro lado, diciendo que se propaga más que transmite, y lo del índice es correcto pero vamos. 

>Lo de botones "Anterior y Siguiente" y todo tema de interfaz es mejor explicarlo más adelante en la parte del frontend creo, aqui me queda raro. Recuerda que estamos en backend, aplica esta lógica para toda la memoria.

"Para cada tramo del itinerario seleccionado se devuelve: modo de transporte, distancia, duración, geometría decodificada, parada de inicio y fin, nombre de línea, agencia y horarios de salida y llegada en formato \texttt{HH:MM}. Para los tramos de transporte público se añade a la consulta el parámetro \texttt{showIntermediateStops}, que incorpora a la respuesta de OTP las paradas intermedias de cada tramo; con ellas el backend compone la secuencia ordenada completa de paradas del tramo, desde el embarque hasta el desembarque, anotando para cada una su nombre, coordenadas y hora de paso. Esta secuencia alimenta el diagrama de paradas del itinerario descrito en la sección~\ref{subsec:impl_frontend_legs}."

>Aqui creo que está bien, revisa que no adelantemos mucho de la parte backend, la referencia al frontend diria que está bien.

"La geometría, codificada en formato polyline, se decodifica en el frontend y se concatena para componer la traza completa del itinerario."

>Lo de "se concatena para componer la traza" suena muy raro, hazlo más simple

"Cuando la distancia entre origen y destino es muy corta, o cuando no existe servicio de autobús entre los dos puntos en el horario fijado, OTP puede devolver como mejor itinerario una ruta completamente a pie, equivalente en tiempo y trayecto a la que ya proporciona OSRM con el perfil peatonal. En ese caso, si se construyese el vector de características de transporte público con los valores devueltos (tiempo de acceso cero, tiempo en bus cero, transbordos cero), el modelo podría asignar una probabilidad elevada al transporte público en trayectos sin servicio real. La solución adoptada, descrita en la sección~\ref{subsec:impl_backend_penalizacion}, consiste en detectar esta situación y sobrescribir las características de transporte público del vector con valores de penalización que llevan al modelo a descartar ese modo."

>Esto es correcto mencionarlo aquí? O lo quitamos y lo hablamos en el backend o en la parte de conocimiento experto o ajustes o algo así? Veo que al final lo hablamos en la 5.4.4, entonces no se si quitarlo directamente o hacer una introducción al problema y explicar la solución más adelante (incluso referenciarla aquí), pero igual no hace ni falta y lo podemos quitar porque sobre. Tú me dices.

"La Figura~\ref{fig:otp_itinerario} ilustra un itinerario multimodal típico en la interfaz del simulador: un tramo a pie inicial (trazado discontinuo en tono naranja oscuro) conecta el origen con la parada de embarque, un tramo en autobús (trazado continuo del color de la línea) cubre el recorrido principal, y un tramo a pie final lleva hasta el destino; las paradas del trayecto se marcan sobre el mapa con el color de su línea. En el panel lateral, una cabecera resume las horas de salida y llegada y la duración total, y bajo ella se despliega el detalle tramo a tramo: los tramos a pie como una línea de resumen y cada tramo en autobús como un diagrama vertical con todas sus paradas y la hora de paso por cada una. Al pulsar una parada del diagrama, el mapa se centra en ella y muestra su información, y los transbordos entre líneas se señalan de forma explícita.
"

>En este párrafo estamos explicando una captura de pantalla que viene justo después (Figura 5.3) que tengo desactualizada con la interfaz antigua. Además, quiero enseñar un ejemplo con transbordos, pero me estoy dando cuenta de que quizá todo esto habría que explicarlo en el frontend, incluso las capturas, y en estos apartados mostrarlo distinto. Eso o igual es correcto hacer una vista previa o algo y luego explicar en detalle más adelante, pero no sé, por cómo está redactado ahora mismo, parece que debería ser de frontend, y aquí explicar tema de integración, luego backend, luego frontend... sabes?

>También me hace cuestionarme el nombre del algunos sections/subsections... Por ejemplo, el anterior era "### 5.2.4 Integración de itinerarios en el backend" y ahora toca "## 5.3 Integración del feed GTFS". No es técnicamente lo mismo? Igual tenemos que cambiar nombres para explicar mejor lo que se habla, o reestructurar un poco. Sin miedo, puedes modificar, pero preguntame primero claro.

---

## 5.3 Integración del feed GTFS

### 5.3.1 Arquitectura de la capa estática

"El router \texttt{/api/gtfs} expone la información estática de la red de autobús directamente a partir de los ficheros del feed GTFS, sin depender de OpenTripPlanner. Esto permite consultar y visualizar la red (paradas, líneas y horarios) de forma independiente del planificador."

>Lo de "sin depender de OTP está repetido o no? Está OK? Creo que está bien pero tener cuidado. Y "planificador" es la palabra más correcta? revisa otros usos y todos los sitios donde la usamos para referirnos a OTP o a otra cosa.

"El feed GTFS consiste en una colección de archivos de texto plano con extensión \texttt{.txt} y formato de valores separados por comas, empaquetados en un único archivo ZIP \cite{GTFSOverview}. En el arranque del servicio, el backend descomprime y carga en memoria con \texttt{pandas} los seis ficheros necesarios: \texttt{stops.txt} (paradas con coordenadas y nombre), \texttt{routes.txt} (líneas de la red), \texttt{trips.txt} (servicios programados por línea), \texttt{stop\_times.txt} (horarios de paso por cada parada), \texttt{shapes.txt} (geometría de los trazados) y \texttt{calendar\_dates.txt} (calendario de excepciones de servicio) \cite{GTFSReference}. Los DataFrames resultantes permanecen en memoria durante toda la vida del proceso."

>Esto revisa que no repitamos también. No sé si ponerlo en lista o dejarlo así, o si hay que ponerlo aquí o estamos repitiendo como digo antes. Lo de "y formato de valores separados por comas" esta regular formulado, añade ahi algun verbo o algo conjuncion o algo.


"Para los horarios por fecha se añade el filtro de \texttt{calendar\_dates.txt}, que indica los días en que cada servicio está activo. Mantener todos los ficheros en memoria evita releer el feed completo en cada petición y elimina la necesidad de añadir una base de datos para datos que no cambian en tiempo de ejecución."

>Lo de "base de datos para datos" no es incorrecto? Entiendo que es un tema de traducción que has hecho, ten mucho cuidado, no traduzcas del inglés al español, escribe en español directamente.

"\begin{figure}[htbp]
  \centering
  \missingfigure{Diagrama de los seis ficheros GTFS como cajas (\texttt{stops}, \texttt{stop\_times}, \texttt{trips}, \texttt{routes}, \texttt{shapes}, \texttt{calendar\_dates}) con flechas que muestran los cruces por clave: \texttt{stops}\,--\,\texttt{stop\_times} (stop\_id), \texttt{stop\_times}\,--\,\texttt{trips} (trip\_id), \texttt{trips}\,--\,\texttt{routes} (route\_id), \texttt{trips}\,--\,\texttt{shapes} (shape\_id) y \texttt{trips}\,--\,\texttt{calendar\_dates} (service\_id). Resaltar la cadena stops$\to$stop\_times$\to$trips$\to$routes que resuelve ``líneas por parada''.}
  \caption{Cruces entre los ficheros del feed GTFS para resolver las consultas de la capa estática.}
  \label{fig:gtfs_joins}
\end{figure}
"

>TODO: Hacer este diagrama, vendrá bien para la defensa.

---

### 5.3.2 Endpoints disponibles

"\subsection{Endpoints disponibles}
\label{subsec:impl_gtfs_endpoints}

La capa GTFS expone cuatro endpoints que cubren las operaciones necesarias para la visualización cartográfica y la consulta de la red:

\begin{itemize}
..."

>Toda esta subsection me genera dudas. Debería ir en la parte de backend? Porque estamos explicando los endpoints etc. del router GTFS, y quizá se lia con OTP porque es dependiente o algo asi. En cualquier caso, al estar explicando endpoints del backend, me queda más como para después junto al resto del backend. De hecho, en la parte de backend mejor si explicamos todo, desde la documentación FastAPI hasta la lógica de cada router y sus endpoints, etc. Y en el frontend tema interfaz, etc.

---

### 5.3.3 Coloración de líneas y agrupación por sentido

>Aquí hay fallos estructurales grandes. Primero, la coloración de líneas y agrupación por sentido deberían ser dos subsections distintas, aunque se hicieran en la misma tirada, tenemos que redactar un orden lógico, aunque difiera un poco del real por cosas que me di cuenta después, vamos a explicarlo con el sistema finalizado, ya si me preguntan daré explicaciones de orden o los remito al ch3 pero no líemos. 

>Además, la coloración de líneas, aunque podemos mencionar algo a nivel arquitectura (ch4) o en alguno de los subsections anteriores donde decimos cosas del formato del GTFS, debería ir toda en frontend. Habla de funciones que son solo para el renderizado, es teoría de color y tema de interfaz, etc. En cualquier caso, te voy a hacer comentarios sobre ese apartado, pero habría que moverlo.

>La agrupación por sentido también lo veo más un tema de arquitectura o de alguna subsection anterior, literalmente volvemos al formato del GTFS y como UNAUTO ha montado los sentidos para cada línea como route_ids distintos. Luego, con esto explicado ya con anterioridad, se entiende mejor el tema de coloración de líneas y que los snetidos ya vienen agrupados y que lo cogemos por short_name en el backend o donde sea, etc.

>Con todo esto, me surge una duda grande estructural y a donde quiero ir. ¿Hace falta el 5.3 INTEGRACIÓN DEL GTFS directamente? O lo podemos mover todo a otros capítulos, o añadir un subapartado o un apartado antes donde recogemos todos estos temas del formato GTFS? Incluso ampliar el ch4 en su lugar. Todo lo que no corresponda a frontend o backend o algo de ch5 que pudiesemos aprovechar, se iría a ch4. ¿Me enteindes? Esta es una de las decisiones clave que debemos tomar.

>A continuación, te comento sobre la coloración y agrupación para que ya tengas una idea de como lo quiero cuando lo muevas:

"El feed GTFS de Toledo incluye en \texttt{routes.txt} un color por línea (campos \texttt{route\_color} y \texttt{route\_text\_color}), que la interfaz utiliza directamente para mostrar cada línea con el color oficial del operador. Si un feed no incluye esos campos, la función \texttt{routeColor()} genera un color de reserva a partir del nombre corto de la línea:"

>Esto del principio es un poco lo que podríamos explicar mejor en otro sitio anterior o en un propio apartado del formato del GTFS o en arquitectura o lo que sea. Y tema interfaz al frontend, pero explicar antes el formato en el que viene y que le ponemos ese color (con algunos ajustes para facilitar la visibilidad) y si viene sin color se genera uno de forma determinista. También justo al final esos dos puntos ":" habría que reemplazarlos por otra cosa, o explicar quizá en una bullet list o enumerada los pasos que se realizan si son mas de 2.

"\begin{lstlisting}[language=Java, caption={Color de línea: feed GTFS como fuente primaria y hash determinista como respaldo.}, label={cod:gtfs_color}]
function hslForKey(key: string): string {
  let h = 0;
  for (let i = 0; i < key.length; i++) h = (h * 31 + key.charCodeAt(i)) | 0;
  return `hsl(${Math.abs(h) % 360}, 70%, 35%)`;
}
function routeColor(r: { color?: string | null; short_name?: string | null; id: string }): string {
  if (r.color) return `#${r.color}`;
  return hslForKey(r.short_name || r.id);
}
\end{lstlisting}
"

>Habría que explicar los parámetros de cada función, hacer hincapié en que la funcion hslForKey es recursiva y en general la manera en la que lo hemos programado leyendo el nombre, que esta chulo. Tambien habrá que incluir la función de `isLightColor`, que se menciona justo después. Y quizá convendría reconducir un poco los textos aprovechando estos consejos para que el código tenga más sentido y venga bien explicado.

"Este criterio de color se aplica de forma homogénea en toda la interfaz: en las etiquetas de línea del catálogo y del panel de rutas, en las etiquetas de las paradas, en el diagrama de paradas y en el trazado de la línea sobre el mapa."

>Cuidado con los dos puntos ":", utiliza conectores, (tanto..., como...) o algo así, es que repites mucho las enumeraciones con ":".

"Algunas líneas del feed de Toledo son de color blanco (por ejemplo, la L14), y parecería invisible sobre el fondo claro de los paneles y del mapa. Para evitarlo, la función \texttt{isLightColor()} mide cuán claro es un color a partir de sus componentes de rojo, verde y azul y, si supera un umbral cercano al blanco, le añade un contorno oscuro.
"

>Esto es lo que me refería del isLightColor, que quizá habria que moverlo. También me suena raro el "parecería invisible". Revisar redacción en todo para variar.

---

>Ahora vamos con lo que en mi opinión sería otra sección, "Agrupación por sentido", o como no es muy larga meterlo en otro apartado. Eso o ampliarlo y explicarlo bien, incluso meterlo largo en otro apartado, como sea:

"El feed de Toledo contiene 56 entradas en \texttt{routes.txt} pero solo 25 líneas distintas, ya que el operador registra cada sentido y variante de recorrido como un \texttt{route\_id} independiente con el mismo \texttt{route\_short\_name}. La interfaz agrupa esas entradas por nombre corto en un diccionario (\texttt{routeSiblingsByShortName}), de modo que el catálogo muestra una sola entrada por línea. Cuando el usuario selecciona una línea, el sentido activo se deduce de la posición del \texttt{route\_id} elegido dentro del grupo de variantes; así, al pulsar la etiqueta de una parada en el mapa (que conoce el \texttt{route\_id} exacto del servicio que pasa por ella) se activa directamente el sentido correcto, sin lógica adicional."

>Esto es que aquí en coloración no pinta nada porque no dice nada de la coloración y creo que tiene más peso incluso y debería ir en su propia sección o en arquitectura. Tener cuidado porque estaoms adelantando un poco de frontend creo, mejor explicarlo todo en alguna parte del formato de GTFS y las transofrmaciones o cosas así. Estoy diciendo quizá mucho lo de arquitectura aunque quiza hay un hueco en el ch5 mejor, recomiéndame.

"La Figura~\ref{fig:gtfs_paradas} muestra el panel Red GTFS. El catálogo se organiza en un acordeón donde cada fila representa una línea física con su badge coloreado y nombre largo. Al expandir una entrada con varios sentidos, aparece una sublista con las variantes (sentidos) de la línea y el identificador activo resaltado mediante un borde lateral de su color. El panel muestra además un diagrama vertical de paradas inspirado en los paneles de andén: una barra vertical del color de la línea, con las terminales como puntos rellenos, las paradas intermedias como aros huecos y la parada de referencia resaltada en azul. Al pulsar sobre el nombre de una parada, el mapa ejecuta un desplazamiento animado (\texttt{flyTo}) hasta esa posición. Una tabla de salidas agrupada por hora completa la información de la ruta seleccionada; las salidas se muestran siempre para la fecha activa, atenuando las anteriores a la hora seleccionada en el control global, resaltando en azul las posteriores y en negrita la próxima salida. Si la línea no circula el día elegido, se sustituye la tabla por un aviso que indica los días en que sí presta servicio. De este modo el panel no necesita sus propios selectores de día: la fecha y la hora provienen del control global descrito en la sección~\ref{subsec:impl_otp_fecha}.



\begin{figure}[H]
  \centering
  \missingfigure{Panel Red GTFS: a la izquierda, el acordeón con la línea seleccionada desplegada mostrando el diagrama vertical de paradas y la tabla de horarios agrupada por hora (con las salidas pasadas atenuadas y la próxima resaltada); a la derecha, el trazado de la línea sobre el mapa de Toledo con sus paradas coloreadas.}
  \caption{Panel GTFS con acordeón de líneas, diagrama de paradas y horarios.}
  \label{fig:gtfs_paradas}
\end{figure}"

>En mi opinión todo esto es FRONTEND. Tanto toda la explicación de los controles y la interfaz y los componentes al mas minimo detalle, como las capturas de la interfaz. Por eso, tengo mis dudas si quitar tambien la foto de la interfaz de OSRM donde muestro las 3 rutas y lo dejamos para frontend o cómo. Yo veo bien lo de hacer diagramas, tablas, listas, código, etc. en ch4 y principio de ch5, y a partir de frontend meter capturas de la aplicación. Sería solo quitar un par de las que llevamos creo, y hacer toda la seccion de Frontend bien claro.

>Pequeños apuntes, ya que estoy: 

"El catálogo se organiza en un acordeón donde cada fila representa una línea física con su badge coloreado y nombre largo."

>No sé si "catálogo" es el mejor término. Lo de acordeón es un término muy de frontend que habria que explicar con anterioridad o si lo movemos todo al frontend pues hacer una explicacion en la primera mención, porque se reutiliza mucho ese elemnto. Lo mismo para "badge". Y con nombre largo me imagino que te refieres al de la línea.

"Al expandir una entrada con varios sentidos, aparece una sublista con las variantes (sentidos) de la línea y el identificador activo resaltado mediante un borde lateral de su color."

>Aquí repetimos "sentidos", "variantes" confunde con otras cosas, revisar el uso correcto de línea, ruta, etc., y lo de "el identificador activo resaltado mediante un borde lateral de su color" es muy raro, muy sobreexplicativo y demasiado técnico, cuando realmente es simplemente un efecto hover y active tipico cuando marcas un botón, no hace falta.

"El panel muestra además un diagrama vertical de paradas inspirado en los paneles de andén: una barra vertical del color de la línea, con las terminales como puntos rellenos, las paradas intermedias como aros huecos y la parada de referencia resaltada en azul. 

>Lo de la parada de referencia resaltada en azul tambien raro, y está regular explicado, porque eso es un detalle muy concreto de cuando pinchas en una parada de la línea, y habría que repetirlo tambien al pinchar en paradas del trayecto propuesto por OTP para un par origen-destino, osea que no liarnos tantos, que se nota mucho que es IA/relleno.

"Una tabla de salidas agrupada por hora completa la información de la ruta seleccionada; las salidas se muestran siempre para la fecha activa, atenuando las anteriores a la hora seleccionada en el control global, resaltando en azul las posteriores y en negrita la próxima salida."

>Esto está fatal explicado, sobretodo el principio, así la oración enunciada en pasiva o muy raro, muy robótico, haz parrafos descriptivos, no tan tecnicos y traducidos del inglés, es que se nota mucho que sigues las estructuras del inglés.

" De este modo el panel no necesita sus propios selectores de día: la fecha y la hora provienen del control global descrito en la sección~\ref{subsec:impl_otp_fecha}."

>Esto parece metido con calzador, igual no hace ni falta, ya me dices, como vamos a cambiar eso de la fecha también según te he comentado antes...

---

## 5.4 Implementación del backend FastAPI

### 5.4.1 Estructura modular

"El backend está implementado con FastAPI sobre Python y organizado en módulos por responsabilidad. Un directorio \texttt{api/} contiene los cuatro routers (\texttt{routes\_osrm.py}, \texttt{routes\_otp.py}, \texttt{routes\_gtfs.py}, \texttt{routes\_lpmc.py}); un directorio \texttt{services/} contiene la lógica de negocio desacoplada de la capa HTTP (\texttt{osrm\_client.py}, \texttt{lpmc\_inference.py}); y el módulo raíz \texttt{main.py} monta los routers y habilita CORS (\textit{Cross-Origin Resource Sharing}), el mecanismo que autoriza al navegador a que la interfaz web, servida desde un puerto distinto, consuma la API del backend."

>Aquí lo de CORS igual ocupa más la explicación que el resto del párrafo, así que tengamos cuidado, redactemos bien.

"Los endpoints expuestos por cada router se recogen en la Tabla~\ref{tab:endpoints_api} del capítulo~\ref{ch:arquitectura}."

>Está bien referenciar esa tabla de arquitectura por si quieren tener una vista global pero cuidado, porque es aquí el sitio donde habría que explicar y desarrollar a fondo esos endpoints, no en el de arquitectura.

"La separación en módulos permite desarrollar, probar y documentar cada router de forma independiente. FastAPI genera documentación OpenAPI automática en \texttt{/docs} que refleja el estado actual de los endpoints en tiempo real, lo que facilitó la verificación del contrato de cada integración durante el desarrollo sin necesidad de un cliente HTTP externo."

>El "lo que facilitó la verificación del contrato de cada integración" está fatal, aparte del uso repetitivo de "Lo que", lo de "contrato" con cada sprint/integración no es correcto, es un termino anglosajón diría, utilia otra cosa o directamente no te enrolles en esto. Y lo de sin necesidad de un cliente HTTP externo también me parece redundante, qué ibas a usar si no? Algo escrito por ti para mostrar la documentación de cada endpoint o cómo? Revisemos esto por favor

>También, lo que quiero hacer con esta sección es dividirlo por routers (más o menos como está), pero me falta el de GTFS, y meter todas las mierdas que deciamos en las subsections anteriores que nos estabamos adelantando a la parte de backend. Así como desarrollar los endpoints, recoger toda la información de lógica y demás en un sitio y dejar todo bien explicado para el frontend también. Además, explicar bien tema documentación, docker, al final es su propio contenedor no? Pues eso.En general, repartir mejor la información, hablando en arquitectura un poco del disñeo y estructura del backend con routers etc pero sin entrar a fondo en los endpoints no?

---

### 5.4.2 Router OSRM: consultas multiperfil

"El router \texttt{/api/osrm/routes} acepta un par origen-destino y una lista de perfiles solicitados, y lanza las consultas a los tres contenedores OSRM en paralelo mediante \texttt{asyncio.gather}."

>Aqui empezmaos directamente con /api/osrm/routes, ¿esto es un endpoint del router? O es el propio router? es que la palabra "routes" lía. Que quede bien explicado desde la arquitectura y en apartados anteriores para mantener consistencia a lo largo de estos apartados.

>También falta poner algo entre el "mediante" y el "asyncio", quizá "mediante el método asyncio"?

"La paralelización reduce la latencia total al tiempo de la consulta más lenta en lugar de la suma de las tres, lo que es especialmente útil cuando se solicitan los tres perfiles a la vez."

>Este lo que es completamente innecesario, ademas no se si está explicado ya lo de shift+click, en cualquier caso eso es un tema de interfaz. Simplemente confirmar que lo hacemos de manera paralela.

"Para cada perfil, el backend recibe la distancia en metros, la duración en segundos y la geometría en formato polyline, decodifica esta última en una lista de coordenadas \texttt{[lat, lon]} lista para Leaflet, y convierte las duraciones de segundos a horas antes de construir el vector de características, ya que el dataset LPMC almacena todas las duraciones en esa unidad."

>En este párrafo no hay como muchísimas comas? Parece una enumeración muy larga. De hecho estoy viendo que todo el párrafo está escrito en una oración. Por favor, coherencia y buena praxis. Separemos donde sea necesario. No repitamos tampoco mucho y adentremonos más en los endpoints etc, este es el sitio del backend donde explicar toda la logica, no hay que hacerlo con prisa.

>También repetimos lista como verbo y como nombre muy cerca, arreglamos. Quizá "lista para Leaflet" ponemos "para que peuda ser enviada a Leaflet" o algo así?

---

### 5.4.3 Router OTP: itinerarios multimodales

"La geometría de cada tramo se concatena para formar la traza completa del itinerario, que el frontend divide y renderiza por segmentos según el modo."

>Según el modo... hay que poner "de transporte", con cuidado esto, y de nuevo no adelantar mucho al frontend aunque aqui está bien.

---

### 5.4.4 Penalización de itinerarios sin transporte público real.

>Antes de comentar esta sección, me he dado cuenta de que no tenemos ninguna sección para el router GTFS. No sería mejor comentar aquí lo que decíamos antes en 5.3? Tanto lo de agrupación por sentido y todas las cosas que han hecho falta relativas al router GTFS y en general el tema de líneas? No sé como lo ves, es uno de esos cambios estructurales gordos. Y esto de penalización no se si meterlo en alguno de los routers, o cuando ya estén todos explicados, no sé.

"Cuando OTP devuelve un itinerario compuesto exclusivamente por un tramo a pie, sin ningún tramo de transporte público, las características de transporte público del vector de entrada (tiempo de acceso a la parada, tiempo en el vehículo, tiempo de espera y de transbordo, y número de transbordos) tomarían valores próximos a cero."

> Lo de "tomarían valores próximos a cero" es más o menos correcto, por no decir que serían directamente cero. Si no tiene tramos en transporte público, entiendo que solo devuelve el pt_walk. Explica bien los campos que irían como 0 y la que tendria la distancia o tiempo andando para ese caso de pt_available=false. Explicarlo todo bien vaya. 

"El problema es que esos mismos valores bajos caracterizan en el dataset a un transporte público rápido y directo, por lo que el modelo podría asignar una probabilidad elevada al transporte público en un trayecto donde en realidad no hay servicio."

>Esto está bastante bien, no se sí lo de "caracterizan en el dataset a un..." está correctmaente formulado, pero me suena aceptable. Igual se puede poner un poquito mejor.

"El caso se detectó durante las pruebas de integración del módulo de inferencia: en trayectos cortos en los que la opción más rápida era ir a pie, OTP devolvía ese único tramo como mejor itinerario y la inferencia resultaba engañosa."

>Cuidado con los dos puntos ":" repetitivos, y también cuidado con lo der que OTP devolvía ese único tramo como mejor itinerario. Nosotros priorizamos los itinerarios que devuelve OTP para que siempre utilicen transporte público, si el primero que sale es sin transporte público, es que OTP solo devuelve ese, ninguno más (solo 1, no 5). Pero bueno, está medio bien, solo que no se si es necesario explicar y justificar tanto cuando lo detectamos.

"Para evitarlo, el backend comprueba si el itinerario contiene algún tramo de transporte público. Si no es así, sobrescribe las seis características de transporte público (\texttt{dur\_pt\_access}, \texttt{dur\_pt\_bus}, \texttt{dur\_pt\_rail}, \texttt{dur\_pt\_int\_waiting}, \texttt{dur\_pt\_int\_walking} y \texttt{pt\_n\_interchanges}) con un valor situado en el extremo superior de su distribución. En concreto, a cada característica se le asigna el valor que, tras el escalado estándar (\texttt{StandardScaler}) del modelo, queda cinco desviaciones típicas por encima de la media de entrenamiento: es decir, $\mu + 5\sigma$, tomando la media $\mu$ y la desviación típica $\sigma$ que el escalador aprendió de esa característica."

>Esto estaría muy bien poner la formula matemática o el código o lo más simple para que se entienda, porque en texto es un poco lío. Al menos la forma en la que sacamos los valores para ponerselos al array de valores de transporte publico para que los modelos lo descarten rapidamente. Y lo de "la desviación típica $\sigma$ que el escalador aprendió de esa característica." es correcto lo de el escalador? igual podemos utilizar el término en inglés porque "escalador" suena a persona que hace escalada como deporte?

>Por cierto, el tutor me ha corregido este párrafo a: "Un problema detectado reside en que los modelos de aprendizaje automático que serán entrenados en la Sección~\ref{sec:impl_lpmc} realizan la inferencia con un número fijo y predefinido de modos de transporte. De esta forma, si el viaje no admite transporte público, no es posible eliminar este modo para la inferencia. Para solucionar este problema, el backend comprueba si el itinerario contiene algún tramo de transporte público. Si no es así, sobrescribe las seis características de transporte público (\texttt{dur\_pt\_access}, \texttt{dur\_pt\_bus}, \texttt{dur\_pt\_rail}, \texttt{dur\_pt\_int\_waiting}, \texttt{dur\_pt\_int\_walking} y \texttt{pt\_n\_interchanges}) con un valor situado en el extremo superior de su distribución. En concreto, a cada característica se le asigna el valor que, tras el escalado estándar (\texttt{StandardScaler}) del modelo, queda cinco desviaciones típicas por encima de la media de entrenamiento: es decir, $\mu + 5\sigma$, tomando la media $\mu$ y la desviación típica $\sigma$ que el escalador aprendió de esa característica. De este modo el modelo percibe un transporte público como un modo de transporte poco interesante, ya que tendría tiempos de viaje y número de transbordos extremos, haciendo que fue prácticamente inviable, y descarta esa opción sin necesidad de modificar su arquitectura ni el número de variables de entrada."

"De forma análoga, en trayectos muy cortos (menos de 500~m en línea recta) el backend añade un recargo de tiempo al coche, que representa el aparcamiento y el acceso al vehículo. Sin él, el modelo tendería a elegir el coche siempre que su tiempo de conducción fuese menor, ignorando que para distancias tan cortas el sobrecoste de aparcar hace más razonable ir a pie. Ambas correcciones son ejemplos de conocimiento experto inyectado en las entradas del modelo; el análisis de cómo responde cada modelo a la penalización y la justificación de este enfoque se abordan en la sección~\ref{subsec:impl_lpmc_entrenamiento}."

>Esto no sé si está bien aquí? Sobretodo si al fianl lo hacemos por routers, no sería más cosa de OSRM o algo así al ser relativo a coche y no toca OTP ni GTFS? O directamente lño explicamos en la Sección 5.6.4 bien, como conocimiento experto, igual que lo que hacemos con trayectos sin transporte público. Sabes por donde voy no? Si hacemos la estructuracionq ue he propuesto, este párrafo no iría aquí, a no ser que hagamos uno nuevo en la parte de frontend para estas penalizaciones, sin importar si son de OSRM, OTP, GTFS, LPMC, etc. aunque yo pondria cada cosa en su sitio.

>Aunque el tutor me ha dicho respecto a este párrafo "Muy razonable y bien explicado. Bien hecho!", así que mantenemos la escritura

---

### 5.4.5 Router LPMC: inferencia modal y descubrimiento de modelos.

>Este apartado lo veo mejor estructurado que los anteriores, con una introducción y explicación que explican el router, seguido de los endpoints. No se si hay alguna manera mejor de explicar los endpoints que en lista, igual con negrita haciendo subsubsubapartados, aunque no vayan al índice, o seguimos así con la lista. Lo digo para poder escribir varios párrafos, hagamos lo más correcto en el registro de un TFM.

"Expone cuatro endpoints:"

>Buen uso de los dos puntos, para darte refuerzo positivo jaja.

"\item \textbf{Predicción con modelo seleccionable} (\texttt{POST /api/lpmc/predict}): recibe el par origen-destino, el índice del itinerario OTP seleccionado, el perfil de usuario y, de forma opcional, el identificador de variante de modelo (\texttt{model\_variant}). Si no se especifica, se usa la variable de entorno \texttt{LPMC\_MODEL\_VARIANT} como predeterminado, manteniendo la compatibilidad con scripts externos que no pasen el parámetro. "

>Lo de "el índice de OTP seleccionado", recordarte que es hasta 5 (pueden ser menos). No está mal, pero por asegurarnos. Quizá explicar un poco mejor, en vez de "índice" buscar una palabra mejor.

>Lo de "el perfil de usuario" quizá deicr mejor las variables sociodemográficas, o no se si ahi se refiere a que le pasamos un ID de perfil, entiendo que le pasamos los valores de las variables.

>El "identificador de variante de modelo" queda muy raro, y cuidado porque no sé si aqui te refieres al nombre del modelo en sí, con eso que hacemos regex, o el tema de "no_hh" cuando teníamos un modelo mal entrenado con los households, eso no puede quedar en código

"La respuesta incluye la probabilidad de cada uno de los cuatro modos (a pie, bicicleta, transporte público y coche), el modo más probable y su probabilidad,"

>Los "modos" mencionar que son "de transporte", Y decir que es "el modo más probable para dicho usuario junto con su probabilidad"

>Cuidado con los terminos "confianza" "probabilidad" "porcentajes" y derivados de éstos... Usemos una convención común para referirnos a los porcentajes que devuelven los modelos para cada modo de transporte y el modo con mayor porcentaje o puntuación.

"el vector de características de ruta (con las penalizaciones aplicadas si el trayecto resultó ser solo a pie) y varios metadatos del modelo: la ruta del artefacto, el indicador \texttt{pt\_available} (verdadero cuando el itinerario contiene al menos un tramo de transporte público) y el indicador de trayecto corto."

>Lo del vector de características de ruta con las penalizaciones aplicadas, cuidado si movemos lo de penalizaciones, para explicarlo bien. Habria que explicarlo en el sitio donde se haga, y quiza una pequeña mencion en la vista global en la arquitectura.

>Cuidado con el uso de ":" de nuevo para enumeraciones, mejor explicarlo bien que en una enumeración rápida poco visual, sobretodo cosas de parámetros, etc.

>También cuidado con adelantar lo del indicador de trayecto corto, y explicar bien el pt_available donde corresponda.

"\item \textbf{Comparación de modelos disponibles} (\texttt{POST /api/lpmc/compare}): ejecuta la predicción con cada variante en secuencia y devuelve un diccionario con los resultados de cada una. La ejecución es secuencial, no concurrente: a diferencia de las consultas a OSRM y OTP (que esperan respuestas de red y se benefician de la concurrencia), la inferencia es un cálculo intensivo en CPU que el intérprete de Python ejecuta en un único hilo, por lo que lanzarla en paralelo no aceleraría el proceso. La latencia adicional es aceptable, ya que el usuario activa la comparación de forma explícita, al margen del flujo de cálculo principal."

>Cuidado de nuevo con "variante", y lo de que se ejecuta en secuencia justo después dices la ejecución es secuencial, y el uso de dos puntos ":"

>Además, no hay que decir lo de que el intérprete de Python ejecuta en un único hilo porque no tiene sentido. Si yo quisiera podria hacer inferencia con 3 hilos a los 3 modelos a la vez. No se hacía para no afectar al rendimiento de la CPU y que pudiera llegar a variar los resultados? No tanto en accuracy si no en tiempo que tardan los modelos en cada cosa? bueno igual me estoy equivocando, tu me dirás. Igual mejor no decimos esto y ya está, o si lo decimos que tenga una justificación correcta que no sea porque sí, si no hay nada interesante que decir pues no decimos nada.

>Lo de la latencia también lo podemos quitar.

"  \item \textbf{Depuración del vector de características} (\texttt{POST /api/lpmc/debug-features}): devuelve el vector completo ensamblado por \texttt{\_build\_feature\_frame()}, con los valores crudos y escalados. Facilita verificar que las variables de ruta calculadas a partir de OSRM y OTP se encuentran en el rango esperado por el dataset LPMC, y fue la herramienta principal para diagnosticar los errores de unidades descritos en la sección~\ref{subsec:impl_lpmc_entrenamiento}."

>Lo de los "valores crudos y escalados" suena raro y se puede malentender, decir bien los valores, antes y después de pasar por el StandardScaler o algo. El "facilita verificar" tambien suena raro, alggo mas sencillo, simplemente decir eso diagnosticar errores, ya poemos entrar en detalle luego con los errores de unidades y demás en la sección 5.6.4, no hace falta referenciarlo aqui quizás.

"  \item \textbf{Descubrimiento de modelos disponibles} (\texttt{GET /api/lpmc/models}): escanea \texttt{lpmc/models/} buscando pares de ficheros \texttt{\{nombre\}\_lpmc.joblib} y \texttt{\{nombre\}\_lpmc\_scaler.joblib}. Devuelve la lista de variantes disponibles y la variante predeterminada según \texttt{LPMC\_MODEL\_VARIANT}. Este mecanismo permite añadir un modelo entrenado externamente al directorio y que la interfaz lo detecte en la siguiente petición, sin necesitar reiniciar ningún contenedor."

>Cuidado con "variantes", y de nuevo, quiero indagar en esto, no se si podemos montarlo mas sencillo sin modificar mucho código o esta es la manera más optima, quizá si estuviera mejor explicado...

"Dos detalles transversales completan el router. Primero, el identificador de variante recibido del exterior se valida con una expresión regular (\texttt{\textasciicircum[a-z0-9\_]\{1,32\}\$}), que solo admite letras minúsculas, dígitos y guiones bajos; con ello se evita que un valor manipulado se interprete como una ruta de fichero arbitraria al construir el nombre del artefacto a cargar. Segundo, los modelos se cargan de forma diferida y se conservan en una caché en memoria: la primera predicción con una variante asume el coste de leer y deserializar su artefacto desde disco, y las siguientes lo reutilizan sin volver a leerlo."

>Este párrafo es la primera mención a lo de validar con expresión regular y creo que va relacionado con el descubrimiento de modelos disponibles. No me gusta la estructura del párrafo, lo de "dos detalles transversales completan el router" con Primero y Segundo no me convence. Quiero revisar contigo bien como estamos haciendo lo de la expresión regular por si es overkill, al igual que el /models, aunque entiendo que es correcto para la UX.

---

### 5.4.6 Resolución de rutas y portabilidad

>Esta sección me pasa lo mismo que con el final de la anterior, que son cosas del código que quiero revisar por si son overkill o están bien. Me asusta que pueda ser algun fallo o alucinación de Claude.

"El backend necesita localizar en disco los datos del feed GTFS y los artefactos de los modelos. En lugar de codificar rutas absolutas, que dependerían del equipo y del sistema operativo concretos, cada módulo deriva la ruta que necesita a partir de su propia ubicación mediante la biblioteca estándar \texttt{pathlib}. Por ejemplo, la función auxiliar \texttt{\_project\_root()} del módulo de inferencia evalúa \texttt{Path(\_\_file\_\_).resolve().parents[4]}, que asciende cuatro niveles desde el fichero del módulo hasta la raíz del repositorio; desde ahí se compone la ruta a \texttt{lpmc/models/}."

>Lo del Path(file).resolve().parents[4], el "4" cambia según la carpeta en la que estemos? De nuevo, entiendo que es para no hardcodear y para que sea compatible en todos los sistemas operativos, pero hagamoslo bien, porque esto al final es medio hardcodear, o al menos expliquémoslo mejor. Aun asi lo reviso contigo, si me das la explicación.


"Este enfoque es portable entre el entorno de desarrollo (Windows) y el contenedor de ejecución (Linux) porque \texttt{pathlib} abstrae el separador de directorios propio de cada sistema y las rutas se calculan siempre de forma relativa a la posición del código, no a un punto de montaje fijo."

>No está mal, me suena raro lo de que Este enfoque es portable, decirlo mejor, que es por compatibilidad.

"La orquestación de los contenedores y el montaje del repositorio en ellos se describen en la sección~\ref{sec:arch_infra}."

>Esto igual innecesario?

---

## 5.5 Implementación

> Esta sección igual toca también reestructurar, porque me gustaría que hubiera un apartado de tecnología como tenemos, otro de diseño de interfaz, otro de mapa con los controles etc, y uno por cada rail del panel lateral izquierdo con las explicaciones relevantes a cada raíl, itinerarios, etc. ahora que ya está explicado el mapa de base y los controles etc. se puede explicar toda la lógica y como cada raíl pinta cosas en el mapa o lo modifica o cambia el comporamiento de la app...

>Además, como te he comentado a lo largo de este documento, quiero mover muchas cosas de fuera a este bloque (las explicaciones de frontend que hay en los puntos anteriores del ch5, las capturas de la interfaz, etc.). Esta debería ser la sección con más capturas y figuras de la aplicación, dejando las anteriores para backend y diagramas. O alguna captura cuando sea realmente necesario. También recuerda lo de la coloración determinista de líneas, etc. Imagino que deberia ir en el raíl de GTFS, aunque tambien afecta al de Rutas por OTP y los "Detalles del itinerario" (donde vienen los pasos, transbordos, tramos andando o en bus, etc.)

### 5.5.1 Tecnologías y Estructura

"El frontend está desarrollado con React 18, Vite y TypeScript."

>Aqui viene mi pregunta, TanStack no es suficientemente grande para ponerlo aquí? Así como otras tecnologías? O aunque luego lo pongamos como plugins (Lucide-React, React-Leaflet, y cualquier cosa que usemos, acreditando también a los creadores con citas y demás..., dando documentación de las tecnologías si no se han dado ya antes en el TFM, etc.)


"Vite proporciona recarga en caliente instantánea durante el desarrollo y genera el bundle de producción con división de código automática."

>Hay que explicar mejor lo de recarga en caliente instantánea durante el desarrollo, y no entiendo lo de la división de código automática. Además "bundle" no es del todo corecto.

"TypeScript añade comprobación estática de tipos, especialmente útil al manejar las estructuras de datos complejas que devuelven los endpoints del backend: itinerarios OTP con desglose por tramos, respuestas GTFS con múltiples entidades relacionadas y vectores de probabilidades de los tres modelos."

>Quizá poner aquí o antes si expandimos un pcoo sobre cada tecnología (si no está hecho ya) que es (a mi entender) JavaScript con gestión de tipos, no? O me equivoco.

>Lo de especialmente útil quizá es innecesario si lo explicamos bien antes, y el uso de ":" de nuevo es excesivo, hagamoslo bien. De hecho igual es innecesario decir lo que devuelven los endpoints otra vez.

"Leaflet se integra a través de React-Leaflet como librería cartográfica, y los iconos de la interfaz se proporcionan mediante Lucide React, una biblioteca de iconos SVG que no introduce dependencias adicionales en tiempo de ejecución."

>Explicar mejor Leaflet, podemos darle un poco más de profundidad a las librerías que utilizamos, aunque sea una mini lista en este apartado de tecnologías. Lo de "no introduce dependencias adicionales" habria que explicarlo mas, no se sobreentiende a lo que te refieres, o quitarlo, o decir algo distinto de la biblioteca como su fuente/origen.

"La aplicación está estructurada en dos componentes principales, \texttt{App} y \texttt{MapView}, descritos en la sección~\ref{sec:arch_frontend}. Esta separación, en la que \texttt{MapView} recibe todos sus datos como \textit{props} y no mantiene estado propio, simplificó el desarrollo incremental de la capa cartográfica de forma independiente al resto de la lógica."

>Aparte de revisar mejor que esa /ref está bien, lo del "simplficó el desarrollo" y demás suena de nuevo a sobrejustificación de Claude y lo veo innecesario, sobretodo si está explicado ya antes. Se puede poner en una linea algo simple recordando, pero no sobrejustificar.

---

### 5.5.2 Diseño de la interfaz: rail lateral y paneles

>Esta sección no sé si está bien en esta posición o debería ir después del mapa y antes de los endpoints, o el mapa para el final, no tengo ni idea. En general hay que reordenar un poquito el 5.5 y hacer los subapartados por cada raíl (o paneles dentro del raíl, como sea). 

>Mucho cuidado a lo largo de todo el documento con el uso de "rail" "raíl" "\textit{rail}", etc. Siempre de la misma forma. Si lo usamos en inglés, con cursiva. Si es en español, quizá buscar algo alternativo? Como cinta o barra lateral o algo?

>Habrá que reestructurarla, en cualquier caso te voy poniendo mis comentarios:

"La interfaz sigue un esquema inspirado en Google Maps: el mapa ocupa todo el área de la ventana del navegador como fondo, y los controles flotan sobre él sin desplazarlo."

> Lo de los controles flotan sobre él sin desplazarlo, no se entiende. El uso de los ":" es excesivo. Hazlo más desarrollado, no digas solo Google Maps, puedes decirlo pero añadiendo "y otras interaces cartográficas" o algo Así

"El elemento central de navegación es un \textit{rail} lateral izquierdo de ancho fijo (64~px), siempre visible, que contiene los botones de acceso a los paneles funcionales del simulador. Al activar un panel, un contenedor de 360~px de ancho emerge sobre el mapa a la derecha del rail sin alterar sus dimensiones. 

>Revisar las medidas de píxeles, además igual conviene decir que es compatible con todo tipo de tamaños (responsive y adaptive, etc., cosas muy de literatura/plan de estudios de carrera/máster).

>Lo de emerge sobre el mapa a la derecha es mentira, el panel está a la izquierda del mapa (aunque salga hacia la derecha del rail inmovil, pero es confuso), y lo de sin alterar sus dimensiones innecesario también. Explica lo importante, ve al grano.

"Tanto el rail como los paneles tienen fondo blanco y sombra lateral, con el azul \texttt{\#1a73e8} como color de acento, coherente con los marcadores y las rutas del mapa."

>Esto quizá excesivo, y lo de coherente con los marcadores y las rutas del mapa ni es verdad ni es necesario. De nuevo, ve al grano

"Los paneles disponibles se gestionan mediante un único estado (\texttt{activePanel}) con comportamiento de alternancia: pulsar el botón de un panel ya activo lo cierra."

>Dos puntos ":" excesivos, lo de "alternancia" suena raro en castellano, no entiendo los paneles "disponibles", ¿por qué disponibles? Mucho rollo. También explicar bien los estados, esta parrafrada ponerla mejor.

"El panel activo al cargar la aplicación es \textbf{Inicio}, que presenta el proyecto con tabla de créditos y lista de tecnologías. Los restantes son \textbf{Rutas} (origen/destino, tabla de modos, cálculo OSRM y navegación OTP), \textbf{Red GTFS} (buscador de línea, acordeón con diagrama de paradas y tabla de horarios), \textbf{Predicción IA} (perfiles predefinidos, formulario sociodemográfico, inferencia modal y comparación de modelos) y \textbf{Ajustes} (selector de modelo activo, visibilidad de paradas y documentación para modelos personalizados). El selector de capa base, con las seis opciones descritas en la sección~\ref{subsec:impl_frontend_mapa}, se integra también en el rail sin abrir un panel expandido."

>Esto también ponerlo mejor, lo del panel activo entiendo que viene por la gestión del estado "activePanel" pero tal y como está ahora es confuso, si explicamos todo bien de primeras y de manera ordenada seguro que queda mejor.

>Las rutas deberían ir en una lista, no en negrita en una parrafada. Revisar el contenido total de cada panel, además te has dejado el de "Capas". Actualizate respecto al código y pon la memoria bien. El de Inicio añadir que tiene la introducción al proyecto o algo así, lo de tabla de créditos suena raro, sobretodo porque no se renderiza como tabla (aunque esté maquetado como una, no tiene bordes).

>"Los restantes" tambien suena raro, en lista ira mejor todo, en vez de así en negrita con parentesis y un monton de enumeraciones, ponlo bien anda.

>Lo de referirte a la sección 5.5.3 justo antes de que comience lo veo innecesario, además lo haces para el panel de Capas que lo has llamado "selector". Se arreglará solo cuando arregles este párrafo con mis instrucciones, asi no hay que referenciar al siguiente.

---

### 5.5.3 Interfaz cartográfica

>Esta sección debería ir antes de todos los apartados de panel de rail, y no sé si también antes de la explicación esta del diseño de la interfaz (la anterior, 5.5.2). Además esta sección es larguísima, hay que mover muchas cosas y reorientarla

>También estaría bien explicar bien como funciona Leaflet. Aquí vemos que tenemos el mapa del mundo, pero solo el extracto OSM descargado, y si pinchamos en cualesquiera puntos del mapa y calculamos la ruta solo nos mostraría la ruta que se encuentra dentro del extracto OSM (castilla la mancha), y solo los buses y paradas del GTFS (Toledo) que hemos construido junto al extracto OSM para OTP (necesita el extracto para los tramos andando). Creo que todo esto ya lo explicamos, pero por recalcartelo.

>Respecto a los controles del mapa, creo que están bien en este apartado, pero me gustaría explicarlos de manera más estructurada, actualmente esta todo en un parrafo muy compacto y no se lee bien, es larguisimo todo en este apartado. Vamos a separar bien, podemos aprovechar el uso de listas para los controles...

"El usuario fija los puntos de origen y destino mediante el menú contextual del mapa o editando sus coordenadas directamente en el panel Rutas, mecanismos que se detallan al final de esta sección."

>Esto quizá referirse más bien al apartado que haremos para el panel Rutas? Según como reestructuremos esto.

" Los marcadores se implementaron con iconos personalizados en CSS, en lugar de los predeterminados de Leaflet, para distinguir visualmente el punto de inicio del de llegada. El diseño partió de elementos base de la librería, adaptados mediante estilos propios."

>Revisar si son iconos personalizados CSS, o si es un SVG o algo, y ponerlo bien. Quizá explicar mejor lo de El diseño partió de elementos base e la librería, aunque veo bien el párrafo a grandes rasgos excepto por esa duda sobre si son CSS puro, SVGs a fuego, iconos ya existentes modificados con CSS u otras herramientas... O si convendría hacer uno nosotros y ponerlo como archivo incluso para que no esté a fuego en código. Ya me dices.

"Las rutas viarias calculadas por OSRM se representan como polilíneas coloreadas según el modo: azul para conducción, verde para bicicleta y gris para desplazamiento a pie. Cuando el usuario solicita los tres perfiles simultáneamente, los tres trazados se superponen sobre el mismo mapa, lo que permite comparar visualmente los recorridos y apreciar las diferencias de trayecto entre modos."

>Esto yo creo que va mejor en el nuevo apartado de "Rutas OSRM/OTP" como te he dicho antes. Cuidado con el "lo que permite comparar"..., es de nuevo repetitivo y muy de LLM.

>Lo de "el usuario solicita los tres perfiles simultáneamente", entiendo que te refieres a lo de Shift+Click para mostrar varias rutas a la vez, que es muy util para el analista y tambien sirvio para generar las figuras de la memoria. Pues realmente son 4 perfiles (coche, bici, andando, bus). En general está muy mal estructurado esto, no decimos nada de bus OTP.

"La aplicación ofrece seis capas de fondo seleccionables. \textit{Blanco y negro} (CartoDB Positron): paleta desaturada que minimiza el ruido visual y maximiza la legibilidad de las rutas superpuestas"...

>Esto es lo que hay que hacer en su propio apartado de Capas como el resto de paneles del rail, y poner una lita bien, así es un parrafaco imposible de leer, además las expicaciones de cada capa hay que mejorarlas, son un poco inventadas algunas. Tenemos que quitar todo lo de las "seis capas de fondo seleccionables" y ponerlo en el propio apartado de Capas una vez ya esté explicado el mapa con anterioridad y todo.

"El nivel de zoom se ajusta en escalones de 0,25 mediante la propiedad \texttt{zoomSnap=0.25} del contenedor Leaflet, combinada con la velocidad estándar de rueda (\texttt{wheelPxPerZoomLevel=60}). El resultado es un zoom más granular que los pasos enteros por defecto, sin alterar la velocidad de desplazamiento."

>Lo de "escalones" queda raro. Lo del "contenedor" Leaflet es confuso, se puede confundir con Docker. "combinada con la velocidad estándar de rueda" también rarisimo, es una traduccion que has hecho ahi mal, entiendo que te refieres a la rueda del mouse, pero esta mal redactado.

>"Sin alterar la velocidad de desplazamiento" no lo entiendo, explicalo mejor. 

>Estructurar bien la explicacion de los controles, que tenga sentido el orden, usar recursos para esto...

"Este ajuste introduce un efecto lateral: cuando el zoom activo es no entero y el usuario cambia de capa base, algunos servidores de teselas no atienden el nivel fraccionario y devuelven errores de carga hasta el siguiente redondeado. El componente auxiliar \texttt{BasemapZoomSnapper}, montado dentro de \texttt{MapContainer}, detecta el cambio de capa y ajusta el zoom al entero más próximo sin animación antes de que el nuevo proveedor comience a servir imágenes."

>Todo mal en este párrafo, de hecho igual no hace falta ni comentarlo, o al menos ponerlo más simple. Lo de servidores de teselas no se entiende, son terminos nunca usados, y creo que es un poco extenso y pesado este párrafo. Podemos poner algo sencillo cuando mencionamos que el Zoom se ha hecho por tramos de 0.25 para suavizarlo y dar más precisión, pero no enrollarnos mucho con esto. Me da la sensación de que al ser de lo más reciente te has explayado demasiado, cuadno es un detalle de codigo que bueno, igual no merece la pena enrollarse con ello.

"Los controles de navegación del mapa se implementaron como componentes React propios, reemplazando los botones predeterminados de Leaflet (\texttt{zoomControl={false}} en \texttt{MapContainer}) para garantizar coherencia visual con el resto de la interfaz y mejorar la accesibilidad en dispositivos táctiles. Los controles se dividen en dos grupos posicionados como capas fijas sobre el mapa. En la esquina inferior derecha se sitúan los botones de acercar y alejar más, bajo ellos en un bloque separado, el botón de centrar la vista, que restablece el centro de Toledo y el nivel de zoom inicial."

>No me gusta el "para GARANTIZAR coherencia visual con el resto de la interfaz", y lo de mejorar la accesibilidad por la cara. Simplemente para tneer más control y que sea más bonito, y que sea mas coherente o siga el estilo pero lo de "GARANTIZAR" no me gusta.

"En la esquina superior derecha se coloca una barra horizontal con tres botones de limpieza: el primero elimina las rutas de navegación calculadas por OSRM y OTP, el segundo descarta la línea de bus seleccionada en el panel Red GTFS y el tercero combina ambas acciones y restablece además los puntos de origen y destino a sus posiciones iniciales. Los botones de limpieza se deshabilitan automáticamente cuando no hay datos que eliminar."

>Cuidado con el uso de dos puntos ":", aunue no está mal del todo aquí. Lo de "que restablece el centro de Toledo" está mal redactado. Me gustaría más estructurado esto, quizá para todos los controles necesitamos una sección aparte de la interfaz cartográfica?

" El acceso a la instancia de mapa desde botones situados fuera del \texttt{MapContainer} se resuelve con el componente auxiliar \texttt{MapRefCapture}: montado dentro del contenedor, captura la instancia mediante \texttt{useMap()} y la almacena en una referencia mutable que los manejadores externos pueden invocar directamente."

>Esto acaso es necesario? De nuevo dos puntos ":" innecesario, y no entiendo qué explica ni a qué se refiere, lo quitamos si no es imprescindible

"Las paradas del feed GTFS se muestran como marcadores interactivos; al hacer clic en una parada se abre un popup con el nombre, el código identificador y las líneas que pasan por ella. Al seleccionar una línea desde el popup o desde el desplegable del panel lateral, el mapa dibuja el \textit{shape} de la ruta y el panel muestra la secuencia de paradas y los horarios del día seleccionado. Al hacer clic en una parada del listado lateral, la vista se desplaza hasta ella (\texttt{flyTo} a zoom~17) y, al concluir la animación, se abre automáticamente el popup correspondiente en el mapa."

>En "las paradas del feed GTFS", mejor aclarar que son las paradas de autobús, y separar más las oraciones con puntos "." en vez de ";" en general. Cuidado con terminos como "popup" y demás del inglés, intentar traducir, o usar préstamos linguisticos con textit o como digan las normas de un TFM en castellano. También cuidado con el "shape": ¿a qué se refiere? explicar bien, o usar el término en castellano más correcto. También cuidado, porque estamos mezclando las paradas que se muestran en el mapa con lo que ocurre al pulsarlo en los paneles OSRM/OTP y GTFS del raíl, cada cosa en su sitio por favor. Es un mareo tal y como lo tenemos. En el bloque de interfaz cartográfica mostramos todas las cosas que aparecen en el mapa y luego vamos panel por panel del raíl diciendo lo que tiene cada uno y cómo interactua con el mapa.


"El mecanismo se implementa con dos estados coordinados: \texttt{flyTarget} provoca el desplazamiento y \texttt{highlightedStopId} identifica la parada a activar; un \texttt{useEffect} en \texttt{MapView} espera 900~ms tras el cambio de \texttt{highlightedStopId} (duración aproximada de la animación) y abre el popup mediante una referencia al marcador \texttt{CircleMarker} almacenada en el momento de su montaje."

>Esto o explicar mejor o quitarlo porque no se entiende nada, es super lioso, y no pega aquí, de nuevo, cada cosa en su sitio, y explicado bien, no tan compacto todo, o si no es imprescindible y son detalles muy técnicos del código, quitarlo.

"Los botones de modo de transporte no son mutuamente excluyentes: un clic normal selecciona en exclusiva el modo pulsado, mientras que un clic con \textit{Shift} añade o quita ese modo de la selección activa sin alterar los demás. El estado se modela como un \texttt{Set<UiMode>} y el componente \texttt{MapView} renderiza una polilínea por cada perfil cuyo modo esté en el conjunto activo. Las tres rutas OSRM se calculan siempre en paralelo (sección~\ref{subsec:impl_backend_osrm}), por lo que cambiar la selección de modos activos no requiere ninguna nueva petición al backend: los trazados ya están en memoria y el efecto es inmediato."

>De nuevo, uso de dos puntos ":" repetitivo al principio y al final. Y ya hablamos de esto antes con lo del Shift+Click, cada cosa en su sitio, deberiamos ponerlo en el panel de Rutas OSRM/OTP. Explicar bien todo, lo de clic con Shift está raro, mejor explicando, pulsando a la vez la tecla Shift mientras hacemos click o algo así.

"Los puntos de origen y destino se establecen mediante un menú contextual de clic derecho: al pulsar el botón secundario sobre cualquier punto del mapa, se suprime el menú nativo del navegador y se muestra un menú compacto. Su primera entrada, inspirada en Google Maps, muestra las coordenadas del punto pulsado (latitud y longitud con cinco decimales) y las copia al portapapeles al hacer clic, confirmándolo con un cambio temporal del texto a ``¡Copiado!''; las dos entradas siguientes son ``Establecer como origen'' y ``Establecer como destino''. El menú se cierra al seleccionar una opción, al pulsar \textit{Escape} o al hacer clic fuera de él. Este mecanismo reemplaza el esquema anterior de clic izquierdo alternado, que resultaba poco intuitivo cuando el usuario quería reubicar solo uno de los dos puntos.
"

>Esto no se si lo dejamos en interfaz cartográfica o se va al panel de RUTAS (gtfs/otp). Lo de "menú compacto" lo veo raro, no hace falta ese adjetivo, indicar que es un menú de click derecho, y de nuevo has usado dos puntos ":" otra vez. 

>Lo de "su primera entrada, inspirada en Google Maps" aparte de estar repetido de hace poco no hace falta decir que está inspirado, ya lo decimos antes. Y "entrada" me suena raro para el primer elemento del menú, la primera fila..., y sobreexplicado lo del cambio temporal del texto a Copiado quizña. Al pulsar "la tecla \textit{Escape}" mejor Lo de "Este mecanismo reemplazael esquema anterior..." quitalo.


"De forma complementaria, el panel Rutas permite editar las coordenadas de ambos extremos como texto, pegando un par ``latitud, longitud'' copiado de cualquier fuente. Cada campo valida el rango geográfico al confirmar, ya sea con la tecla \textit{Intro} o al perder el foco, y restaura el valor previo si el formato no es válido; mientras el campo está enfocado se suspende su sincronización con el estado del marcador para no sobrescribir lo que el usuario teclea."

>De nuevo, esto irá en su propio apartado. "De ambos extremos" no está mal, aunque quizá mejor puntos o algo. Lo de "un par latitud, longitud" queda un poco raro, y mejor poner que es pegando un par en cada punto claro. 

>Lo de "valida el rango geográfico al confirmar" no sé a que te refieres, a que comprueba si el valor introducido son coordenadas no? en ese caso lo de "ya sea con la tecla Intro o al perder el foco" sobra cmpletamente, y lo de "mientras el campo está enfocado se suspende su sincronización con el estado del marcador para no sobreescribir lo que el usuario teclea" también está explicado muy complejo, o lo simplificamos o lo quitamos, poruqe no se entiende. 

"Una vez calculadas las rutas por primera vez, cualquier modificación posterior de un extremo, provenga del menú contextual o de la edición manual, vuelve a lanzar automáticamente las peticiones a OSRM y OTP sin pulsar de nuevo el botón de cálculo. Este recálculo automático se desactiva al limpiar las rutas y permanece inactivo hasta el siguiente cálculo manual, lo que evita peticiones innecesarias antes de que el usuario haya definido un escenario completo."

>Esto está muy apelotonado y pegado a lo anterior, cuando se merece su propio párrafo. Aunque no sea muy extenso, que vayan las cosas separadas, esta todo muy junto. También mucho cuidado con la sobrejustificación, y repetimos el "lo que", es interesante esa ultima frase pero reformulala, que repetimos mucho a lo largo del documento...

"\begin{figure}[htbp]
  \centering
  \missingfigure{Captura general de la aplicación mostrando el mapa de Toledo con las tres rutas OSRM calculadas para un par origen-destino (polilíneas azul, verde y gris), el panel lateral con el formulario de perfil de usuario y el bloque de resultados de inferencia con las probabilidades para cada modo.}
  \caption{Vista general de la interfaz del simulador de movilidad urbana.}
  \label{fig:app_general}
\end{figure}"

>Esta captura habría que ponerla más arriba, y quizá que primero incluya los cuatro itinerarios, con las paradas y mostrando todo, a modo de itnroducción, ya sea en el punto de "Interfaz cartográfica" (o como lo llamemos) o en algun punto anterior del capitulo de Frontend. En general, más capturas, algunas generales, otras especificas. Primero una donde se ve una vista previa de la aplicación mostrando todo lo posible en una foto (las cuatro rutas dibujadas, paradas, con una de las 6 capas disponibles, la introducción o el panel de rutas abierto, ya sabes por donde voy), y luego seccion por seccion, rail por rail, en detalle, mostramos el mapa con las cosas de esa sección, o capturas mas centradas a los paneles, etc.

>En general, este capítulo tiene muchas cosas de interacción, algunas hay que moverlas, otras si que se quedan en la interfaz cartográfica, ordenarlo todo bien.

---

### 5.5.4 Representación de itinerarios multimodales

>Este capítulo con la nueva estructura será parte del panel de RUTAS (OTP), y seguramente algunas partes se irán al panel de RED (GTFS), y me da miedo que expliquemos aquí cosas de backend que deberian ir antes, o en arquitectura. Vamos revisando:

"Los itinerarios de transporte público devueltos por OTP tienen una estructura de tramos heterogénea: un viaje típico en autobús urbano se compone de un tramo a pie hasta la parada de embarque, uno o varios tramos en autobús y un tramo a pie final hasta el destino. Representar este itinerario como una única polilínea homogénea perdería la información sobre qué parte del recorrido se realiza en cada modo."

>De nuevo uso de dos puntos ":". innecesario. También aclarar los transbordos en lo de uno o varios tramos de autobús, la posibilidad de además tener que desplazarse de parada en parada para el posible transbordo. 

"La solución adoptada consiste en renderizar cada tramo como un trazado independiente con estilo diferenciado: los tramos a pie se representan con trazado discontinuo en tono naranja oscuro y los tramos en autobús con trazado continuo del color de la línea."

>Uso de dos puntos ":" repetitivo, y el "La solución adoptada" tambien queda un poco repetitivo. 

>Además, hay información desactualizada. Para empezar, habría que decir primero los tramos en bus (que se muestran el color naranja que hemos asignado a ese modo de transporte en el panel de Rutas), y las paradas por las que pasa se colorean del color de la línea del autobús en el que pasa por esas paradas, para que detecte rápidamente los transbordos aparte de con el panel que aparece a la izquierda. Luego, los tramos andando, que son de un color similar al de la linea mas oscuro, e intermitente, para no ser igual que el gris del modo "andando" normal, por si el usuario decide mostrar las 4 rutas a la vez, que vea lo que es andando para ir al bus y lo que es andando él.

>En cualquier caso, esto lo tenemos que poner de distinta manera en el panel de RUTAS (como he explicado arriba), y en el panel de GTFS (al pinchar una línea en el acordeón, se dibuja la linea y las paradas cogen el color de esa línea, y al pinchar una hace el zoom etc...)

" Los trazados del itinerario OTP solo se muestran cuando el modo activo en la interfaz es ``Transporte público'', evitando el solapamiento visual con las rutas viarias de OSRM cuando el usuario explora otros modos.""

>Esto es complketamente innecesario.

"Esta distinción requirió adaptar el proceso de renderización para gestionar una lista variable de geometrías con estilos distintos, en lugar del único trazado por consulta que se usa en el caso de OSRM."

>No está mal, pero aclara que te refieres a que se devuelve la línea con distintos estilos en un mismo mensaje, en vez de una simple polyline coloreada para OSRM en cada modo de transporte con su estilo propio, entiendo. Y lo de "esta distinción requirió", tanto el distinción como el requirió me suenan raro.


"Más allá del trazado sobre el mapa, el panel lateral despliega el detalle del itinerario. Se encabeza con un resumen destacado del viaje completo (hora de salida, hora de llegada y duración total) y, debajo, el desglose tramo a tramo. Los tramos a pie se resumen en una línea con su distancia y duración."

>Todo esto debería ir en el apartado del panel de RUTAS, como comento. Lo de "Se encabeza con un resumen destacado" lo veo raro.

"Cada tramo de transporte público se encabeza con la etiqueta de su línea y las horas de salida y llegada, y bajo él se dibuja un diagrama vertical con todas las paradas del recorrido, reutilizando el mismo componente que el panel Red GTFS (sección~\ref{subsec:impl_gtfs_color}): una barra vertical del color de la línea, las terminales como puntos rellenos, las paradas intermedias como aros huecos y la hora de paso junto a cada parada."

>Uso de dos puntos ":" excesivo, y aquí estamos haciendo una referencxia al panel Red GTFS pero ese capítulo se va a mover con toda la reestructuración y ahora este (panel de RUTAS) irá antes que ese (panel de RED)

"La etiqueta de cada línea debe lucir el mismo color que en el catálogo GTFS. Sin embargo, OTP identifica las líneas con un \texttt{routeId} prefijado por el identificador del feed (por ejemplo, \texttt{1:50011}), que no coincide directamente con el \texttt{route\_id} del feed estático. Para recuperar la línea correcta, una función auxiliar (\texttt{resolveGtfsRoute()}) intenta la correspondencia por identificador exacto, por identificador sin el prefijo del feed y, en último término, por nombre corto, obteniendo así el color real de la línea con el mismo criterio que el resto de la interfaz."

>No entiendo nada de aquí, y está puesto todo en una frase muy larga. Es realmente necesario? Explicame que es esto y o lo explicas mas sencillo (si se puede o lo quitamos=). Tampoco se muy bien donde deberia ir. Igual lo quitamos.

"Las paradas se dibujan sobre el mapa como marcadores circulares rellenos con el color de su línea, tanto las de la línea seleccionada en el panel Red como las del trayecto del itinerario. Como ese relleno coincide con el color del trazado sobre el que se sitúan, cada marcador lleva un contorno de contraste (blanco, o negro si el color de la línea es claro) que lo separa visualmente del trazado."

>Aquí estamos explicando lo de las paradas, pero yo creo que deberíamos en el apartado de Interfaz cartográfica (con la captura de vista previa), decir que se muestran como puntos en el mapa a partir del GTFS/stops (que ya estaría explicado de antes). Y luego, en los paneles de RUTAS y RED, ya vemos como interactúan con estos puntos en el mapa, pero es que tal y como está es un lío. Lo del contorno de contraste también depende de que panel estemos usando, así que lo movemos también y reestructuramos todo.

"Por último, las paradas representadas como marcadores circulares sobre el mapa se renderizan en una capa propia de Leaflet (\textit{pane}) con un índice de apilamiento superior al de las polilíneas. Sin esta separación, una polilínea dibujada con posterioridad podía quedar por encima de un marcador y capturar sus clics; con la capa dedicada, las paradas permanecen siempre accesibles a la interacción del usuario por encima de los trazados."

>Cuidado, expliquemos bien lo de "pane", y lo del índice de apilamiento es muy lioso, te refieres al z-order o algo?. Esto iría en lo de interfaz cartográfica junto a la presentación de los puntos de paradas de autobús, como he comentado justo antes. Está bien explicar lo que ocurre sin la separación, quiza hacerlo un poco mas sencillo. El ";" quizá innecesario, se puede reemplazar, y la ultima frase tambien "por encima de los trazados" un poco rara, además parece sobrejustificacion.

"El diagrama de paradas del itinerario es interactivo: al pulsar una parada, el mapa se desplaza hasta ella, se resalta en el diagrama y se abre su globo informativo sobre el mapa. La apertura del globo se coordina con la animación de desplazamiento mediante un temporizador, reutilizando el mismo mecanismo de referencias a marcadores que el panel de red."

>Todo esto hay que explicarlo correctamente en la sección de RUTAS (itinerario OTP) como en el panel RED (feed GTFS) segun se use en cada caso, aunque sea muy similar, podemos decir en el de rutas (que contaremos después) que se hace igual que en el "Detalle del itinerario" del panel RUTAS.

>Mucho cuidado con el uso de "globo" como "popup", por favor, usemos lo mismo en todos sitios, busca el término más correcto y que esté igual en toda la memoria. Y lo de "se coordina con la animación de desplazamiento mediante un temporizador" es rarísimo, no entiendo, es necesario? parece muy a bajo nivel. 

>Cuidado en el " reutilizando el mismo mecanismo de referencias a marcadores que el panel de red", que ahora va a ir en orde distinto y  cada cosa en su apartado según el panel.

"El globo de cada parada del trayecto muestra la línea por la que se pasa (con su color real), la hora de paso y, cuando la parada es un punto de transbordo directo (cambio de línea en la misma parada sin tramo a pie intermedio), las líneas implicadas. La condición de transbordo se detecta directamente de la estructura del itinerario: dos tramos de transporte consecutivos sin un tramo a pie entre ellos comparten la parada de bajada y de subida"

> Esto solo se aplica para el panel de RUTAS, en GTFS sale distinto el globo, así que cuidado. Y no sé si hay algo repetido también. 

---

### 5.5.5 Gestión del estado con TanStack Query

>Hay que hablar de TanStack Query, pero quizá moviendo este capítulo a después de todos los paneles, o en el ch4 (arquitectura) igual ponemos algo, si tiene suficiente peso. Lo que si habría que hacer como te he cometnado antes al principio del frontend, en el 5.5.1 "Tecnologías", quiza meter la mención a TanStack Query siguiendo las instrucciones que te puse antes. Ya me dices.  Yo pondría una mención al principio en tecnologías y explicaba esto a fondo después de todos los paneles en el ch5.

"Las peticiones al backend se gestionan con TanStack Query (\texttt{@tanstack/react-query}). Los datos GTFS estáticos (paradas, lista de rutas) se cargan con \texttt{useQuery} al arrancar la aplicación y se mantienen en caché durante la sesión. Las peticiones de rutas OSRM, itinerarios OTP e inferencia LPMC se declaran como mutaciones (\texttt{useMutation}), que se disparan manualmente al pulsar los controles de cálculo en la interfaz."

>Explicar bien el useQuery, el useMutation, etc. que no se entiende. Por lo demás la redacción no está mal del todo. Respecto a lo deq ue se mantienen en caché durante la sesión, se mantienen en la caché del cliente? O como?

"TanStack Query gestiona de forma automática los estados de carga y error, la caché y el reintento con \textit{backoff} exponencial. Las mutaciones de inferencia LPMC (\texttt{/predict}, \texttt{/compare}, \texttt{/debug-features}) se declaran de forma independiente, lo que permite invocar la predicción con el modelo activo o la comparación de los tres modelos sin afectar al estado del resto de la interfaz."

>Que es el "backoff"? Explicar bien todo eso, cuidado con el "lo que permite"... y en general, redacción muy mal aquí. "Invocar" no se si es el termino correcto. Un poco raro este párrafo.

---

### 5.5.6 Perfiles de usuario predefinidos

>Este apartado creo que debería ir en el nuevo que hagamos para el panel de IA.

"Para facilitar la exploración del simulador sin necesidad de introducir manualmente todos los parámetros sociodemográficos, se implementaron tres perfiles predefinidos que autocompletan el formulario del panel lateral:"

>Mejor empezar con "Para el analista" o algo así, explicar bien que nos referimos a los inputs del panel IA (cuando metamos todo esto en ese panel dedicado se entenderá mejor si lo hemos explicado ya antes). Añadir despues del "formulario del pnael lateral" poner " y que posteriormente se pueden editar:"

"  \item \textbf{Commuter}: viaje al trabajo (HBW) en martes a las 8:15. Varón de 36 años con carnet de conducir y un coche en el hogar."

>Revisar si llamarlo Commuter o traducirlo al español. También explicar de donde viene Commuter (del inglés, verbo para referirse al desplazamiento hacia o desde el trabajo si no me equivoco). Trabajador, que suele ir en su coche. Y poner "usuarios que viajan al trabajo (HBW, por sus siglas en inglés)" ,  usuarios que viajan por motivos de educación (HBE),  usuarios que viajan por ocio (HBO) en cada caso

"Al activar un perfil se carga el conjunto completo de valores."

>Sin modificar la ruta ni nada de eso, por aclarar, que los perfiles son para ver como responden ante la inferencia de un mismo trayecto/par origen-destino.

"El día de la semana y la hora de salida no son campos editables del formulario: se derivan del control global del viaje (sección~\ref{subsec:impl_otp_fecha}) y se muestran como información de solo lectura, de modo que la inferencia siempre emplea el mismo día y hora que los itinerarios."

>Aqui quiero meter tambien como campos no editables (solo lectura) la información del panel RUTAS OSRM/OTP (duracion de cada modo de transporte, distancia, etc.), y se entenderá mejor al ser un apartado dedicado al panel IA ya después de haber hablado del de RUTAS y RED. También cuidado con la referencia a la impl_otp_fecha, que igual cambia con esta reestructuración.

"Por coherencia, al activar un perfil se ajusta también la fecha y la hora globales al escenario que representa (por ejemplo, un día laborable a las 8:15 para el perfil \textit{Commuter}, mapeando el día de la semana a una fecha real dentro de la ventana del feed)."

>Lo de "activar un perfil" es raro, y "mapeando" no creo que esté recogido por la RAE, mucho cuidado.

"La detección de ``perfil activo'' se implementa comparando el estado actual con los valores predefinidos: el indicador visual desaparece en cuanto el usuario modifica algún campo, eliminando la ambigüedad sobre qué conjunto de valores se está usando en la inferencia. Al cargar la aplicación se aplica un perfil por defecto (\textit{Commuter}), de modo que el panel arranca con un escenario completo y coherente ya seleccionado."

>Esto está explicado muy raro, significa que se detecta si el perfil esta activo segun si todos los campos tienen los valores que le corresponden? y se desactiva en cuanto difiera alguno? y si no coinciden todos con ningun perfil no saldra ninugno selecionado? podemos ponerlo más fácil. De nuevo, no uses tanto los dos puntos ":"

>Lo de "de modo que el panel arranca con un escenario completo y coherente" suena demasiado sobrejustificación de nuevo, aunque está mejor redactado que otros casos.

"El panel se organiza para reflejar el flujo de datos hacia el modelo: primero, el par origen-destino en modo de solo lectura (que alimenta a OSRM y OTP); a continuación, la información del viaje (día y hora) y el resto de variables sociodemográficas; y, tras la inferencia, el resultado con la probabilidad de cada modo."

>Esto va de la mano de lo que te he comentado antes, que iba a meter tambien la información de las rutas OSRM/OTP (duracion, distancia...) para cada modo de transporte en solo lectura, podemos hacer el cambio en la app y ponerlo todo en un párrafo bien? Siguiendo esta línea del flujo de datos, aunque lo de "El panel se organiza" me suena raro. quizá está organizado o algo así.

"La predicción se lanza con el botón ``Inferir modo'', que muestra junto a su rótulo la variante de modelo activa. Bajo el resultado, dos acciones secundarias permiten profundizar: ``Comparar modelos'' genera una tabla con las probabilidades de los tres modelos para el mismo escenario, y ``Ver variables'' abre una ventana modal con el vector de características completo que recibe el modelo (valores crudos y escalados), útil para inspeccionar qué datos alimentan la inferencia."

>Cuidado con "variante de modelo activa". Expliquemos también bien como se muestran los resultados antes de lanzarnos con los dos botones, que aparecen una vez se ha ejecutado la inferencia con el botón de Inferir modo. También pon a qué endpoint llaman, como ya están explicados de antes, esto para todas las acciones del frontend a ser posible. También  poner esto en su propio párrafo, que está pegado a lo anterior y lo veo demasiado compacto todo para ser pasos distintos de la app... Quizá poner una lista? Con lo que hace cada botón, a qué endpoint llama, etc.

"Los tres perfiles representan escenarios típicos de elección modal con comportamientos esperados claramente diferenciados. La ausencia de carnet de conducir en el perfil de estudiante elimina prácticamente la opción \textit{drive} de la predicción, mientras que la disponibilidad de dos vehículos en el perfil familiar, combinada con el contexto de ocio en sábado, tiende a favorecer el modo \textit{drive} frente al transporte público. Estos contrastes son útiles para verificar cualitativamente que el modelo responde de forma coherente a las variables de entrada."

> Lo de "los tres perfiles... con comportamientos esperados claramente diferenciados" está redactado de manera muy compleja aposta, aunque entiendo la intención, vamos a redactarlo de otra manera.

>También cuidado, con usar "drive" etc donde podemos usar el castellano perfectamente.

>Lo de "Estos contrastes son útiles para verificar..." no esta mal pero suena a sobreexplicación de Claude/LLM, ponlo más simple

"\begin{figure}[htbp]
  \centering
  \missingfigure{Captura del panel de comparación de los tres modelos (XGBoost, Random Forest, DNN) mostrando las probabilidades de elección para los cuatro modos (walk, cycle, pt, drive) ante el mismo par origen-destino y perfil de usuario. Mostrar un caso con clara concordancia entre modelos y el modo predicho visualmente destacado.}
  \caption{Panel de comparación de probabilidades de los tres modelos de elección modal.}
  \label{fig:panel_comparacion}
\end{figure}
"

>Esto irá en el panel de IA pero tras enseñar en otra captura los inputs y el resultado de inferir modo. Tambien hara falta captura del "Ver variables" (debug-features). Para el panel de IA con esas 3 figuras vamos perfectos.

---

### 5.5.7 Panel de ajustes y modelo activo

>Antes de este panel estaría el propio de "Capas" que hemos comentado al principio que faltaba, y metemos bien todos los basemaps, con su origen, explicación, etc., y una captura del panel.

>En este apartado hay varias cosas desactualizadas, hay que contrastar con el código, y tenemos que reestructurarlo para que no sea todo un párrafo larguisimo que habla de tres cosas completamente distintas.

"El panel de ajustes agrupa tres secciones de configuración global de la sesión. La primera sincroniza la visibilidad de las paradas de bus con el interruptor del panel Red GTFS, permitiendo activarlas o desactivarlas desde cualquiera de los dos paneles."

>En el panel Red GTFS ya no está ese interruptor, solo aparece en el menú de Ajustes para configurar la visibilidad de ls paradas. Quiz´este párrafo para que no sea tan tocho podemos hacerlo en lista según las secciones del panel de ajustes o algo así. Explicar tambien como se gestiona el estado, entiendo que es solo cosa de Frontend, no hay APIs de por medio para esto.

"La segunda aloja el selector de modelo activo de inferencia: al abrir el panel por primera vez, la interfaz consulta \texttt{GET /api/lpmc/models} para obtener la lista de variantes disponibles e inicializa el selector con el valor de \texttt{default\_variant} devuelto por la API, que refleja el contenido de la variable de entorno \texttt{LPMC\_MODEL\_VARIANT}. Cada opción muestra el nombre del modelo, una descripción breve y el indicador de modelo en uso. Cambiar la selección no dispara ninguna petición: el identificador de variante elegido se adjunta como campo del cuerpo de la siguiente petición de inferencia a \texttt{POST /api/lpmc/predict}."

>El "aloja" es raro, y en general lo de "activo" es redundante. De nuevo al principio el uso de dos puntos ":", no abusemos. También explicarlo mejor porque está lioso lo que hacemos, con todo el rollo del REGEX que hemos comentado antes y demás. También cuidado con no repetir. Igual no es necesario explicar tanto de aquí? Al menos ceñirse a lo que es frontend, que más o menos está así. Al final también utilizas dos puntos ":". Es una barbaridad.

"La tercera sección contiene instrucciones colapsables para añadir modelos propios al sistema: convenio de nombres (\texttt{\{nombre\}\_lpmc.joblib} y \texttt{\{nombre\}\_lpmc\_scaler.joblib} en \texttt{lpmc/models/}), formatos admitidos (cualquier objeto sklearn con interfaz \texttt{predict\_proba}, o una red PyTorch cargable mediante \texttt{TorchModalWrapper}) y cómo configurar el modelo predeterminado. Cualquier par de ficheros que cumpla el convenio de nombres es detectado automáticamente por \texttt{GET /api/lpmc/models} sin necesidad de modificar el código ni reiniciar los contenedores."

>"Instrucciones colapsables" también suena raro. Y explicar bien las instrucciones para añadir modelos nuevos, aunque creo que deberíamos mencionarlo antes también, no sé si te lo he pedido ya en algún lado, para dejar aquí lo frontend y las explicaciones en backend, no liarnos aqui a explicar como cargar modelos

"
La Figura~\ref{fig:panel_ajustes} muestra el panel con los tres modelos incluidos en el repositorio seleccionables desde el desplegable.

\begin{figure}[htbp]
  \centering
  \missingfigure{Captura del panel Ajustes mostrando: (1) checkbox de paradas de bus, (2) selector de modelo activo con los tres modelos disponibles (XGBoost, Random Forest, DNN) y la etiqueta ``Activo'' junto al seleccionado, (3) bloque de instrucciones colapsable para añadir modelos personalizados.}
  \caption{Panel de ajustes con selector de modelo activo y documentación de extensión.}
  \label{fig:panel_ajustes}
\end{figure}"

Aquí pondré directamente una foto del panel de Ajustes al completo

---

## 5.6 Modelos de elección modal

>Aquí tendremos que reestructurar también los subapartados, explicando cada modelo en orden: Random Forest, XGBoost y DNN.

> En todo lo posible, fijate en la tesis del tutor para escribir aquí
>Hay varios temas mal de redacción y de lo que podemos poner en un TFM, como atribuyendo cosas al tutor, etc. que hay que cambiar o quitar.

"Esta sección describe el proceso de entrenamiento, validación y despliegue en producción de los tres modelos de elección modal que integra el simulador. La arquitectura del pipeline de inferencia se describe en la sección~\ref{sec:arch_pipeline_inferencia}; aquí se detalla la implementación concreta: el dataset utilizado, las decisiones de preprocesado, la configuración de los modelos y los resultados obtenidos."

> Creo que estos dos puntos ":" son excesivos de nuevo, se puede poner de otra manera. Cuidado con las referencias también si tocas algo.

### 5.6.1 Dataset LPMC y variables de entrada

"El dataset London Passenger Mode Choice (LPMC) \cite{Hillel2018LPMC,CSLPMC2019} contiene registros de viajes observados en el área metropolitana de Londres, enriquecidos con variables de nivel de servicio calculadas para cada modo de transporte disponible en cada par origen-destino."

>Aquí ponemos doble cita por algo en particular? se me renderiza en el PDF como "[Hillel et al., 2018, Hillel, 2019]", también revisar si hay alguna fuente de donde se hacen las encuestas, o si las hizo Hillel et al.

>Lo de "variables a nivel de servicio" no lo entiendo, te refieres a OSRM y OTP? Se puede poner de otra manera para que se entienda mejor? 

" Fue construido por Hillel et al.\ como banco de pruebas para la comparación de modelos de elección discreta y de aprendizaje automático en el dominio del transporte, y es la fuente de la investigación previa del tutor del TFM \cite{MartinBaos2023Thesis,MartinBaos2023TRC}. La Tabla~\ref{tab:lpmc_dataset_stats} resume sus características principales."

>Fue construido completamente por Hillel et al.? Y hay qeu poner "Hillel et al."? o el nombre completo del autor, o la empresa/institución? También, ¿las encuestas quien las hizo? él a lo largo de los años que incluye el dataset? si es así, impresionante. Lo de "es la fuente de investigación previa del tutor del TFM" queda fatal, quitalo, o se menciona de otra manera, pero no creo que sea correcto.

"El interés metodológico del dataset para este TFM no reside en el caso geográfico concreto (Londres), sino en que dispone de variables de nivel de servicio equivalentes a las que OSRM y OTP pueden calcular para cualquier par origen-destino, incluye variables sociodemográficas similares a las recogidas por encuestas de movilidad estándar, y tiene un tamaño suficiente para entrenar modelos de aprendizaje automático con validación cruzada robusta."

>Cuidado tambien con los "dispone" e "incluye". 

>"similares a las recogidas por encuestas de movilidad estándar", tiene sentido? De donde sale eso? No está mal del todo pero lo veo raro, parece como generico. También aparte del tamaño suficiente, poner que ya se ha probado para un fin similar con estos modelos (Martín Baos 2023) o algo así.

"Las variables de entrada al modelo se dividen en dos grupos. El primero comprende las variables de ruta, derivadas automáticamente de OSRM y OTP para cada par origen-destino consultado en el simulador. El segundo comprende las variables sociodemográficas y contextuales, introducidas por el usuario a través del panel lateral de la interfaz. La Tabla~\ref{tab:lpmc_features} describe ambos grupos con su tipo de dato y su origen."

>Este está bastante bien, al final, en lo de "introducidas por el usuario a través del panel lateral" (que es verdad), quizá poner "o autocompletadas a partir de uno de los perfiles" o algo así.

>La tabla quizá es más conveniente moverla a anexo, y referenciarla hacia el aenxo directamente. Asi ganamos una página de espacio

---

### 5.6.2 Preprocesado de datos

>Este apartado incluye todas las tareas que se realizan sobre el dataset para el entrenamiento validación e inferencia etc., y está todo descrito en un o dos párrafos larguísimos, vamos a hacerlo en lista o con negrita subsubsubapartados o algo, explicando cada paso que se realiza en orden, o agrupando bien según las tareas (Limpieza, normalización, discretización, etc.), y poner bien las variables, etc. que ahora mismo están apelotonadas.

"La estrategia de división de datos es temporal, no aleatoria. El dataset contiene tres oleadas de encuesta identificadas por \texttt{survey\_year}; las oleadas 1 y 2 forman el conjunto de entrenamiento y la oleada 3 el conjunto de test independiente. Una división aleatoria introduciría contaminación temporal: el modelo aprendería tendencias de periodos recientes y sería evaluado sobre tendencias pasadas, invirtiendo la dirección causal real. La separación temporal mide la capacidad de generalizar hacia delante en el tiempo, que es la condición de uso prevista del simulador, y es consistente con la metodología del tutor \cite{MartinBaos2023Thesis}."

>Cuidado con "test", utiliza el término en castellano más correcto para aprendizaje automático. De donde sacas lo de que "Una división aleatoria introduciría contaminación temporal"? De la tesis de MartinBaos? Si es así vale, pero quita los dos puntos ":" de nuevo excesivos (a no ser que él lo pusiera así, en ese caso déjalos). La cita no se si es desde la contaminación, o solo desde "La separafción temporal mide la capacidad"...

>Lo de "Es consistente con la metodología del tutor" hay que quitarlo

"
Las variables continuas reciben normalización estándar (media~0, desviación típica~1) mediante \texttt{StandardScaler} de scikit-learn, aplicada a las dieciséis columnas de ruta y contextuales (\texttt{distance}, \texttt{dur\_*}, \texttt{pt\_n\_interchanges}, \texttt{age}, \texttt{car\_ownership}, \texttt{day\_of\_week}, \texttt{start\_time\_linear}, \texttt{cost\_transit}, \texttt{cost\_driving\_total}). Las variables binarias y las columnas \textit{one-hot} no se escalan. Los modelos de árbol (XGBoost, Random Forest) son invariantes al escalado, pero se aplica el mismo preprocesado a los tres modelos para garantizar que el pipeline de inferencia del backend sea idéntico con cualquier variante."

>Esto no se si deberia ir antes, tal y como te he dicho en lista con los pasos de normalización, y luego explicamos todos estos detalles, antes de pasar con los hiperparámetros de cada modelo (RF, XGBoost, DNN). Y confirmar si es verdad lo de que son invariantes. Cuidado con el uso de "cualquier variante", mejor cualquier modelo o algo así, como ya te he dihco a lo largo de todo este documento.

" En la validación cruzada el scaler se ajusta exclusivamente sobre el subconjunto de entrenamiento de cada fold; para el modelo final, sobre todo el conjunto de entrenamiento."

>Cada cosa en su orden, no aglutinemos todo. Esto entiendo que está bien, lo de que se ajusta exclusivamente sobr eel conjunto de entrenamiento, y para el modelo final, sobre todo el conjunto. 

" En ambos casos el mismo transformador se aplica después al conjunto de evaluación, evitando que estadísticas del conjunto de validación contaminen el proceso de normalización."

La última frase no la entiendo, explicamela mejor, y no sobrejustifiques


---

### 5.6.3 Ajuste de hiperparámetros

>Este es el apartado que digo que igual tenemos que reestructurar, para que aquí hablemos modelo por modelo (RF, XGBoost, DNN) de las características de cada uno, los hipereparámetros, Revisar si lo tenemos igual que el tutor también a ser posible. Ya hemos comentado que los 3 modelos (y cualquiera) pasa por el mismo preprocesado aunque no sea necesario, por consistencia y modularidad, pero aquí si que tenemos que dividir.

"Los hiperparámetros de XGBoost proceden de una búsqueda Bayesiana con 1.000 evaluaciones realizada en la investigación previa del tutor \cite{MartinBaos2023Thesis} mediante la librería HyperOpt con el estimador de Parzen estructurado en árbol (TPE, \textit{Tree-structured Parzen Estimator})."

>Aquí cuidado, deberíamos decir primero que hemos hecho nosotros una búsqueda de hiperparámetros en tiempo razonable, ya sea a modo de baseline o lo que sea, para tenerlo nosotros para cada modelo (podemos medio inventarnoslo, y luego corrijo esos valores, como son solo informativos...), pero que luego comparamos con la del tutor (las 1000 evaluaciones, etc.) y como la suya se ejecutó con mucho más tiempo, planificación y recursos, usamos directamente esos que arrojan mejores resultados y ya han probado ser eficaces en su trabajo. Nosotros hacemos una búsqueda simple, y luego explicamos lo que ha hecho el tutor basandonos en su tesis, explicando bien HyperOpt, Parzen, etc. No es realista que esa superconfiguracion de hiperparametros la haya conseguido yo.


"A diferencia de la búsqueda en rejilla, que evalúa exhaustivamente el producto cartesiano del espacio de parámetros, y de la búsqueda aleatoria, que muestrea sin considerar los resultados previos, TPE construye un modelo probabilístico del espacio de hiperparámetros y dirige las siguientes evaluaciones hacia las regiones que han producido los mejores resultados anteriores, logrando una convergencia más rápida."

>Cuidado con los terminos "rejilla" "busqueda aleatoria, producto cartesiano, etc. Creo que son los términos matemáticos correctos en castellano pero por estar seguros. También explicar todo esto mejor, y en su parafo separado, que queda todo apelotonado.

"Los parámetros resultantes se recogen en la Tabla~\ref{tab:xgb_params}.

\begin{table}[htbp]
  \caption{Hiperparámetros del modelo XGBoost seleccionados mediante búsqueda Bayesiana (1.000 evaluaciones TPE).}
  \label{tab:xgb_params}
  \centering
  \begin{tabular}{ll}
    \toprule
    \textbf{Parámetro} & \textbf{Valor} \\
    \midrule
    \texttt{n\_estimators}      & 4.809 \\
    \texttt{learning\_rate}     & 0,01 \\
    \texttt{max\_depth}         & 4 \\
    \texttt{min\_child\_weight} & 35 \\
    \texttt{gamma}              & 3,93 \\
    \texttt{max\_delta\_step}   & 9 \\
    \texttt{subsample}          & 0,767 \\
    \texttt{colsample\_bytree}  & 0,934 \\
    \texttt{colsample\_bylevel} & 0,651 \\
    \texttt{reg\_alpha} (L1)    & 0,048 \\
    \texttt{reg\_lambda} (L2)   & 0,037 \\
    \bottomrule
  \end{tabular}
\end{table}"

>Esta tabla hay que hacerla por cada modelo, (si tiene hiperparametros), o mostrar la configuración o lo que sea., aprovechando que va a ir separado cada apartado por modelo, con los ajustes de hiperparámetros, etc. en vez de montarlo todo en esta sercción.

"La combinación de \texttt{learning\_rate=0,01} con un número elevado de árboles (4.809) es característica de un ensamble robusto: tasas de aprendizaje bajas requieren más iteraciones para converger pero producen modelos con menor varianza. La penalización de árbol mediante \texttt{gamma=3,93} y el peso mínimo de hoja \texttt{min\_child\_weight=35} actúan como regularización estructural, evitando divisiones que no aportan ganancia suficiente y reduciendo el sobreajuste en clases minoritarias como \textit{cycle}."

>Esto entiendo que es solo referido a XGBoost, habrá que explicarlo bien en su propio apartado y de manera más estructurada (lista si hace falta). Cuidado con los dos puntos ":" de nuevo repetitivos. Tienes fuente para estas conclusiones? o te las sacas de la manga?

"Para el Random Forest se emplearon los parámetros estándar de la literatura de referencia \cite{Breiman2001}: 500 árboles, profundidad ilimitada con regularización por tamaño mínimo de muestra en nodo (\texttt{min\_samples\_split=5}, \texttt{min\_samples\_leaf=2}) y \texttt{max\_features=sqrt}, que es el valor recomendado por Breiman para clasificación. La profundidad ilimitada favorece la capacidad del ensemble, mientras que los parámetros de hoja evitan que los árboles individuales memoricen grupos de hogares muy pequeños."

>Esto irá en su propia sección de RandomForest. Cuidado con el "emplearon", mejor utilizaron, etc. También "los parámetros estándar de la literatura de referencia", eso de donde sale? Breiman es fuente nuestra? O del tutor? En cualqueir caso, hay que hacer lo mismo que con XGBoost, que primero montamos una nosotros y luego cogimos los parámetros del tutor.

>"tamaño mínimo de muestra en nodo" entienod que es correcto pero suena raro, hay alguna traduccion oficial mejor para eseparáemtro? o lo hacemos más explicativo, y lo de "recomendado por Breiman" de nuevo cuidado.

>No sé si "es el valor recomendado" es la palabra correcta en ese caso de max_features=sqrt, quizá la "opción recomendada". Aún así no me fio yo mucho de esa fuente que has referenciado, explicame bien, convenceme si es correcto.

>Lo de "grupos de hogares muy pequeños" tampoco lo entiendo, explica bien, y pon las fuentes en el apartado que haremos para RFF

"La arquitectura de la DNN se fijó con tres bloques ocultos de 128, 64 y 32 neuronas, respectivamente, con BatchNorm y ReLU en cada bloque, y Dropout de 0,3 y 0,2 en los dos primeros. La normalización por lotes se sitúa después de la capa lineal y antes de la activación, normalizando las preactivaciones: esto estabiliza la escala de los gradientes en capas profundas y hace que la superficie de pérdida sea más suave durante el entrenamiento. El optimizador es Adam con tasa de aprendizaje inicial $10^{-3}$ y regularización L2 implícita (\texttt{weight\_decay}~$= 10^{-3}$). La función de pérdida es entropía cruzada con suavizado de etiquetas (\texttt{label\_smoothing=0,1}), que evita que el modelo maximice los logits indefinidamente y mejora la calibración de las probabilidades de salida. El entrenamiento emplea reducción de tasa de aprendizaje por meseta (\texttt{ReduceLROnPlateau}, factor~0,5, paciencia 5~épocas), recorte de gradientes (\texttt{clip\_grad\_norm=1,0}) y parada anticipada con paciencia de 10~épocas."

>Esto debería ir explicado aquí? O en arquitectura? En cualquier caso convendría hacer un diagrama de la red neuronal empleada, ya me dices tú donde lo ponemos. Apuntado como /TODO. No sé si aquí, me suena que hemos dicho algo en el ch4, pero bueno, lo correcto es desarrollar aquí. Me lo tendrás que explicar muy bien tambien porque no entiendo mucho de redes neuronales, aunque mas o menos se lo que dices con las capas que colocas, pero no se lo que hacen ni tengo mucha base de redes neuronales, asi que todo bien masticado. Quizá estos parámetros mejor ponerlos en una lista o tabla como el XGboost, en su apartado en concreto. Lo de "entropía cruzada con suavizado de etiquetas" creo que el término es correcto, pero revisar por si hay algo mejor para machine learning. Lo de "calibración" no se si está mal, me suena raro igual hay otro termino mas sencillo pero si es terminología de redes neuronales lo hacemos así. También lo de "parada anticipada con paciencia", no sé si "paciencia" es terminología correcta de nuevo. 

" Se fijó la semilla aleatoria 481516 en PyTorch y NumPy para reproducibilidad."

>Cuidado que esto no esté repetido, debería ir en arquitectura quizá, al principo del todo? Usamos esa semilla para cualqueir cosa random

---

### 5.6.4 Entrenamiento y evaluación

>Este capítulo no sé si haría falta desglosarlo. Si los 3 modelos han pasado por el mismo proceso de entrenamiento y evaluación, lo podemos dejar así. Te pongo algunos comentarios para rematarlo

"Los tres modelos se entrenaron con validación cruzada de 5~folds agrupada por hogar (\texttt{GroupKFold} de scikit-learn con \texttt{household\_id} como criterio de agrupación)."

>Entiendo que "folds" es el termino corecto, pero cuidado, y lo de "agrupada por hogar" es correcto pero no se si hay algun termino mejor.

"Esta estrategia garantiza que todos los viajes de un mismo hogar caen íntegramente en el mismo fold: si viajes del mismo hogar aparecieran en conjuntos de entrenamiento y validación simultáneamente, las variables sociodemográficas compartidas (\texttt{age}, \texttt{car\_ownership}, \texttt{driving\_license}) actuarían como identificadores indirectos del hogar y producirían una estimación optimista del error de generalización. "

>Aqui hay mucho fallo de LLM. El "garantiza" sobra, aunque la explicación está bien. De nuevo, los dos puntos ":" hay que quitarlos. "AGE" es una variable sociodemográfica compartida? entiendo que cada uno tiene su edad y puedes inferir la relacion familiar entre ellos, pero revisa si es correcto. Y también, si tienes fuente de esto (la tesis del tutor, o algo de lo que ya usamos, o algo nuevo) ponla. También (aunque creo que es lo que dices), mencionar que sobreajustaría a tendencias del hogar. Lo de "una estimación optimista del error de generalización" no se entiende. Mencionar palabras clave de Machine Learning como sobreajuste, data leakage, etc.

" Con la agrupación por hogar, la validación cruzada aproxima un escenario de \textit{leave-one-household-out}, más realista respecto a la aplicación del modelo sobre hogares no vistos."

>Lo de leave-one-household-out tambien me lo tienes que explicar, entiendo que te refieres a que dejamos siempre a un miembro de la familia fuera del fold minimo, y lo de "más realista respecto a la aplicación del modelo sobre hogares no vistos" no lo entiendo en absoluto. Tienes fuentes de esto? Es del tutor?

"Las métricas de la Tabla~\ref{tab:lpmc_train_results} son la media de los cinco folds."

>Esto lo pones aquí pero la tabla está mas adelante, cuidado con el orden. Además hay que explicar antes las métricas de evaluación. Tambien poner " se han reportado usando la media de los cinco folds." o algo así


"Además de la exactitud (\textit{accuracy}), se emplea el GMPCA (\textit{Geometric Mean Probability of Correct Alternative}) como métrica complementaria de calibración. El GMPCA se define como:

\begin{equation}
  \label{eq:gmpca}
  \text{GMPCA} = \exp\!\left(\frac{1}{N}\sum_{i=1}^{N} \ln \hat{p}(y_i)\right) = \exp(-H)
\end{equation}"

>Hay que explicar más las métricas de evaluación, poner la formula de cada una, accuracy, entropía, y todo lo necesario para calcular el GMPCA, usar más las formulas.

"donde $N$ es el número de observaciones, $y_i$ la clase real del viaje $i$, $\hat{p}(y_i)$ la probabilidad asignada por el modelo a esa clase y $H$ la entropía cruzada media. Un clasificador que asigna probabilidad uniforme sobre las cuatro clases obtendría GMPCA~=~0,25; un clasificador perfecto obtendría GMPCA~=~1,0. La métrica penaliza más severamente las predicciones confiadas e incorrectas que la exactitud pura, lo que la hace más informativa sobre la calibración de las probabilidades: es la métrica estándar de comparación en la literatura de elección modal con aprendizaje automático \cite{MartinBaos2023TRC}."


>No está mal, quizá poner la explicación de cada parámetro de las fórmuals de otra manera, no se si en lista o en la propia equation se pueden poner, y explicar mejor cada elemento de la ecuación. me gusta la explicación de un clasificador que asigna probabilidad uniforme, 0.25, 1.0, etc. Revisar en la tesis y en la literatura de GMPCA si esto es así o nos lo hemos inventado.

>Explicar mejor lo de "predicciones confiadas e incorrectas que la exactitud pura, con el tema de falsos positivos, aciertos, etc. (precission, acuracy, todas esas cosas de machine learning). Cuidado con el "lo que", y la "calibración" de probabilidades, que suena raro. También los dos puntos ".", y la frase de la literatura basandote en el tutor sobra completamente.

>El tutor me dice dejarlo como " es la métrica más recomendada para la comparación en la literatura de elección modal con aprendizaje automático \cite{MartinBaos2023TRC}"

"Las Tablas~\ref{tab:lpmc_train_results} y~\ref{tab:lpmc_test_results} muestran que los tres modelos alcanzan un rendimiento muy similar, con XGBoost ligeramente por delante en ambas métricas. La brecha entre validación cruzada y test es inferior a un punto porcentual en todos los modelos, lo que indica que el split temporal no introduce diferencias de distribución apreciables entre oleadas del dataset."

>Lo del rendimiento muy similar es cierto, pero en teoría. En la práctica, tras aplicar las penalizaciones y el conocimiento experto de escenarios reales del simulador, el que mejor responde a nuestros cambios y más fiable y representativo es el de XGBoost.

>La "brecha entre validación y test"... revisa si es inventado, pero lo de "un punto porcentual" suena raro, aunue es correcto. No se si hay otra menera de referirnos a ese 1%

>"LO QUE INDICA" de nuevo repetido, y que el splittemporal no introduce diferencias de distribución apreciables entre oleadas del dataset suena a sobrejustificación, o mira si tenemos fuente para eso. No está mal, pero no se puede poner con "lo que indica".

"El GMPCA en torno al 50--52\,\% supone aproximadamente el doble del clasificador aleatorio sobre cuatro clases (25\,\%), resultado coherente con los obtenidos en investigaciones previas sobre el mismo dataset \cite{MartinBaos2023TRC}. XGBoost registra la mayor GMPCA en test (51,63\,\%), lo que indica una ligera ventaja en calibración de probabilidades además de en exactitud; por este motivo se adoptó como variante predeterminada del simulador."

>Cuidado con mencionar alt utor de nuevo, "resultado coherente" con los obtenidos en ivnestigaciones previas sobre el mismo dataset. No está mal, pero confirma que lo tiene así. 

>También, veo que te refieres aquí a "la mayor GMPCA", cuando justo antes dices "el GMPCA en torno al 50-52%". Hay que poonerlo en masculino, y ponemos mejor "XGBoost registra el mayor valor GMPCA en test (51,63\,\%)".

>De nuevo, repites "calibración de probabilidades", ten cuidado, ponlo mejor o busca un término común para todas las veces que aparece, o varía un poco. Y cuidado de nuevo con "variante". Además la frase entera de "por este motivo se adoptó como vairante predeterminada del simulador" queda raro, habria que decir directamente que por todas estas razones (tanto la teoría como la práctica, mejor respuesta a penalización, etc.) se escogió XGBoost como modelo principal.

"Durante el desarrollo se detectaron tres errores con impacto significativo en los resultados. El primero fue la inclusión de \texttt{household\_id} como variable de entrada en versiones tempranas: al ser un identificador único por hogar, el modelo memorizaba el comportamiento de hogares concretos en lugar de generalizar a sus características sociodemográficas, produciendo métricas infladas en validación. La solución fue excluirlo completamente de las \textit{features} y reservarlo únicamente como criterio de agrupación para \texttt{GroupKFold}. El segundo error fue una inconsistencia de unidades: OSRM y OTP devuelven duraciones en segundos, mientras que el dataset LPMC las expresa en horas. Sin la conversión, las duraciones llegaban al modelo 3.600 veces infladas, lo que producía predicciones incorrectas que no podían diagnosticarse examinando únicamente las métricas de entrenamiento; el error se detectó al comparar predicciones del simulador con expectativas cualitativas sobre trayectos conocidos en Toledo. El tercer error, específico de la DNN, fue la colocación del BatchNorm antes de la capa lineal en una versión intermedia, en lugar de después: el efecto era inestabilidad en el entrenamiento y convergencia errática entre folds. La secuencia correcta (Linear $\to$ BatchNorm $\to$ ReLU) normaliza las preactivaciones, no las activaciones de la capa anterior, lo que proporciona un rango de entrada más estable a la función de activación."

>Este párrafo directamente igual no hace ni falta, aunque no viene mal. Cuidado que no repitamos mucho con secciones anteriores. Te pongo también algunas frases raras o comentarios.

> "se detectaron tres errores con impacto significativo en los resultados" Queda un poco raro, dilo mas simple

>"versiones tempranas" tambien raro, mejor al principio del desarrollo o algo así

>"el modelo memorizaba el comportamiento de hogares concretos en lugar de generalizar a sus características sociodemográficas, produciendo métricas infladas en validación." esto revisa, aunque creo que está bien.

>Al final fue un fallo que tuve al principio y no me di cuenta, igual quelas otras dos tonterías, pequeños erroes que no sé si hace falta mencionar, aunque está bien así en un párrafo, revisar redacción.

>Cuidado con los "lo que", y cosas similares, los dos puntos ":" al final...

>"Con expectativas cualitativas sobre trayectos conocidos de Toledo" sobra muchísimo, es mucho mas simple que eso, probando distintas rutas o algunos trayectos comunes de la ciudad se fueron descubriendo con el propio simulador cosas a solucionar, pero no te enrolles tanto, es muy fallo de LLM eso.

>"El efecto era inestabilidad en el entrenamiento y convergencia errática entre folds" también queda raro.

>"normaliza las preactivaciones, no las activaciones de la capa anterior, lo que proporciona un rango de entrada más estable a la función de activación" Esto me lo tienes que explciar mejor, o pònerlo más simple.

>EN CAUQLUEIR CASO, EL TUTOR ME HA DICHO QUE LO PODEMOS QUITAR, y decirlo en elt urno de preguntas de la defensa si me dicen algo sobre problemas que he encontrado

"Estos resultados conviene enmarcarlos en una limitación de fondo de los modelos de elección modal, tanto los clásicos de elección discreta como los de aprendizaje automático. Todos ellos maximizan una utilidad y asumen un comportamiento racional del viajero, pero las decisiones reales incorporan un componente de ruido irreducible: por debajo de cierto umbral no es realista esperar una probabilidad exactamente nula para un modo, por lo que un valor residual del orden del 1\,\% no debe leerse como un error del modelo. Por otra parte, todo modelo de aprendizaje automático pierde fiabilidad al extrapolar fuera del rango de datos con el que se entrenó; el dataset LPMC, por ejemplo, apenas contiene trayectos muy cortos, en los que el modelo tiende a preferir el coche aunque a pie se tarde menos. En estas regiones poco cubiertas por los datos resulta útil inyectar conocimiento experto que corrija el comportamiento sin modificar el modelo: la penalización del transporte público cuando no hay servicio y el recargo de tiempo de aparcamiento que el backend suma al coche en trayectos muy cortos (sección~\ref{subsec:impl_backend_penalizacion}) son ejemplos de este enfoque, que ajusta las entradas a partir de criterio experto allí donde los datos no bastan."

>Cuidado con la redacción de la primera frase. Este bloque habría que desarrollarlo un poco más, y moverlo donde corresponda (conocimiento experto, modificaciones, penalizaciones, etc.) o aquí al final tal y como está o en conclusiones... donde tu me digas. Tambien saber que te refieres al 1% ese cuando hemos metido injerencia no? por lo de trayectos cortos? o a  que te refieres. Es que creo que esto es unos copypastes que te pasé yo de lo que me dijo el tutor que me lo apunté rápido conforme me hablaba y los has pegado casi tal cual a mis notas, y no está bien hilado. Tampoco pasa nada si no lo ponemos aquí, puede ir en conclusiones o directamente no lo ponemos.

>El "apenas" tambien suena unpoco raro, y no esta bien hilado con esta frase "en los que el modelo tiende a preferir el coche aunque a pie se tarde menos". A continuaciónd eicmos lo del concoimento experto, quizá reorganizar un pcoo mejor esto, y estamos diciendo muchas cosas a la vez. Además, uso de dos puntos ":". Cuidado también con esa /ref por si cambia o estamos repitiendo mucho. 

>"a partir de criterio experto allí donde los datos no bastan", no me disgusta, pero igual se puede conjugar de otra manera para que no suene tan poético.

"Un resultado adicional de interés se obtuvo al estudiar el comportamiento de los tres modelos ante la penalización de itinerarios sin transporte público (sección~\ref{subsec:impl_backend_penalizacion}), que lleva las características de transporte público al extremo de su distribución (cinco desviaciones típicas por encima de la media). XGBoost responde como se espera y reduce la probabilidad del transporte público a un valor prácticamente nulo. Los modelos de árbol presentan, además, un comportamiento acotado ante valores extremos: una entrada fuera de rango cae en la hoja más extrema del árbol, cuya predicción está determinada por los ejemplos de entrenamiento que la poblaron, de modo que el resultado nunca se dispara. La red neuronal, en cambio, no está acotada: ante entradas alejadas de la distribución de entrenamiento puede extrapolar de forma no controlada y concentrar casi toda la probabilidad en un único modo. Conviene matizar que la literatura atribuye a las redes neuronales una capacidad de extrapolación más flexible que la de los modelos de árbol~\cite{Goodfellow2016}, pero esa flexibilidad no garantiza que la extrapolación sea acertada en un caso concreto. En el contexto del simulador, la variante XGBoost es la más adecuada para el despliegue, ya que gestiona correctamente los casos límite sin intervención posterior a la inferencia."

>La primera frase suena muy raro, como en pasiva, y demasiado impactrante nada mas empezar, organiza mejor. Lo de "que lleva las características de transporte público al extremo de su distribución (cinco desviaciones típicas por encima de la media)" tambien suena un poco bestia, auque está correcto, pero no repitamos mucho con antes.

>El "además" de "Los modelos de árbol presentan, además, un comportamiento acotado ante valores extremos:" igual es innecesario. Esto igual lo ponemos en párrafos separados por cada modelo, según como reestructuremos esto.

>El "que la poblaron" tambien usena raro, y lo de que el resutlado "nunca se dispara" no lo entiendo, is estamos en RF donde como poco se queda en 16% o asi (no llega a 0%). Cuidado con los ";", usa . para no alargar tanto las frases. 

>Cuidado con "variatne" y lo de "sin intervención posterior a la inferencia" no se si habria que decirlo porque no lo hacemos con ninguno.

