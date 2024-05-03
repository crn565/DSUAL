# CONJUNTO DE DATASETS APTOS PARA EL NILM DE LA UNIVERSIDAD DE ALMERIA

En este repositorio presentamos cinco nuevos conjuntos de datos de
medidas eléctricas incluyendo el agregado de estas en el formato H5
usado en la herramienta NILMTK.

Los nuevos conjuntos de datos son los siguientes:

-   **DSUALM:** mediciones de siete medidores OZM (OpenZmeter) v1, cuyas
    medidas se asocian al agregado y al de 6 aplicaciones.

-   **DSUALMH**: mediciones de siete medidores OZM (OpenZmeter) v1,
    cuyas medidas se asocian al agregado y al de 6 aplicaciones. En este
    conjunto de datos además se incluyen los armónicos hasta el orden
    150 de la tensión, corriente y potencia

-   **DSUALM10**: mediciones de siete medidores OZM (OpenZmeter) v2,
    cuyas medidas se asocian al agregado y al de 10 aplicaciones

-   **DSUALM10H**: mediciones de siete medidores OZM (OpenZmeter) v2,
    cuyas medidas se asocian al agregado y al de 10 aplicaciones. En
    este conjunto de datos además se incluyen los armónicos hasta el
    orden 150 de la tensión, corriente y potencia

-   **UALM2:** mediciones de seis medidores OMPM (Open Multi Power
    Meter) v1, cuyas medidas se asocian al agregado y 5 aplicaciones.

Describimos a continuación más en detalle la composición de estos
conjuntos de datos.

## DSUALM y DSUALMH

En febrero de 2022, se desarrolló el nuevo conjunto de datos DSUALM
(Data Set de la Universidad de Almería), el cual se creó a partir de las
mediciones de siete medidores OpenZmeter v1, cuyas medidas se asocian al
agregado y al de 6 aplicaciones. Este contador de electricidad y
analizador de calidad de energía (OZM) empleado para la creación de este
conjunto de datos, ha sido desarrollado en colaboración con la
Universidad de Granada y ALmeria, y funciona de acuerdo con los
principios de código abierto y hardware abierto. Mide parámetros
eléctricos a alta frecuencia (15625Hz) como frecuencia, corriente,
potencia activa, factor de potencia, potencia aparente y potencia
reactiva, entre otras medidas.


### DESCARGAS DE LOS DATASETS 
-DSUALM se puede descargar desde el repositorio (https://github.com/crn565/DSUAL_without-armonics) en: 
https://github.com/crn565/DSUAL_without-armonics/blob/main/dsual.h5

-DSUALMH se puede descargar commprimido desde el repositorio (https://github.com/crn565/DSUALMH_OZM) en dos partes:
https://github.com/crn565/DSUALMH_OZM/blob/main/dsualmh.part1.rar
https://github.com/crn565/DSUALMH_OZM/blob/main/dsualmh.part2.rar

## DSUALM10 y DSUALM10H

En junio de 2023, se desarrolló DSUALM10H (Dataset de la Universidad de
Almería de 10 electrodomésticos con armónicos), el cual como su propio
nombre indica amplió con 10 electrodomésticos la versión inicial. Este
nuevo conjunto de datos incluye 150+ mediciones eléctricas con
transitorios I, V y W, utilizando la nueva versión del OpenZmeter v2 de
alta precisión para mayor precisión.

Los tres dispositivos trifásicos OZM v2 empleados para generar este
conjunto de datos nos ofrecen en total doce canales de medición, de los
que uno de ellos queda reservado para la agregación del resto. El uso de
la API de OZM fue vital para adquirir datos operativos de múltiples
dispositivos durante períodos prolongados. Sin embargo, algunos campos
requirieron una adaptación para la integración con NILMTK, lo que
garantizó un registro preciso de los datos de consumo y el
almacenamiento de metadatos en el nuevo conjunto de datos.

El medidor primario IP X.X.X.100 (canal 1) se utilizó para las
mediciones agregadas, mientras que los otros diez dispositivos
utilizaron los canales restantes para registrar la marca de tiempo, la
potencia, la potencia reactiva, la frecuencia, el voltaje, el factor de
potencia, los datos de corriente y los armónicos hasta el orden de 50
para cada dispositivo, como se muestra en la imagen.



![](./images/image1.jpg)


### DESCARGAS DE LOS DATASETS 


-DSUALM10 se puede descargar desde el repositorio (https://github.com/crn565/10_APLICATIVOS_SIN_ARMONICOS)en: 
https://github.com/crn565/10_APLICATIVOS_SIN_ARMONICOS/blob/main/dsual.h5

-DSUALM10H se puede descargar commprimido en cuatro partes desde el repositorio (https://github.com/crn565/DSUALM10H_OZM):
https://github.com/crn565/DSUALM10H_OZM/blob/main/dsualmh.zip.001
https://github.com/crn565/DSUALM10H_OZM/blob/main/dsualmh.zip.002
https://github.com/crn565/DSUALM10H_OZM/blob/main/dsualmh.zip.003
https://github.com/crn565/DSUALM10H_OZM/blob/main/dsualmh.zip.004


## UALM2

OMPM10 (Open Multi Power Meter), se desarrolló en 2023 a partir de
mediciones de 6 canales (5+añadidos) utilizando un novedoso sistema
basado en un único microcontrolador ESP32, un lector de tarjetas
microSD, una pantalla I2C y 6 módulos de medición PZEM004, todos ellos
funcionando en un bus RS485. Los 6 módulos de medición están asociados
respectivamente al contador principal y a los cinco aparatos que se
seleccionaron por su bajo consumo (Freidora, Lámpara LED, Lámpara
Incandescente, Ordenador Portátil, Ventilador).


### DESCARGAS DEL DATASET 


-UALM2 se puede descargar desde el repositorio (https://github.com/crn565/OMPM) en:
https://github.com/crn565/OMPM/blob/main/ualm2.h5

# NUEVOS CONVERSORES

# 

Dado que los diferentes ficheros de medidas obtenidos con oZm v1, oZm v2
y el OMPM se deben procesar en formato csv en la una fase previa (ver
cuadernos en Jupyter correspondientes a la fase uno para cada Dataset),
necesitamos transferir estas a un único fichero optimizado en formato
HDF5 (o simplificando H5), y que almacenamos en la carpeta "/data/".
Además, es de destacar, que cada archivo H5 que generaremos a partir de
los ficheros de medidas, no sólo va a contener las medidas recopiladas
que nos interesen de cada medidor, ya que también contendrá todos los
metadatos del nuevo conjunto de datos.

Asimismo, según la versión de oZm, el número de aplicativos, y si se van
a procesar armónicos, generaremos 4 nuevos conjuntos de datos: dos
nuevos conjuntos de datos (con o sin armónicos) para oZm v1 con 5
aplicativos más el agregado y otros dos otros nuevos conjuntos de datos
(con o sin armónicos) para oZm v2 con 10 aplicativos más el agregado. De
forma similar para el OMPM al no soportar armónicos crearemos sólo un
nuevo dataset con 5 aplicativos más el agregado.

NILMTK usa formatos de conjuntos de datos estandarizados (ver apartado
2.8 titulado "DS Públicos"), pero dada la exclusividad de los datos
ofrecidos por ambas versiones de oZm (y después OMPM), requerimos un
formato de datos nuevo, para lo cual creamos 4 nuevas funciones para
generar los diferentes conjuntos de datos*.* Como podemos intuir, estos
nuevos convertidores, aunque están basados en el convertidor de IAWE,
contiene grandes diferencias porque se ha incluido el soporte de
timestamp de 13 dígitos, así como nuevas medidas y además difieren en el
soporte de armónicos, y en el número o tipo de electrodomésticos
soportados.

Estas nuevas funciones que generaran los nuevos conjuntos de datos, en
caso de que nuestro equipo cuente con Windows 11 (o Windows 10) y
tengamos instalado tanto Anaconda como NILMTK, se situaran en nuevos
directorios en la ruta:
*"/Users/Usuariox/anaconda3/envs/NILMTK-env/Lib/site-packages/nilmtk/data-converters/".*

En estos directorios además de albergar el código en *Python* de los
nuevos convertidores, también debemos incluir un nuevo subdirectorio
llamado "*/metadata/"*, el cual incluya los ficheros de metadatos.

Para soportar el nuevo conversor, en la ruta mencionada incluimos el
fichero *convert_ualm.py*, fichero donde contendremos el código del
nuevo convertidor que procesará los ficheros del oZm (en el ejemplo oZm
v1 sin soporte de armónicos).

En el caso de necesitar procesar armónicos, de forma análoga al
tratamiento sin armónicos crearemos el directorio
*"/Users/Usuariox/anaconda3/envs/NILMTK-env/Lib/site-packages/nilmtk/data-converters/ualm5t"*
y replicaremos la estructura anterior, pero incluyendo
*convert_ualmt.py*, (entre otros ficheros), cuyo cometido será procesar
los ficheros del oZm v1 incluyendo armónicos (*convert_ualmt.py*).

Por otra parte, de un modo similar al citado anteriormente, en el caso
de oZm v2 al implementar un mayor número y tipos de diferentes de
electrodomésticos, precisaremos una lógica, muy similar a la anterior
(con soporte o no de armónicos) pero diferenciada para procesar las
nuevas medidas.

Respecto al tratamiento de armónicos, tanto con los datos aportados por
oZm v1 como con los datos aportados por oZm v2, generados los ficheros
de medida, dado que vamos a añadir nuevos campos, tenemos que modificar
asimismo el código en *Python* del conversor en la lista
*column_mapping,* para que procese los nuevos campos.

Es muy relevante el contenido de estos tres ficheros mostrados en la
imagen anterior, pues nos van a posibilitar incorporar los metadatos que
contendrá el conjunto de datos, así como también los tipos de medidas
contenidas en los ficheros de datos en formato *csv.*

Precisamente, podemos ver de forma más clara la configuración de todos
los ficheros necesarios para los nuevos convertidores, así como la
estructura de directorios requerida.

![](./images/image2.png)

Pasemos a ver el contenido de estos ficheros, para lo cual, empecemos
observando el fichero *building1.yaml,* cuyo contenido podemos ver en el
listado en formato *yaml* que, según el conversor, en este caso ualm5,
localizaremos en la ruta
"*C:\\Users\\Usuario\\anaconda3\\envs\\nilmtk-env\\Lib\\site-packages\\nilmtk\\dataset_converters\\ualm5\\metadata\\building1.yam)*,"
donde se configuran en este caso los 5 dispositivos más el agregado
(todos del tipo oZm v1), y el nombre de los aparatos eléctricos al que
están conectados.

![](./images/image3.png)

Como deducimos en el listado anterior tenemos 6 medidores (todos oZm
v1), siendo el número uno el principal desde el punto de vista
conceptual (es decir, el general o *Main*), y el resto, contadores
individualizados conectados a 5 electrodomésticos diversos.

Es fácil entender que este fichero es idéntico para los dos conversores
usados con oZm v1 (con o sin armónicos) al contener ambos los mismos
aplicativos, pero es diferente a los ficheros usado en los conversores
para procesar los datos provenientes de oZm v2 (con o sin armónicos)
dado que se amplía en este caso el número de aplicativos.

Si visualizamos el contenido del fichero *dataset.yaml*, en el listado
en formato *yaml*, se puede apreciar cómo se especifican el resto de
metadatos que pueden ser de interés para el investigador, como lo es la
fecha, la localización geográfica o simplemente una vía de contacto,
metadatos que obviamente asociaremos también al conjunto de datos.

![](./images/image4.png)

Es fácil deducir que este fichero es idéntico al del conversor con
soporte con armónicos dado que parten de las mismas medidas, siendo
además muy similar al usado con las medidas de oZm v2 (excepto en
apartado referente a la fecha de publicación).

Por último, nos queda también en formato *yaml*, el fichero de medidas
*meter_devices.yaml*. En éste hay diferencias acusadas tanto en las
medidas obtenidas con oZm v1 o oZm v2 como en el soporte de armónicos,
porque si bien comparten el número de medidas fundamentales soportadas
por los diferentes oZm's (como son la potencia activa, aparente y
reactiva, la frecuencia, el voltaje, la corriente y el factor de
potencia) en los conjuntos de datos con soporte de armónicos añadiremos
además 150 medidas correspondientes a los armónicos hasta el orden 50 de
la tensión, corriente y potencia.

En este caso, al ser medidas idénticas las tomadas con oZm v1 y oZm v2,
este fichero asociado, dado que está asociado al tipo de contador, este
será idéntico en ambas versiones tan solo defiriendo en el soporte de
armónicos al albergar estos ultimo un mayor número de medidas. Por
tanto, es relevante destacar en este punto, como el fichero de medidas
debe estar íntimamente relacionado con el convertidor de los ficheros de
datos, razón por la cual, en esta Tesis, dado que buscamos evaluar la
posible mejora del procesamiento de los armónicos en NILMTK,
dispondremos para los datos aportados por oZm v1 y oZm v2 de diferentes
convertidores con todo su soporte necesario (función de conversión,
ficheros de configuración, etc.)

Como ejemplo reproducimos en el listado el contenido para el caso de
conversor de los datos apartados por oZm v1 sin soporte de armónicos.

![](./images/image5.png)

Es fácil deducir que este fichero será idéntico al usado en el conversor
para capturar los datos de oZm v2 sin armónicos. Además de forma
parecida en el caso de soporte con armónicos tanto para oZm v1 como oZm
v2 el contenido de este fichero será aún mucho más extenso al incluir
además 150 variables correspondientes a los 50 armónicos de tensión,
corriente y potencia.

**Ampliación del soporte de nuevos conversores a NILMTK**

Es necesario destacar, que como el formato original de NILMTK para el
campo *timestamp* es de 10 dígitos, pero el *timestamp* arrojado por el
OZM está en formato 13 dígitos (es decir, en el que se almacena hasta
los milisegundos pasados desde el 1 del 1 de 1970). Es por ello que
debemos realizar una adaptación especial, pues además este formato no es
soportado por ningún conversor soportado por el toolkit. Es precisamente
este importante cambio, en el formato de *timestamp* de 10 a 13 dígitos,
uno los motivos por el que se requieren nuevos convertidores específicos
para el procesamiento de las medidas arrojadas por los oZm's en sus
diferentes versiones, además de otros factores secundarios (como, por
ejemplo, el cambio del valor de *timezone* para nuestra ubicación de
*Europe/Madrid).*

Además, respecto a los metadatos que se van a tratar en los diferentes
convertidores, estos difieren, dado que algunos soportan solo la
potencia (real, reactiva y aparente), el voltaje, la intensidad, la
frecuencia y el factor de potencia, pero en otros además añadimos los
armónicos hasta el orden 50 de la corriente, tensión y potencia.

Como cada fichero de medidas es obtenido en la fase anterior a partir de
los ficheros de los diferentes oZm's, es necesario numerarlos del 1 al
número de aplicativos máximo (6 en caso de oZm v1 y 11 en caso de oZm
v2), siendo el Nº 1 el correspondiente al medidor principal y el resto
perteneciente a los submedidores asociados a los aparatos eléctricos.
Para ello, cada nueva función accede a todos los citados ficheros de
datos de medidas localizados en la carpeta de entrada "/*electricity/",*
usando para ello el fichero de etiquetas *labels.csv,* proceso que
representamos en la siguiente figura.

> [](./images/image6.jpg)

Obviamente, al contenido del fichero *labels.dat* dependerá de los
electrodomésticos que hayamos conectado en el experimento en particular,
pero, en todo caso, es muy importante este fichero, ya que ubica cada
fichero *csv* numerado con su aplicativo (por ejemplo, el fichero
*1.csv*, que corresponde a la primera línea, corresponde a *mains*, es
decir al contador principal).

En el caso de los datos ofrecidos por oZm v2, la estructura de ficheros
es muy similar a la vista con los datos de oZm v1, lógicamente con los
cambios oportunos para soportar el doble de aplicativos, tal y como
podemos ver en el siguiente esquema en la imagen.

![](./images/image7.png)

Un ejemplo del contenido de este fichero, usado para las medidas tomadas
con oZm v1 tanto con soporte o no de armónicos, se puede observar en la
Tabla.

![](./images/image8.png)

En el caso las medidas tomadas con oZm v2 tanto con soporte o no de
armónicos, al ampliar el número de aplicativos su contenido es
diferente, como podemos ver en siguiente tabla.

![](./images/image9.png)

En cuanto a los ficheros de datos (*1.csv, 2.csv, 3.csv, 4.csc, 5.csv,
6.csv*), salvando la primera fila que corresponde a los identificativos
de los campos de las medidas, el resto de filas representa una medida en
un determinado instante temporal definido por su valor de *timestamp**.*

En nuestro caso, el valor del *timestamp* está fijado al formato Unix
Epoc de 13 dígitos, a diferencia del formato convencional de NILMTK que
está fijado en 10 dígitos, **siendo este trabajo uno de los primeros
trabajos relacionados con NILMTK en adoptar dicho formato, mucho más
completo.**

Es de destacar que los ficheros de medidas deben estar de acorde, tanto
con los ficheros de metadatos (en formato *yaml*), como con los propios
datos en sí mismos (en formato csv).

Una vez ubicados los ficheros de medidas, lo primero es invocar el
conversor especifico llamando a la nueva función *convert_ualm* (de modo
similar se haría de forma similar con las correspondientes funciones
específicas para el resto de datasets)*,* pasándole la ruta de los
metadatos y el nuevo nombre del fichero del conjunto de datos que se
generará en formato *H5*, como podemos hacer con el Listado en *Python*.

![](./images/image10.png)

Es asimismo importante mencionar para que, tanto los ficheros de
metadatos como el código en *Python* de cada convertidor sean procesados
por el toolkit, debemos añadir nuevas líneas en el fichero \_\_init\_\_
con los 5 nuevos conversores soportados, tal y como podemos apreciar en
la imagen.

![](./images/image11.png)

En cuanto al fichero "\_\_init\_\_\_", este decisivo fichero en formato
yaml lo localizaremos en la ruta:
*"/Users/Usuariox/python3/envs/NILMTK-env/Lib/site-packages/NILMTK/data-converters/\_\_init\_\_",*
y su contenido los podemos ver a continuación.

![](./images/image12.png)

En este fichero, es de destacar las últimas nuevas líneas de código,
donde contemplamos el soporte de los nuevos convertidores:

-   *convert_ualm* que usaremos para el procesamiento de los datos
    provenientes de varios oZm v1 sin registrar armónicos con 5
    aplicativos (Línea 15).

-   *convert_ualmt,* que contempla 5 aplicativos, pero además de los
    campos mencionados, los armónicos hasta el orden 50 de la tensión,
    la corriente y la potencia (Línea 16)

-   *convert_ualm10* que usaremos para el procesamiento de los datos
    provenientes de varios oZm v2 sin registrar armónicos con 10
    aplicativos (Línea 17)

-   *convert_ualm10H,* que contempla 10 aplicativos, pero además de los
    campos mencionados, los armónicos hasta el orden 50 de la tensión,
    la corriente y la potencia (Línea 18)

-   *convert_ualm2* para procesar las medidas del nuevo hardware
    OMPM(Línea 19).
