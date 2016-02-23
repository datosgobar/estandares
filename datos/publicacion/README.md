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
* Horarios de apertura de locales: **TODO**
* Numeros: De acuerdo con lo definido por la W3C \[2\] se tendra en cuenta lo siguiente:
 * El separador decimal debe ser el caracter "."
 * Se admiten los siguientes valores especiales:
  * NaN: Indica que el valor no es un numero valido.
  * INF y -INF: En caso de que el valor tienda a mas o menos infinito respectivamente.
 * Se recomienda consultar la especificacion original en caso de de dudas sobre casos particulares.
* Informacion geografica embebida **TODO: Elegir preferido**
 * GeoJSON
 * WKT: Lenguaje de mark-up para almacenar informacion geografica utilizado por PostGIS entre otros. Definido incialmente por el Open Geospatial Consortium y luego extendido por la norma ISO/IEC 13249-3:2011.

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
**TODO: Elegir preferido**
* SHP: Es una especificacion abierta definida y manejada por la empresa Esri (los de ArcGIS).
 * https://en.wikipedia.org/wiki/Shapefile
* KML: Formato abierto de informacion geografica definido utilizando por Google
 * http://www.opengeospatial.org/standards/kml
* GeoJSON: Formato JSON simple para especificar informacion geografica.
 * http://geojson.org/
* TopoJSON: Extension de GeoJSON para manejar informacion topografica de manera compacta.
 * https://github.com/mbostock/topojson/wiki

#### Sistemas de referencia
El marco de referencia mas utilizado es WGS84 (EPSG 4326) con la proyeccion mercador Mercator (EPSG 3857).

El Instituto Geografico Nacional utiliza el Sistema de Referencia WGS 84 y el Marco de Referencia POSGAR 07 para los datos que libera.
* http://www.ign.gob.ar/sig

#### Validacion de archivos GeoJSON
Se recomienda utilizar alguna herramienta como la siguiente para asegurarse de que el formato del archivo GeoJSON se correcto
* http://geojsonlint.com/

