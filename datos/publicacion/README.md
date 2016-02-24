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
 * Los rangos estaran divididos en dos partes separadas por un doble guion bajo "__", la 1ra indica el dia y otra la hora.
 * Se puede omitir la parte del dia o bien de la hora pero nunca ambas
 * Si se omite la parte que indica el dia se asumira que el rango abarca todo el horario indicado
 * Si se omite la parte que indica el horario se asumira que el rango abarca todo el dia indicado
 * El dia se puede indicar tanto mediante rangos separando los dias con guines medios "-" o bien como particulares con el guion bajo "_".
 * Ejemplos de formatos validos para dias:
  ``` 
  DAY : Un solo dia
  DAY1-DAY2 : Entre entre DAY1 y DAY2
  DAY1_DAY2 : DAY1 y DAY2
  DAY1-DAY2_DAY3 : DAY1 a DAY2 y DAY3
  ``` 
 * La hora se indica mediante rangos separando los horarios con guines medios "-". Tambien se pueden indicar varios horarios con el guion bajo "_".
 * Ejemplos de formatos validos para horas:
  ``` 
  HH:MM-HH:MM : Rango simple
  HH:MM-HH:MM_HH:MM-HH:MM : Dos rangos
  ``` 
 * Mas ejemplos de formatos validos completos:
  ``` 
  HH:MM-HH:MM para indicar un rango que ocurre todos los dias.
  DAY para indicar que el rango ocupa todo el dia DAY.
  DAY__HH:MM-HH:MM para indicar un rango que ocurre los dias DAY entre HH:MM y HH:MM.
  DAY__HH:MM-HH:MM_HH:MM-HH:MM para indicar mas un rango horario en el mismo dia
  DAY1-DAY2__HH:MM-HH:MM para indicar un rango que ocurre los dias DAY1 a DAY2 entre HH:MM y HH:MM
  DAY1-DAY2__HH:MM-HH:MM_HH:MM-HH:MM para indicar mas un rango horario en el mismo rango de dias 
  ```
 * En caso de que se necesite cubrir mas de una franja horaria y esta sintaxis sea insuficiente se pueden incluir varias separadas por espacios.
 * Los dias se indicaran con sus iniciales en castellano: LUN, MAR, MIE, JUE, VIE, SAB y DOM
 * Ejemplos:
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
* Numeros: De acuerdo con lo definido por la W3C \[2\] se tendra en cuenta lo siguiente:
 * El separador decimal debe ser el caracter "."
 * Se admiten los siguientes valores especiales:
  * NaN: Indica que el valor no es un numero valido.
  * INF y -INF: En caso de que el valor tienda a mas o menos infinito respectivamente.
 * Se recomienda consultar la especificacion original en caso de de dudas sobre casos particulares.
* Informacion geografica simple
 * Si el dato que se quiere incluir es solo un punto indicado por su latitud y longitud se recomienda crear dos columnas "lat" y "long" para dicho fin en lugar de utilizar un solo campo.
* Informacion geografica embebida
 * GeoJSON: Tiene la ventaja de que es facil de utilizar consumir.
 * WKT: Lenguaje de mark-up para almacenar informacion geografica utilizado por PostGIS entre otros. Definido incialmente por el Open Geospatial Consortium y luego extendido por la norma ISO/IEC 13249-3:2011.
 * WKB: Version binaria de WKT. Mucho mas compacto
 * El formato GeoJSON es el preferido. En la medida de lo razonable convendria incluir ademas una columna con los mismos datos en formato WKT y WKB.


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
Consiste en agregar un archivo ```datapackage.json``` al dataset con los CSVs con la metadata correspondiente.

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
* GeoJSON: Formato JSON simple para especificar informacion geografica facilmente consumible.
 * http://geojson.org/
* TopoJSON: Extension de GeoJSON para manejar informacion topografica de manera compacta.
 * https://github.com/mbostock/topojson/wiki
* GML: Estandar del Open Geospatial Consortium normalizado en el estandar ISO 19136:2007.
 * http://www.opengeospatial.org/standards/gml
 * http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=32554

De momento los formatos mas utilizados son SHP, KML y GeoJSON. En la medida de lo posible es preferible ofrecer los datos en estos tres formatos.

#### Conversion entre formatos
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


#### Sistemas de referencia
El marco de referencia mas utilizado es WGS84 (EPSG 4326) con la proyeccion mercador Mercator (EPSG 3857).

El Instituto Geografico Nacional utiliza el Sistema de Referencia WGS 84 y el Marco de Referencia POSGAR 07 para los datos que libera.
* http://www.ign.gob.ar/sig

#### Validacion de archivos GeoJSON
Se recomienda utilizar alguna herramienta como la siguiente para asegurarse de que el formato del archivo GeoJSON se correcto
* http://geojsonlint.com/


### Estándares para fines especificos
* Open Budget
  * https://github.com/open-data-standards/data-schemas/blob/gh-pages/schemas/Open_Budget.md
* Building & Land Development Specification
  * http://permitdata.org/
  * https://github.com/open-data-standards/permitdata.org/wiki
* Varias
  * https://www.codeforamerica.org/our-work/data-formats/
