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

### DSUALM y DSUALMH

En febrero de 2022, se desarrolló el nuevo conjunto de datos DSUALM^15^
(Data Set de la Universidad de Almería), el cual se creó a partir de las
mediciones de siete medidores OpenZmeter v1, cuyas medidas se asocian al
agregado y al de 6 aplicaciones. Este contador de electricidad y
analizador de calidad de energía (OZM) empleado para la creación de este
conjunto de datos, ha sido desarrollado en colaboración con la
Universidad de Granada y ALmeria, y funciona de acuerdo con los
principios de código abierto y hardware abierto. Mide parámetros
eléctricos a alta frecuencia (15625Hz) como frecuencia, corriente,
potencia activa, factor de potencia, potencia aparente y potencia
reactiva, entre otras medidas \[25\].

### DSUALM10 y DSUALM10H

En junio de 2023, se desarrolló DSUALM10H^17^ (Dataset de la Universidad
de Almería de 10 electrodomésticos con armónicos), el cual como su
propio nombre indica amplió con 10 electrodomésticos la versión inicial.
Este nuevo conjunto de datos incluye 150+ mediciones eléctricas con
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
para cada dispositivo, como se muestra en Fig. 51.

![](./imagenes/media/image1.jpg){width="5.595879265091863in"
height="4.017341426071741in"}

### UALM2

OMPM10 (Open Multi Power Meter), se desarrolló en 2023 a partir de
mediciones de 6 canales (5+añadidos) utilizando un novedoso sistema
basado en un único microcontrolador ESP32, un lector de tarjetas
microSD, una pantalla I2C y 6 módulos de medición PZEM004, todos ellos
funcionando en un bus RS485. Los 6 módulos de medición están asociados
respectivamente al contador principal y a los cinco aparatos que se
seleccionaron por su bajo consumo (Freidora, Lámpara LED, Lámpara
Incandescente, Ordenador Portátil, Ventilador).
