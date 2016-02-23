Publicación de Datos
===

## Estándares

En las siguientes subsecciones se estipulan procedimientos de publicación estándar que se aplican a todos los datasets.

### Informacion Tabular
Se usar archivos CSV con las siguientes caracteristicas:

* Todos los datasets se publican en el charset UTF-8 segun \[2\]
* Se deben usar saltos de linea **CR-LF (\r\n)** siguiendo lo indicado por el RFC4180 \[1\] y \[2\]
* No se admiten nombre de columnas duplicados.
* No se admiten nombre de columnas duplicados.
* Se considera valido para todos los tipos de dato que el valor indefinido.
Ej: 
col1,col2,col3, 
a,,b 
a,"",b 
En la primera linea el valor de la columna col2 es indefinido en tanto que en la segunda se considera una string vacia. 

* Formato de tipos de datos (basado en la especificacion de la W3C \[2\]): 
 * Boolean: A menos que se indique lo contrario se identificaran con los valores **true o false**. 
Tene en cuenta que este campo puede tener el valor indefinido. Si existe la posiblidad de que haya otro posible valor significa que se eligio un tipo de dato incorrecto. 
* Strings: Segun el RFC 4180 las strings pueden o no estar entre comillas dobles pero seria recomendable que en todo caso lo esten para separar el caso de las strings vacias y los valores indefinidos. 
* Tiempo: Se usara el estandar **ISO 8601 (YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM])** \[3\]. A menos que se indique lo contrario se asumira la que la zona horaria es UTC-03:00 (Argentina).
 * Fecha: **YYYY-MM-DD**
 * Hora: **HH:MM:SS[.mmmmmm][+HH:MM]**
 * Fecha y Hora: **YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM]**
 * Duracion: **YYYY-MM-DDTHH:MM:SS[.mmmmmm]**
* Rangos horarios recurrentes:
 * Se aceptaran los siguientes formatos:
  ``` 
  Se usara el formato HH:MM-HH:MM para indicar un rango que ocurre todos los dias.
  Se usara el formato DAY para indicar que el rango ocupa todo el dia DAY.
  Se usara el formato DAY_HH:MM-HH:MM para indicar un rango que ocurre los dias DAY entre HH:MM y HH:MM.
  Se usara el formato DAY_HH:MM-HH:MM_HH:MM-HH:MM para indicar mas un rango horario en el mismo dia
  Se usara el formato DAY1-DAY2_HH:MM-HH:MM para indicar un rango que ocurre los dias DAY1 a DAY2 entre HH:MM y HH:MM
  Se usara el formato DAY1-DAY2_HH:MM-HH:MM_HH:MM-HH:MM para indicar mas un rango horario en el mismo rango de dias 
  En caso de que se necesite cubrir mas de una franja horaria se incluiran varios rangos separados por espacios.
  ```
 * Los dias se indicaran con sus iniciales en castellano: LUN, MAR, MIE, JUE, VIE, SAB y DOM
 * Ejemplos:
  ```
  24hs -> "00:00-23:59" 
  Jueves 24hs -> "JUE" 
  Jueves de 14:30 a 17 hs -> "JUE_14:30-17:00" 
  Jueves de 8 a 12 hs y de 16 a 20 hs -> "JUE_14:30-17:00_16:00-20:00" 
  Jueves de 8 a 15 hs y Viernes de 8 a 15 hs -> "JUE_08:00-15:00 VIE_08:00-15:00" 
  Lunes a Viernes 7:30 a 17 hs y Sábados 8 a 12 hs -> "LUN-VIE_07:30-17:00 SAB_08:00-12:00" 
  Lunes a Viernes 8 a 11 y 14 a 18 hs -> "LUN-VIE_08:00-11:00_14:00-18:00" 
  ```
* Numeros: De acuerdo con lo definido por la W3C \[2\] se tendra en cuenta lo siguiente:
 * El separador decimal debe ser el caracter "."
 * Se admiten los siguientes valores especiales:
  * NaN: Indica que el valor no es un numero valido.
  * INF y -INF: En caso de que el valor tienda a mas o menos infinito respectivamente.
 * Se recomienda consultar la especificacion original en caso de de dudas sobre casos particulares.
* Informacion geografica embebida **TODO: Encontrar una herramientas para pasar de un formato a otro facilmente**
 * GeoJSON
 * WKT: Lenguaje de mark-up para almacenar informacion geografica utilizado por PostGIS entre otros. Definido incialmente por el Open Geospatial Consortium y luego extendido por la norma ISO/IEC 13249-3:2011.
 * WKB: Version binaria de WKT


Referencias:
\[1\]: http://tools.ietf.org/html/rfc4180 

\[2\]: https://www.w3.org/TR/tabular-data-model/ 

\[3\]: https://en.wikipedia.org/wiki/ISO_8601 

#### Validacion
Se recomienda el uso de alguna herramienta como csvlint para asegurarse que el formato del CSV es correcto y eliminar los errores obvios:
* http://csvlint.io/ 
* https://github.com/theodi/csvlint 

#### Tabular Data Package (a considerar)
Es un estandar para facilitar la publicacion y consumo de datos tabulares.
Consiste en agregar un datapackage.json al dataset con los CSVs con la metadata correspondiente.

CKAN dispone de herramientas para manejar este tipo de paquetes:
http://ckan.org/2014/06/09/the-open-knowledge-data-packager/

Ref:
http://data.okfn.org/doc/tabular-data-package
http://dataprotocols.org/data-packages/

### Informacion Geografica
#### Formatos utilizados comunmente

* SHP: Es una especificacion abierta definida y manejada por la empresa Esri (los de ArcGIS).
 * https://en.wikipedia.org/wiki/Shapefile
* KML: Formato abierto de informacion geografica definido utilizando por Google
 * http://www.opengeospatial.org/standards/kml
* GeoJSON: Formato JSON simple para especificar informacion geografica.
 * http://geojson.org/
* TopoJSON: Extension de GeoJSON para manejar informacion topografica de manera compacta.
 * https://github.com/mbostock/topojson/wiki
* GML: Estandar del Open Geospatial Consortium normalizado en el estandar ISO 19136:2007.
 * http://www.opengeospatial.org/standards/gml
 * http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=32554

De momento los formatos mas utilizados son SHP, KML y GeoJSON. 

**TODO: Encontrar una herramientas para pasar de un formato a otro facilmente**

#### Sistemas de referencia
El marco de referencia mas utilizado es WGS84 (EPSG 4326) con la proyeccion mercador Mercator (EPSG 3857).

El Instituto Geografico Nacional utiliza el Sistema de Referencia WGS 84 y el Marco de Referencia POSGAR 07 para los datos que libera.
* http://www.ign.gob.ar/sig

#### Validacion de archivos GeoJSON
Se recomienda utilizar alguna herramienta como la siguiente para asegurarse de que el formato del archivo GeoJSON se correcto
* http://geojsonlint.com/

