Publicación de Datos
===

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Estándares](#est%C3%A1ndares)
  - [Informacion Tabular](#informacion-tabular)
    - [Sobre los Campos.](#sobre-los-campos)
    - [Sobre los datos](#sobre-los-datos)
  - [Validación](#validaci%C3%B3n)
  - [LINKS Y REFERENCIAS QUE PUEDEN SER UTILES](#links-y-referencias-que-pueden-ser-utiles)
    - [Tabular Data Package (a considerar)](#tabular-data-package-a-considerar)
    - [Informacion Geografica](#informacion-geografica)
      - [Formatos utilizados comunmente](#formatos-utilizados-comunmente)
      - [Conversion entre formatos](#conversion-entre-formatos)
      - [Sistemas de referencia](#sistemas-de-referencia)
      - [Validacion de archivos GeoJSON](#validacion-de-archivos-geojson)
    - [Estándares para fines especificos](#est%C3%A1ndares-para-fines-especificos)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Estándares

En las siguientes subsecciones se estipulan procedimientos de publicación estándar que se aplican a todos los datasets.

### Información Tabular
Se usan archivos CSV con las siguientes características:

* Todos los datasets se publican en el charset UTF-8 según [W3C][W3C]
* Se deben usar saltos de linea **CR-LF (\r\n)** siguiendo lo indicado por el RFC4180 [rfc4180][rfc4180] y [W3C][W3C]
* No se admiten nombres de columnas duplicados.
* Para todos los tipos de datos se considera válido el valor indefinido. Este se expresará con la ausencia de todo caracter y no con un caracter o string especial como podrían ser ".", "null", "none", "nan", etc.

**Ejemplo:**

```
col1,col2,col3, 
a,,b 
a,"",b 
```

En la primera línea el valor de la columna *col2* es indefinido, mientras que en la segunda línea se considera un string vacío.

#### Sobre los campos

* Los campos deben ser lo más atómicos posible. Se debe evitar definir campos que contengan más de un tipo de información (por ejemplo: e-mail y sitio web).
* Los nombres de los campos deben respetar la siguiente convención: palabras en minúsculas unidas por un guión bajo, utilizando únicamente caracteres ASCII **a-z** y **0-9** (Ej.: *fecha_audiencia_solicitada*)


#### Sobre los datos
El formato de tipos de datos está basado en la especificacion de la [W3C][W3C]: 

##### Strings

Según el [RFC 4180][rfc4180] los strings pueden o no estar entre comillas dobles. En el caso de que un valor corresponda a un string vacío, este debe estar encerrado entre comillas dobles para separarlo del caso de valor indefinido.

* *Nombres propios:* Se capitalizan (primera letra de cada palabra es mayúscula, el resto de las letras son minúsculas) todas las palabras significativas, salvo las siglas. Las palabras significativas son aquellas que no cumplen la función de artículos o preposiciones.
* *Siglas:* Van todas en mayúscula sin puntos. 
* Las *entidades* mencionadas deben tener una descripción única. Es decir que toda mención que se realice a una entidad dada debe hacerse utilizando **exactamente la misma cadena de caracteres**

##### Tiempo

Se usará el estandar [ISO 8601][ISO8601] **(YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM])**. A menos que se indique lo contrario, se asumirá que la zona horaria es UTC-03:00 (Argentina).
    - Fecha: **YYYY-MM-DD**
    - Hora: **HH:MM:SS[.mmmmmm][+HH:MM]**
    - Fecha y Hora: **YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM]**
    - Duración: **YYYY-MM-DDTHH:MM:SS[.mmmmmm]**

* *Rangos horarios:*
    - Los rangos estarán divididos en dos partes separadas por un doble guión bajo "__", la primera indica el día y la segunda, la hora.
    - Se puede omitir la parte del día o bien de la hora pero nunca ambas
    - Si se omite la parte que indica el día se asumira que el rango abarca todo el horario indicado
    - Si se omite la parte que indica el horario se asumira que el rango abarca todo el día indicado
    - El día se puede indicar tanto medíante rangos separando los días con guines medios "-" o bien como particulares con el guion bajo "_".
    - Ejemplos de formatos validos para **días**:

    ```
    DAY: Un solo día
    DAY1-DAY2: Entre entre DAY1 y DAY2
    DAY1_DAY2: DAY1 y DAY2
    DAY1-DAY2_DAY3: DAY1 a DAY2 y DAY3
    ```

    - La hora se indica medíante rangos separando los horarios con guiones medios ("-"). También se pueden indicar varios horarios con el guión bajo "_".
    - Ejemplos de formatos válidos para **horas**:

    ```
    HH:MM-HH:MM : Rango simple
    HH:MM-HH:MM_HH:MM-HH:MM : Dos rangos
    ```

    - Más ejemplos de formatos válidos completos:

    ```
    HH:MM-HH:MM para indicar un rango que ocurre todos los días.
    DAY para indicar que el rango ocupa todo el día DAY.
    DAY__HH:MM-HH:MM para indicar un rango que ocurre los días DAY entre HH:MM y HH:MM.
    DAY__HH:MM-HH:MM_HH:MM-HH:MM para indicar mas un rango horario en el mismo día
    DAY1-DAY2__HH:MM-HH:MM para indicar un rango que ocurre los días DAY1 a DAY2 entre HH:MM y HH:MM
    DAY1-DAY2__HH:MM-HH:MM_HH:MM-HH:MM para indicar mas un rango horario en el mismo rango de días
    ```

    - En caso de que se necesite cubrir más de una franja horaria y esta sintaxis sea insuficiente, se pueden incluir varias separadas por espacios.
    - Los días se indicarán con sus iniciales en castellano: LUN, MAR, MIE, JUE, VIE, SAB y DOM
    - Ejemplos:

    ```
    24hs -> "00:00-23:59" 
    Jueves 24hs -> "JUE" 
    Jueves de 14:30 a 17 hs -> "JUE__14:30-17:00" 
    Jueves de 8 a 12 hs y de 16 a 20 hs -> "JUE__08:12-17:00_16:00-20:00" 
    Jueves de 8 a 15 hs y Viernes de 8 a 15 hs -> "JUE__08:00-15:00 VIE_08:00-15:00" 
    Lunes a Viernes 7:30 a 17 hs y Sábados 8 a 12 hs -> "LUN-VIE__07:30-17:00 SAB__08:00-12:00" 
    Lunes a Viernes 8 a 11 y 14 a 18 hs -> "LUN-VIE__08:00-11:00_14:00-18:00" 
    Lunes y Miercoles 8 a 11 y 14 a 18 hs -> "LUN_MIE__08:00-11:00_14:00-18:00" 
    Lunes a Miercoles y Viernes 8 a 11 y 14 a 18 hs -> "LUN-MIE_VIE__08:00-11:00_14:00-18:00"
    Lunes a Miercoles 8 a 11 y de Viernes a Domingo 9 a 10 -> "LUN-MIE__08:00-11:00 VIE-DOM__09:00-10:00"
    ```

##### Números

De acuerdo con lo definido por la W3C [W3C][W3C] se tendrá en cuenta lo siguiente:

* El separador decimal debe ser el caracter "."
* Se admiten los siguientes valores especiales:
    - NaN: Indica que el valor no es un número válido.
    - INF y -INF: En caso de que el valor tienda a mas o menos infinito respectivamente.
* Se recomienda consultar la especificación original en caso de de dudas sobre casos particulares.

##### Boolean

A menos que se indique lo contrario se identificaran con los valores **true o false**. Tener en cuenta que este campo puede tener el valor indefinido. Si existe la posiblidad de que haya otro valor significa que se eligio un tipo de dato incorrecto.

##### Información geografica

* **Información geográfica simple**
    - Si el dato que se quiere incluir es solo un punto indicado por su latitud y longitud se recomienda crear dos columnas "lat" y "lon" para dicho fin en lugar de utilizar un solo campo.

* **Información geografica embebida**
    - GeoJSON: Tiene la ventaja de que es facil de utilizar consumir.
    - WKT: Lenguaje de mark-up para almacenar informacion geografica utilizado por PostGIS entre otros. Definido incialmente por el Open Geospatial Consortium y luego extendido por la norma ISO/IEC 13249-3:2011.
    - WKB: Version binaria de WKT. Mucho mas compacto
    - El formato GeoJSON es el preferido. En la medida de lo razonable convendria incluir ademas una columna con los mismos datos en formato WKT y WKB.


<!-- Referencias -->

[rfc4180]: http://tools.ietf.org/html/rfc4180 
[W3C]: https://www.w3.org/TR/tabular-data-model/ 
[ISO8601]: https://en.wikipedía.org/wiki/ISO_8601 

### Validación
Se recomienda el uso de alguna herramienta como csvlint para asegurarse que el formato del CSV es correcto y eliminar los errores obvios:
* http://csvlint.io/ 
* https://github.com/theodi/csvlint 

###LINKS Y REFERENCIAS QUE PUEDEN SER UTILES
#### Tabular Data Package (a considerar)
Es un estandar para facilitar la publicacion y consumo de datos tabulares.
Consiste en agregar un archivo ```datapackage.json``` al dataset con los CSVs con la metadata correspondiente.

CKAN dispone de herramientas para manejar este tipo de paquetes:
http://ckan.org/2014/06/09/the-open-knowledge-data-packager/

Ref:
http://data.okfn.org/doc/tabular-data-package
http://dataprotocols.org/data-packages/

#### Informacion Geografica
##### Formatos utilizados comunmente

* SHP: Es una especificacion abierta definida y manejada por la empresa Esri (los de ArcGIS).
 * https://en.wikipedía.org/wiki/Shapefile
* KML: Formato abierto de informacion geografica definido utilizando por Google
 * http://www.opengeospatial.org/standards/kml
* GeoJSON: Formato JSON simple para especificar informacion geografica facilmente consumible.
 * http://geojson.org/
* TopoJSON: Extension de GeoJSON para manejar informacion topografica de manera compacta.
 * https://github.com/mbostock/topojson/wiki
* GML: Estandar del Open Geospatial Consortium normalizado en el estandar ISO 19136:2007.
 * http://www.opengeospatial.org/standards/gml
 * http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=32554

De momento los formatos mas utilizados son SHP, KML y GeoJSON. En la medida de lo posible es preferible ofrecer los datos en estos tres formatos.

##### Conversion entre formatos
* ogr2ogr: Soporta varios formatos
  * www.gdal.org/ogr2ogr.html
* WKT -> GeoJSON
  * https://github.com/mapbox/wellknown
* WKT -> GeoJSON (Shapely)
  * http://lists.geojson.org/pipermail/geojson-geojson.org/2008-August/000459.html
* GeoJSON -> SHP
  * http://ben.balter.com/2013/06/26/how-to-convert-shapefiles-to-geojson-for-use-on-github/
* Varias
  * https://ogre.adc4gis.com/
  * http://gis.stackexchange.com/questions/68175/geojson-to-esri-shapefile-using-ogr2ogr


##### Sistemas de referencia
El marco de referencia mas utilizado es WGS84 (EPSG 4326) con la proyeccion mercador Mercator (EPSG 3857).

El Instituto Geografico Nacional utiliza el Sistema de Referencia WGS 84 y el Marco de Referencia POSGAR 07 para los datos que libera.
* http://www.ign.gob.ar/sig

##### Validacion de archivos GeoJSON
Se recomienda utilizar alguna herramienta como la siguiente para asegurarse de que el formato del archivo GeoJSON se correcto
* http://geojsonlint.com/


#### Estándares para fines especificos
* Open Budget
  * https://github.com/open-data-standards/data-schemas/blob/gh-pages/schemas/Open_Budget.md
* Building & Land Development Specification
  * http://permitdata.org/
  * https://github.com/open-data-standards/permitdata.org/wiki
* Varias
  * https://www.codeforamerica.org/our-work/data-formats/

