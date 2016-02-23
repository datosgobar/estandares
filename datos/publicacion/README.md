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
* Numeros: De acuerdo con lo definido por la W3C \[2\] se tendra en cuenta lo siguiente:
 * El separador decimal debe ser el caracter "."
 * Se admiten los siguientes valores especiales:
  * NaN: Indica que el valor no es un numero valido.
  * INF y -INF: En caso de que el valor tienda a mas o menos infinito respectivamente.
 * Se recomienda consultar la especificacion original en caso de de dudas sobre casos particulares.

Referencias:
\[1\]: http://tools.ietf.org/html/rfc4180 

\[2\]: https://www.w3.org/TR/tabular-data-model/ 

\[3\]: https://en.wikipedia.org/wiki/ISO_8601 

#### Validacion
Se recomienda el uso de alguna herramienta como csvlint para asegurarse que el formato del CSV es correcto y eliminar los errores obvios:
* http://csvlint.io/ 
* https://github.com/theodi/csvlint 

