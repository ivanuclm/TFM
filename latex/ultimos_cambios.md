>Hay que revisar todos los "<<" ">>" y usar las comillas de LaTeX ``''

"En cuanto a la transferencia, cada descarga completa consume esos 0,64~GiB; para el número de evaluadores previsto (del orden de ocho), el consumo mensual rondaría los 5~GiB, aún dentro del margen gratuito. Incluir el modelo, por tanto, no supone coste alguno y evita que quien clone el repositorio tenga que reentrenarlo. Si en el futuro el número de descargas creciera hasta comprometer la cuota, la alternativa natural sería distribuir los modelos como \textit{release assets}, que no computan en la cuota de LFS."

>Hay que revisar lo del número de evaluadors previsto (del orden de ocho), y ponerlo más simple sin especificar cuantos son, y simplmenete cuantos clonados podemos. También explicar como alternativa el pagar el uso. Además pusimos una budget rule en GitHub para que como maximo pueda cobrar 5 euros en total, que da muhciismo mnargen porque cada clone seria cuestion de centimos, o fraccion de centimos. Revisa eso ahi.

"El sistema está pensado para ejecutarse sin cambios en cualquier máquina, con independencia del sistema operativo. Dos decisiones lo hacen posible: la resolución de rutas y la elección de puertos.

En cuanto a las rutas, ningún módulo codifica rutas absolutas del disco, que dependerían del equipo concreto. Cada módulo deriva las rutas que necesita a partir de su propia ubicación mediante la biblioteca estándar \texttt{pathlib}, que abstrae el separador de directorios de cada sistema (la barra invertida de Windows frente a la barra de Linux). Por ejemplo, el módulo de inferencia asciende desde su propio fichero hasta la raíz del repositorio y, desde ahí, compone la ruta al directorio de modelos; el mismo código funciona en el entorno de desarrollo (Windows) y en el contenedor de ejecución (Linux), sin puntos de montaje fijos.

En cuanto a los puertos, cada contenedor OSRM escucha internamente en el 5000, y el backend se comunica con ellos por nombre de servicio dentro de la red interna de Docker. Hacia el anfitrión, en cambio, cada instancia se publica en un puerto distinto (5001, 5002 y 5003 para conducción, bicicleta y a pie, respectivamente) para poder verificarlas por separado. Se evita publicar en el 5000 del anfitrión porque es un puerto reutilizado por servicios habituales, entre ellos el receptor AirPlay de macOS, lo que provocaría conflictos en algunos equipos. Esta publicación de puertos es solo una comodidad de depuración: en funcionamiento normal, el backend es el único que habla con OSRM y OTP, siempre por la red interna.
"

>El en cuanto a las rutas, en cuanto a los puertos, queda muy repetitovo. Busca otra estructura. Ten cuidado tambien con el "Dos decisiones lo hacen posible: la resolución de rutas y la elección de puertos."

"El router \texttt{/api/osrm} recibe un par origen-destino con la lista de perfiles solicitados, consulta en paralelo las instancias OSRM correspondientes mediante \texttt{asyncio.gather} y devuelve al frontend las rutas con distancia, duración y geometría decodificada para su representación cartográfica.

El router \texttt{/api/otp} consulta OpenTripPlanner para obtener itinerarios de transporte público y gestiona la paginación entre las alternativas devueltas, hasta cinco por consulta. La respuesta incluye el desglose por tramos, con tipo de modo de transporte, geometría, paradas de inicio y fin, y agencia operadora cuando el tramo es en autobús. Los itinerarios se ordenan por duración; se selecciona automáticamente el primero que incluya al menos un tramo en autobús y, si ninguno lo incluye, el de menor duración total.

El router \texttt{/api/gtfs} expone la información estática de la red de autobús a partir del feed GTFS cargado en memoria: listado de paradas con sus líneas asociadas, listado de líneas con sus sentidos, detalle de una línea con sus paradas ordenadas y trazado, y horarios por fecha. Estos datos son independientes de OpenTripPlanner, de modo que la red puede consultarse aunque el planificador no esté disponible.

El router \texttt{/api/lpmc} recibe las coordenadas de origen y destino junto con el perfil sociodemográfico del viajero, construye el vector de características consultando OSRM y OTP internamente, aplica el escalado y ejecuta la inferencia con el modelo activo. El endpoint \texttt{/compare} ejecuta los tres modelos de forma secuencial sobre el mismo escenario y devuelve sus probabilidades para cada modo de transporte; la ejecución secuencial evita comprometer el rendimiento de la CPU compartida entre contenedores."

>Cuidado con repetir tanto "el router", estructura mejor estos 4 párrafos, aunque sea solo cambiar el arranque de cada párrafo.

"de polilínea codificada~\cite{GooglePolyline}: una cadena de texto que comprime la secuencia de coordenadas de la ruta mediante diferencias relativas y codificación Base64,"

>A qué te refieres con "mediante diferencias relativas"?

"
La Figura~\ref{fig:osrm_rutas} muestra las tres rutas calculadas simultáneamente para el mismo par origen-destino: en azul, la ruta de conducción sigue las calles principales; en verde, la ruta de bicicleta prioriza carriles bici y calles tranquilas; en gris con trazado discontinuo, la ruta peatonal accede a zonas restringidas al tráfico rodado. Las diferencias entre los tres trazados reflejan las distintas restricciones de cada perfil sobre la red viaria de Toledo.

\begin{figure}[H]
  \centering
  \includegraphics[width=1.0\textwidth]{figs/RutasSoloOSRM.jpeg}
  \caption{Rutas OSRM para los tres perfiles de transporte sobre Toledo.}
  \label{fig:osrm_rutas}
\end{figure}
"

>Esto quizá lo muevo a frontend o lo quito para ahorrar espacio

"Esta sección cubre todo el transporte público del simulador: la elección del feed GTFS, la construcción del grafo de OpenTripPlanner (OTP) a partir de ese feed, la estructura de los ficheros GTFS y las particularidades del feed de Toledo, el periodo de validez de los datos y la integración de los itinerarios en el backend."

>Aquí redactar mejor, poner que cubre "todo lo relacionado con el transporte público" del simulador o algo así.

"El mismo feed alimenta los dos subsistemas que lo consumen: el grafo de OTP (Sección~\ref{subsec:impl_otp_grafo}) y la capa estática de horarios que expone el router GTFS (Sección~\ref{subsec:impl_backend_gtfs}), de modo que ambos comparten exactamente la misma ventana de validez. La fecha y la hora de consulta se exponen mediante un selector global en la interfaz, con un valor por defecto dentro del rango del feed (\texttt{2026-05-21}, \texttt{12:00}) y acotado al intervalo válido."

>Aquí igual podemos quitar la primera horación, y sustituirlo por "Por ello, la fecha y la hora de consulta...", porque queda repetitivo, yo creo que eso ya lo habiamos dicho lo de que aprovecha el archivo.

>Luego, el siguiente párrafo reordenarlo así (subo lo de "Se fijó la hora por defecto...")

"Se fijó la hora por defecto a las 12:00 por situarse en la franja de mayor frecuencia de
servicio y evitar el horario nocturno, donde la oferta es reducida o inexistente.. Este selector es transversal a toda la simulación: gobierna a la vez los itinerarios multimodales, los horarios de la red y el día y la hora del perfil de inferencia, evitando configuraciones inconsistentes entre las distintas vistas. La ubicación y el comportamiento de este selector en la interfaz se describen en la Sección~\ref{subsec:impl_frontend_mapa}. El backend recibe la fecha y la hora en la petición; cuando no se indican, aplica el valor por defecto.""

---

"\subsection{Integración de itinerarios en el backend}
\label{subsec:impl_otp_integracion}

El router \texttt{/api/otp} del backend consulta OTP a través del endpoint REST de planificación \texttt{/otp/routers/default/plan}, que es el punto de acceso estándar de OTP~2.x para solicitar itinerarios entre dos coordenadas. OTP devuelve hasta cinco itinerarios alternativos. El criterio de selección automática es el siguiente: se elige el primero que incluya al menos un tramo de transporte público (modo distinto de \texttt{WALK}); si ninguno cumple esta condición, se devuelve el de menor duración total. El frontend permite paginar entre las alternativas mediante los botones ``Anterior'' y ``Siguiente'', que transmiten el índice del itinerario deseado al backend, de modo que el vector de características para la inferencia se calcula siempre sobre el mismo itinerario que el usuario visualiza.

Para cada tramo del itinerario seleccionado se devuelve: modo de transporte, distancia, duración, geometría decodificada desde el formato de polilínea codificada, parada de inicio y fin, nombre de línea, agencia y horarios de salida y llegada en formato \texttt{HH:MM}. Para los tramos de transporte público se añade a la consulta el parámetro \texttt{showIntermediateStops}, que incorpora a la respuesta de OTP las paradas intermedias de cada tramo; con ellas el backend compone la secuencia ordenada completa de paradas del tramo, desde el embarque hasta el desembarque, anotando para cada una su nombre, coordenadas y hora de paso. Esta secuencia alimenta el diagrama de paradas del itinerario descrito en la Sección~\ref{subsec:impl_frontend_rutas}. La geometría de cada tramo se combina para componer la traza completa del itinerario, que el frontend renderiza diferenciando los segmentos por modo de transporte.

OTP devuelve los instantes de paso en tiempo universal (epoch UTC) acompañados del desfase horario de la agencia (\texttt{agencyTimeZoneOffset}). El backend suma ese desfase antes de formatear las horas, de modo que los itinerarios se muestran en hora local de Toledo (Europe/Madrid), con el horario de verano resuelto automáticamente según la fecha consultada."

>TODO este punto 5.2.5 tiene que irse a 5.3.3 con el Router OTP

>Cuidado con "Anterior" y "Siguiente"; no profundices tanto en cosas que son de frontend.

>El "geometría decodificada desde el formato de polilínea codificada" es confuso y repetitivo, suprimelo, reducelo, como quieras.

"Cuando OTP devuelve un itinerario compuesto exclusivamente por un tramo a pie, las características de transporte público del vector de entrada tomarían valores próximos a cero, que en el dataset caracterizan precisamente un transporte público rápido y directo. La solución adoptada, descrita en la Sección~\ref{subsec:impl_lpmc_conocimiento}, consiste en sobrescribir esas características con valores de penalización extremos que llevan al modelo a descartar el transporte público en ausencia de servicio real.

La Figura~\ref{fig:otp_itinerario} en la Sección~\ref{subsec:impl_frontend_rutas} ilustra un itinerario multimodal típico en la interfaz del simulador."

Todo esto lo quitamos, estamos repitiendo con una cosa que se explica al final, y mucho foreshadowing en general.

"La lógica de agrupación de sentidos descrita en la Sección~\ref{subsec:impl_otp_gtfs_estructura} (los 56 \texttt{route\_id} del feed de Toledo agrupados en 25 líneas por \texttt{route\_short\_name}) se aplica tanto en este router como en el frontend, de modo que el comportamiento es coherente en todo el sistema."

>Esto es redundante, lo quitamos

"Los marcadores de origen y destino se implementan con iconos SVG propios embebidos en CSS, distintos de los marcadores predeterminados de Leaflet, para distinguir visualmente el punto de inicio del de llegada. Las paradas de autobús se representan como marcadores circulares (\texttt{CircleMarker}) en una capa de renderizado propia de Leaflet (\textit{pane} \texttt{stopsPane}, z-index~450 frente a los 400 de las polilíneas). Este orden de apilamiento asegura que las paradas sean siempre accesibles a la interacción del usuario aunque un trazado las atraviese."

>Lo de "embebidos" es correcto en castellano? Podemos poner de manera más simple que los montamos nosotros con CSS

"La barra lateral de navegación (\textit{rail}) de 64~px de ancho, siempre visible a la izquierda de la pantalla, da acceso a los seis paneles funcionales del simulador. Al pulsar un botón del \textit{rail}, el panel correspondiente se despliega a su derecha; pulsar de nuevo el mismo botón lo cierra. El panel activo al arrancar la aplicación es \textbf{Inicio}. Los demás paneles son \textbf{Rutas}, \textbf{Red GTFS}, \textbf{Predicción IA}, \textbf{Capas} y \textbf{Ajustes}, descritos en las secciones siguientes."

>Molaría decir tambien cuanto ocupa el panel desplegado a lo ancho, para que se entienda en la lectura. Al ser responsive, no se si las medidas cambian o se respeta el tamaño de pantalla. Hablemos siempre en términos de una pantalla de escritorio 1920x1080

"La maquetación es adaptable (\textit{responsive}): el mapa ocupa siempre el espacio disponible y los paneles y controles se dimensionan con unidades relativas, de modo que la interfaz se ajusta a distintos tamaños de ventana y resoluciones, desde un monitor de escritorio hasta la pantalla de una tableta."

>Tableta no es el mejor término, ponemos "tablet" directamente aunque sea con cursiva, o "dispositivos móviles"

"El panel Rutas agrupa todas las funciones de navegación viaria y multimodal. Los puntos de origen y destino se establecen mediante el menú contextual (clic derecho sobre el mapa): la primera entrada muestra las coordenadas del punto pulsado con cinco decimales y las copia al portapapeles, con un cambio temporal del texto a <<¡Copiado!>> como confirmación; las dos entradas siguientes asignan el punto como origen o como destino. El mismo par de coordenadas puede editarse también directamente en los campos de texto del panel, pegando un valor «latitud, longitud» procedente de cualquier fuente; el campo valida el rango geográfico al confirmar con \textit{Intro} o al perder el foco, y restaura el valor previo si el formato no es válido."

>Esto es un lío, no hace falta explicar tanto, ni lo de "¡Copiado!", y queda un poco confuso explicar primero el menú contextual de clic derecho con tanto detalle, además eso no sería más cosa de la interfaz cartográfica? Igual lo podemos explicar antes y aquí centrarnos en el panel en sí.

"Los resultados OSRM se presentan en una tabla con una fila por modo activo, mostrando distancia y duración estimada. El itinerario OTP se muestra en una tarjeta independiente con controles de paginación para navegar entre las alternativas devueltas. El encabezado de la tarjeta resume la hora de salida, la hora de llegada y la duración total; a continuación se despliega el detalle tramo a tramo. Los tramos a pie se resumen en una línea con distancia y duración. Cada tramo en autobús se encabeza con la etiqueta coloreada de la línea y las horas de salida y llegada, y bajo él se dibuja un diagrama vertical con todas las paradas: una barra del color de la línea, extremos como puntos rellenos, paradas intermedias como aros huecos y la hora de paso junto a cada parada. Al pulsar una parada del diagrama el mapa se desplaza hasta ella y se abre su ventana emergente. Cuando el itinerario incluye transbordos directos (cambio de línea en la misma parada sin tramo a pie entre ellos), el diagrama lo indica con una etiqueta de transbordo entre los dos bloques."

>Esto queda larguísimo, reducimos por favor o lo quitamos. En general esta sección podemos sintetizar un poquito sin perder la información importante.

"El feed de Toledo contiene 56 sentidos (identificadores \texttt{route\_id} distintos) agrupados en 25 líneas por nombre corto (\texttt{route\_short\_name}). El panel organiza los contenidos en un acordeón, un listado plegable en el que cada elemento puede expandirse o contraerse de forma independiente para mostrar u ocultar su contenido. Cada entrada del nivel superior representa una línea; las líneas con más de un sentido muestran un icono de despliegue y, al expandirlas, listan los sentidos disponibles con el sentido activo resaltado. El color de cada línea sigue una paleta fija de 26 colores definida en el cliente: los nombres cortos únicos se ordenan alfabéticamente y el i-ésimo recibe \texttt{LINE\_COLORS[i~mod~26]}, con lo que las 25 líneas del feed reciben colores únicos. Una vez determinado el color, la función \texttt{isLightColor()} calcula la luminancia perceptual con la fórmula $0{,}299R + 0{,}587G + 0{,}114B$; si el resultado supera 0,9 (líneas de color claro, como la L14 en blanco), se añade un contorno negro a las etiquetas coloreadas, a los marcadores de parada y al trazado del mapa para mantener la legibilidad sobre fondo blanco."

>ERROR, ESTO ESTÁ COMPLETAMENTE DESACTUALIZADO. CUIDADO. NO USAMOS UNA PALETA FIJA CON 26 COLORES, EL FEED CONTIENE LA LISTA DE COLORES PARA CADA LÍNEA. POR SI ACASO, SE DESARROLLÓ UNA FUNCIÓN QUE SI NO ENCUENTRA LOS COLORES EN EL FEED O SE PONE UN FEED QUE NO INCLUYE COLORES, LOS GENERA DE MANERA DETERMINISTA PARA CADA LÍNEA (AGRUPACIÓN DE SENTIDOS). Luego, sea el color que sea (del feed o asignado por nosotros), se comprueban los problemas de contraste (esto lo hablamos en un párrafo separado, y tendriamos que poner la fuente de la fórmula de luminancia perceptual).

>Para que te hagas una idea, yo decía esto de la coloración determinista: "El feed GTFS de Toledo incluye en routes.txt un color por línea (campos route_color y route_text_color), que la interfaz utiliza directamente para mostrar cada línea con el color oficial del operador. Si un feed no incluye esos campos, la función routeColor() genera un color de reserva a partir del nombre corto de la línea: transforma el texto en un número entero y lo reduce módulo 360 para elegir un tono; la saturación y la luminosidad se mantienen fijas (70 % y 35 %, respectivamente) para que el color resultante tenga siempre contraste suficiente con el texto blanco superpuesto. Como un mismo nombre produce siempre el mismo número, cada línea conserva su color entre ejecuciones. El Código 5.1 recoge ambas funciones.
Listing 5.1: Color de línea: feed GTFS como fuente primaria y hash deter‐
minista como respaldo.
function hslForKey(key: string): string {
let h = 0;
f o r (let i = 0; i < key.length; i++) h = (h * 31 + key.charCodeAt
(i)) | 0;
r e t u r n `hsl(${Math.abs(h) % 360}, 70%, 35%)`;
}
function routeColor(r: { color?: string | n u l l ; short_name?: string
| n u l l ; id: string }): string {
i f (r.color) r e t u r n `#${r.color}`;
r e t u r n hslForKey(r.short_name || r.id);
}
Este criterio de color se aplica de forma homogénea en toda la interfaz: en las etiquetas de línea del catálogo y del panel de rutas, en las etiquetas de las paradas, en el diagrama de paradas y en el trazado de la línea sobre el mapa. Algunas líneas del feed de Toledo son de color blanco (por ejemplo, la L14), y parecería invisible sobre el fondo claro de los paneles y del mapa. Para evitarlo, la función isLightColor() mide cuán claro es un color a partir de sus componentes de rojo, verde y azul y, si supera un umbral cercano al blanco, le añade un contorno oscuro."

>Haz la versión mejorada en eso con todo el contexto actual, y la nueva reorganización.

"Al seleccionar una línea, el mapa dibuja su trazado como polilínea del color correspondiente y sus paradas como marcadores circulares rellenos con ese mismo color y un contorno de contraste. Los marcadores se renderizan en la capa \texttt{stopsPane} (z-index~450), por encima de las polilíneas (z-index~400), de modo que son siempre accesibles a la interacción aunque el trazado los cruce. Al pulsar una parada del listado lateral, la vista se desplaza hasta ella (\texttt{flyTo} a zoom~17) y, transcurridos 900~ms, se abre la ventana emergente de la parada. Las ventanas emergentes muestran nombre, código y las etiquetas coloreadas de las líneas que pasan por ella; al pulsar una etiqueta se selecciona ese sentido directamente en el panel."

>Aquí quitar lo de transcurridos 900ms (queda raro), o poner al terminar la animación o algo así. También igual estamos profundizando demasiaado en algunos detalles del frontend, y todo muy de seguido, por lo que queda confuso. Me parece que es lioso cómo explicamos los paneles emergentes de las paradas en cada panel, revismeos eso bien

"\begin{itemize}
  \item \textbf{Commuter} (del inglés \textit{commuter}, persona que se desplaza a diario entre su domicilio y el trabajo): viaje al trabajo (HBW, \textit{home-based work}) un martes a las 8:15. Varón de 36~años con carnet de conducir y un vehículo en el hogar."

>Lo de "del inglés commuter" es repetir la palabra literalmnete, quizá nos referimos mejor al verbo de desplazarse entre tu domicilio y el trabajo (to commute) o algo así?

"Al cargar la aplicación se aplica el perfil \textit{Commuter} por defecto, de modo que el panel arranca con un escenario completo y coherente. El indicador de perfil activo desaparece en cuanto el usuario modifica algún campo del formulario, eliminando la ambigüedad sobre qué valores se están usando. El resto de parámetros sociodemográficos (edad, género, carnet, vehículos en el hogar, motivo del viaje, tipo de combustible del vehículo, costes) se introducen en el formulario y son editables en cualquier momento. La inferencia se lanza con el botón «Inferir modo», que muestra junto a su rótulo el nombre del modelo activo. El resultado es un conjunto de probabilidades para los cuatro modos de transporte (a pie, bicicleta, transporte público y conducción), con el modo de mayor probabilidad destacado visualmente."

>"Al cargar la aplicación se aplica" queda raro, y lo de "de modo que el panel arranca con un escenario completo y coherente." es innecesario, simpelmente decir que coge ese por defecto.

>Lo de "El resto de parámetros sociodemográficos (edad, género, carnet, vehículos en el hogar, motivo del viaje, tipo de combustible del vehículo, costes) se introducen en el formulario y son editables en cualquier momento." queda como a que esos campos no se modifican al cambiar de perfil. No poner eso, simplemente decir que aunque los perfiles rellenan estos campos automáticamente, se provee la opción de modificarlos manualmente a nuestro gusto.

"La selección de capa persiste mientras el usuario navega entre los demás paneles."

>Esto es obvio, no hace falta ponerlo, lo veo redundante aunque tampoco está mal del todo.

" Un componente auxiliar (\texttt{BasemapZoomSnapper}) detecta el cambio de proveedor y redondea el nivel de zoom al entero más próximo si es fraccionario, evitando errores de carga con los servidores de teselas que no sirven niveles no enteros."

>Esto mejonr decir, que Si se cambia de capa mientras el zoom está fijado a un valor decimal (no entero), y se cambia a una capa que no admite valores decimales o lo que sea, el BasemapZoomSnapper se encarga de eso y redondea al nivel más proximo

"El panel Ajustes agrupa tres secciones de configuración global. La primera sincroniza la visibilidad de las paradas de autobús en el mapa con el interruptor del panel Red GTFS, permitiendo activarlas o desactivarlas desde cualquiera de los dos puntos de la interfaz sin inconsistencias."

>ERROR, YA NO HAY NINGUN INTERRUPTOR EN EL PANEL GTFS, ESTÁ SOLO EN AJUSTES.

"\subsection{Gestión del estado con TanStack Query}
\label{subsec:impl_frontend_query}

Las peticiones al backend se gestionan con TanStack Query (\texttt{@tanstack/react-query}). Los datos GTFS estáticos (paradas, lista de rutas) se cargan con \texttt{useQuery} al arrancar la aplicación y se mantienen en caché durante la sesión. Las peticiones de rutas OSRM, itinerarios OTP e inferencia LPMC se declaran como mutaciones (\texttt{useMutation}), que se disparan manualmente al pulsar los controles de cálculo en la interfaz.

TanStack Query gestiona de forma automática los estados de carga y error, la caché y el reintento con retroceso exponencial (cada reintento espera más que el anterior). Las tres mutaciones de inferencia LPMC (\texttt{/predict}, \texttt{/compare}, \texttt{/debug-features}) se declaran por separado, de modo que la predicción con el modelo activo y la comparación de los tres modelos se lanzan de forma independiente, sin afectar al estado del resto de la interfaz."

>ESTA SECCIÓN CREO QUE LA ELIMINAMOS ENTERA, NO APORTA NADA DE INTERÉS Y PODEMOS MENCIONARLO DE MANERA MÁS BREVE ANTES COMO YA HEMOS HECHO DENTRO DE OTROS APARTADOS. SE PUEDE DECIR LO MISMO CON MENOS.

" Se citan dos publicaciones porque corresponden a aportaciones distintas: el artículo original que presenta el dataset \cite{Hillel2018LPMC} y su descripción técnica detallada \cite{CSLPMC2019}."

>CUIDADO CON ESTA SOBREEXPLCIACIÓN QUE LA HAS PUESTO EN MEMORIA EN VEZ DE DÁRMELA A MÍ, a las malas cambiamos el nombre de las citas para que se diferencien mejor.

"El dataset es, además, el utilizado en los experimentos de referencia sobre los que se apoya este trabajo \cite{MartinBaos2023Thesis,MartinBaos2023TRC}."

>AQUÍ SIN EMBARGO HAS UTILIZADO DOBLE CITA Y NO ENTIENDO POR QUÉ, SI SERÁ LO MISMO NO? LA TESIS DE JOSE ANGEL

"Contiene también las variables sociodemográficas que el simulador pide al usuario, tiene un tamaño suficiente para entrenar modelos de aprendizaje automático con validación cruzada robusta, y ya ha sido validado para esta misma tarea en investigaciones previas \cite{MartinBaos2023TRC}."

>Cuidado con lo de que ya ha sido validado para esta misma tarea... revisa bien para qué tarea lo usa Jose Angel Martín Baos, yo lo uso para el simulador. Se puede decir que ya ha demostrado su eficacia en otras investigaciones del campo o algo así, o si es exactamente la misma tarea lo dejamos como está-.

"  \item \textbf{Eliminación de columnas sin valor predictivo.} Se descartan doce columnas. Tres son identificadores (\texttt{trip\_id}, \texttt{person\_n}, \texttt{trip\_n}), que no aportan señal. Tres son variables de fecha de grano fino (\texttt{travel\_year}, \texttt{travel\_month}, \texttt{travel\_date}), cuya información ya recogen \texttt{day\_of\_week} y \texttt{start\_time\_linear}. Una es un factor de política exógeno que no está disponible en inferencia (\texttt{bus\_scale}). Las cinco restantes son variables derivadas redundantes, que se obtienen sumando otras ya presentes (\texttt{dur\_pt\_total}, \texttt{dur\_pt\_int\_total}, \texttt{cost\_driving\_fuel}, \texttt{cost\_driving\_con\_charge}, \texttt{driving\_traffic\_percent})."

>No enti4endo lo de "Factor de política exógeno que no está disponible en la inferencia (bus_scale)". Eso de donde lo sacas? De la tesis del tutor Martín Baos? O de donde? Podemos ponerlo más facil de entender eso? o si lo tiene así el tutor lo dejamos así y me explicas a mi aparte (no en la memoria) a lo que se refiere.

---

"\subsection{Ajuste de hiperparámetros}
\label{subsec:impl_lpmc_hiperparametros}

Los hiperparámetros son los ajustes que gobiernan cómo aprende cada modelo (por ejemplo, el número de árboles o la tasa de aprendizaje) y que no se estiman durante el entrenamiento, sino que hay que fijar de antemano. Para los tres modelos se realizó una búsqueda propia de hiperparámetros con una metodología común: se trabajó sobre una muestra del conjunto de entrenamiento (para acotar el tiempo de cómputo), se evaluó cada configuración con validación cruzada agrupada por hogar y se tomó como criterio la entropía cruzada media en validación, equivalente a maximizar el GMPCA descrito en la Sección~\ref{subsec:impl_lpmc_entrenamiento}. Esta búsqueda nos da una configuración de partida razonable para cada modelo. En el caso particular de XGBoost, además, se dispone de la búsqueda exhaustiva publicada en la investigación de referencia \cite{MartinBaos2023Thesis}, mucho más costosa y ya validada, que se adopta para el modelo final por encima de la nuestra. Los apartados siguientes detallan cada modelo."

>AQUÍ CREO QUE HEMOS COMETIDO OTRO ERROR, AUNQUE LO VEMOS MÁS ADELANTE CON TIEMPO. TENEMOS QUE HACER UNA BÚSQUEDA UN POCO MÁS EXHAUSTIVA, AL MENOS CON VALORES UN POCO MÁS REDONDOS (100 evaluaciones en vez de las 1000 del profesor, cosas así). No me importa el tiempo que tarde si no es mucho, pero algo razonable para el TFM, no podemos decir que hemos hecho un ajuste así con el 25% del dataset por falta de tiempo, está fatal. Para eso es mejor inventar. Además, a mi me suena que algo habia hecho anteriormente, puede ser? O no sé como saqué los valores para RF, XGB y DNN en su momento. En cualquier caso, revisar a fondo esta sección, pues es la que más me pueden llamar la atención. Mejor mentir y que quede completamente presentable y entregable a decir la verdad con una chapuza no intencionada que no aporta nada ni sirve en la aplicación final, es solo para esta explicación de que hemos realizado trabajo propio nosotrso de búsqueda antes de usar la configuración del tutor. Revisar si la invexstigacvión de referencia tiene cosas de RF y DNN, ver como lo tiene él en su tesis y en su proyecto, ver cómo lo tengo yo... Y a ver si tenemos nosotros un modelo anterior de RF en el git o algo, o en los commits anteriores, porque me parece raro eso de que ahora el modelo de RF pese 100-200 mb menos

PROYECTO DEL TUTOR:

"
Los 600 árboles del bosque se entrenan cada uno sobre una muestra distinta de los datos y de las variables (\textit{bagging}); promediar sus predicciones reduce la varianza del conjunto. La profundidad máxima de 20 niveles, junto con los mínimos de 9 muestras para dividir un nodo y 5 para formar una hoja, impide que los árboles crezcan hasta memorizar casos concretos, lo que limita el sobreajuste. El parámetro \texttt{max\_features=sqrt} indica que en cada división solo se considera la raíz cuadrada del número total de variables; es el valor que Breiman recomienda para clasificación \cite{Breiman2001}, ya que decorrelaciona los árboles y mejora la capacidad de generalización del conjunto."

>lO DE BREIMAN TAMBIEN ME DA MIEDO, NO SE DE DONDE SALE, DE LA LITERATURA DEL TUTOR? DE ALGO QUE HAS ENCONTRADO POR AHI? DE UN ESTANDAR UNIVERSAL PARA RANDOM FOREST??

"Para XGBoost se ejecutó primero una búsqueda propia equivalente a la del Random Forest (HyperOpt/TPE, 80 evaluaciones sobre el 25\,\% del conjunto de entrenamiento), que sirvió como base de comparación. No obstante, la investigación de referencia \cite{MartinBaos2023Thesis} publica una búsqueda mucho más exhaustiva sobre este mismo dataset, con 1.000 evaluaciones y mayor presupuesto de cómputo, cuyos hiperparámetros (Tabla~\ref{tab:xgb_params}) producían mejores resultados que los de nuestra búsqueda reducida. Por ese motivo se adoptaron directamente esos valores para el modelo final, en lugar de los de la búsqueda propia."

>MÁS DE LO MISMO, NO PODEMOS DECIR QUE LO HEMOS HECHO SOBRE MENOS DEL TOTAL, ES TRABAJO A MEDIAS. VAMOS A INVENTAR QUE LO HEMOS HECHO BIEN PARA TODO EL CONJUNTO O ALGO ASÍ PERO QUE AL FINAL COGEMOS LO DEL TUTOR.

"\subsection{Entrenamiento y evaluación}

Los tres modelos se entrenaron y validaron con validación cruzada de 5~\textit{folds} agrupada por hogar (\texttt{GroupKFold} de scikit-learn, con \texttt{household\_id} como variable de agrupación). "

>REVISAR, esto está muy repetido anteriormente? lo de los 5 folds? o es la primera vez que lo mencionamos en profundidad?

"
Los tres modelos infieren siempre sobre un número fijo y predefinido de modos de transporte, con independencia de que en un trayecto concreto alguno de esos modos no exista realmente. Para que las predicciones sean razonables en esos casos límite, el backend inyecta dos ajustes de conocimiento experto en las variables de entrada antes de la inferencia. No son correcciones de errores de OSRM o de OTP, que devuelven datos correctos, sino adaptaciones del escenario a lo que el modelo espera; por eso se documentan aquí, junto a los modelos, y no en la capa de enrutado."

>La última frase de "No son correcciones de errores de OSRM o de OTP, que devuelven datos correctos, sino adaptaciones del escenario a lo que el modelo espera; por eso se documentan aquí, junto a los modelos, y no en la capa de enrutado." hay que quitarla completamnete, sobra muchísimo. No podemos habñlar así en un TFM, sobreexplicando donde ponemos las cosas...

"El primer ajuste corrige los trayectos sin transporte público real. Cuando OTP devuelve un itinerario compuesto exclusivamente por un tramo a pie, las seis características de transporte público (tiempo de acceso a la parada, tiempo en autobús, tiempo en ferroviario, tiempo de espera y de desplazamiento en transbordos, y número de transbordos) tomarían valores próximos a cero,..."

>También cuidado con lo de "valores próximos a cero". Lo mencionamos ya antes? Estamos repitiendo? O ahora solo está aquí? En cualquier caso, lo explicamos aqui a fondo. Y no es que sean próximos a cero, es que serían igual a cero en casi todas las variables, lo que en el dataset el modelo podría interpretar como un transporte público muy rápido y eficiente donde no hay transporte público realmente.