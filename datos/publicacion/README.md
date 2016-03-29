Publicación de Datos
===

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Introducción](#introducci%C3%B3n)
- [Aspectos Generales](#aspectos-generales)
  - [Codificación](#codificaci%C3%B3n)
  - [Tipo de Datos](#tipo-de-datos)
    - [String](#string)
    - [Número](#n%C3%BAmero)
    - [Tiempo](#tiempo)
    - [Booleano](#booleano)
  - [Nomenclatura](#nomenclatura)
    - [Campos](#campos)
    - [Archivos](#archivos)
- [Formatos](#formatos)
  - [Genéricos](#gen%C3%A9ricos)
    - [CSV](#csv)
    - [JSON](#json)
  - [Geográficos](#geogr%C3%A1ficos)
    - [Información geográfica simple](#informaci%C3%B3n-geogr%C3%A1fica-simple)
    - [Información geográfica embebida](#informaci%C3%B3n-geogr%C3%A1fica-embebida)
    - [SHP](#shp)
  - [Estadísticos](#estad%C3%ADsticos)
  - [Particulares](#particulares)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<!-- Referencias -->
[W3C]: https://www.w3.org/TR/tabular-data-model/
[rfc4180]: http://tools.ietf.org/html/rfc4180
[ISO8601]: https://en.wikipedía.org/wiki/ISO_8601

# Introducción

En este documento se estipulan estándares de publicación de recursos de datos. La definición de estos estándares es un *trabajo en progreso*, de manera que no deben considerarse como completos.

Otros estándares pueden ser aplicables para casos no previstos en el documento y se alienta a los usuarios a abrir *issues* con sugerencias, dudas y comentarios que aporten a la discusión de los mismos.

# Aspectos Generales

En esta sección se recomiendan estándares que aplican a una gran variedad de casos, independientemente del formato de publicación o la temática de los datos de que se trate.

## Codificación

* Todos los recursos de datos deben publicarse utilizando el charset **UTF-8** siguiendo las [recomendaciones de la W3C](https://www.w3.org/TR/tabular-data-model/#h-encoding).

## Tipo de Datos

El formato recomendado de los distintos tipos de datos está basado en la especificación de la [W3C][W3C].

### String

* **Nombres propios**: Se **capitalizan** (primera letra de cada palabra es mayúscula, el resto de las letras son minúsculas) todas las palabras significativas, salvo las siglas. Las palabras significativas son aquellas que no cumplen la función de artículos o preposiciones.
* **Siglas**: Van todas en **mayúsculas sin puntos**.
* Las **entidades** nombradas dentro de una columna deben tener una descripción única. Es decir que toda mención que se realice a una entidad dada debe hacerse utilizando **exactamente la misma cadena de caracteres**
    - Las descripciones de entidades deberían elegirse siempre de forma tal que cumplan con el **estándar específico que los describe**, en el caso de que exista.
    - Cuando este estándar no existe y hay dudas respecto del criterio a adoptar para elegir la descripción única de una entidad, debe privilegiarse siempre aquella que sea lo más **explícita, descriptiva y declarativa** posible.

**Ejemplo**:
```
nombre_ciudad
Ciudad Autónoma de Buenos Aires   >>   Ciudad Autónoma de Buenos Aires
CABA                              >>   Ciudad Autónoma de Buenos Aires
Capital Federal                   >>   Ciudad Autónoma de Buenos Aires
Ciudad de Buenos Aires            >>   Ciudad Autónoma de Buenos Aires
```

*En el ejemplo anterior, los 4 valores de texto refieren a la misma entidad. Debe elegirse una **única** forma de referirse a la misma y utilizarla en todos los casos.*

*En este caso se eligió la primera de ellas, siguiendo el criterio general, pero debería elegirse la **más adecuada** según el estándar establecido para ese tipo de entidad o el contexto del dataset de que se trate.*

### Número

Se tendrán en cuenta las siguientes convenciones para tratar con números:

* El separador decimal debe ser el caracter "**.**".
* No se utilizará separador de *miles*.
* Se admiten los siguientes valores especiales:
    - NaN: Indica que el valor no es un número válido.
    - INF y -INF: En caso de que el valor tienda a más o menos infinito respectivamente.
* Se recomienda consultar la especificación original en caso de de dudas sobre casos particulares.

### Tiempo

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

### Booleano

* A menos que se indique lo contrario, se identificarán con los valores **true** o **false**.
    - Esta convención puede variar en algunos rubros específicos de datos, pero en caso de no existir una convención clara y definida aplicable al rubro o contexto del dataset, se recomienda utilizar **true** o **false**.
* Tener en cuenta que este campo puede tener el valor **indefinido**.
* Si existe la posiblidad de que haya otro valor que no es **true**, **false** o **indefinido** significa que se eligió un tipo de datos incorrecto: este no es booleano, el tipo de dato booleano es binario y sólo admite 2 valores de verdad (aparte del caso del valor indefinido).

## Nomenclatura
### Campos

* Los campos deben separar las características de los datos en la forma más **desagregada que sea posible**. Se debe evitar definir campos que contengan más de un tipo de información (por ejemplo: *e-mail* y *sitio web*).
* Los **nombres de los campos** deben respetar la siguiente convención:
    - Utilizar palabras con caracteres siempre en **minúsculas**.
    - Utilizar palabras únicamente con **caracteres ASCII** comprendidos en el rango **a-z** y en el rango **0-9**.
    - Las palabras deben **unirse con guión bajo** ("** _ **").
    - Los nombres de los campos no deben contener espacios, ni ningún otro caracter que no sea **a-z**, **0-9** o **"_"**.
    - Las palabras deben separarse siempre con **" _ "**, en lugar de no tener separación alguna: *fecha_audiencia_solicitada* en lugar de *fechaaudienciasolicitada*
* Se debe buscar que los nombres de los campos sean lo más **explícitos, descriptivos y declarativos** como sea posible. Si bien debe buscarse también no generar nombres de campos excesivamente largos, es preferible que el nombre de un campo sea claro antes que sea corto. En este aspecto, sin embargo, pueden existir convenciones particulares según la temática o rubro de datos de que se trate. Siempre debe privilegiarse primero la convención de la temática específica y luego la convención general, caso de no existir una convención específica clara y ampliamente utilizada.

**Ejemplos**:

* *fecha_audiencia_solicitada*
* *year_2016*

### Archivos
(**TODO**)

# Formatos

En esta sección se cubren los estándares de publicación en formatos de 4 grandes categorías, de las cuáles una cubre la generalidad de los casos ([Genéricos](#genericos)), dos refieren a rubros específicos de gran importancia respecto a la cantidad de datos que se publican sobre ellos ([Geográficos](#geograficos) y [Estadísticos](#estadisticos)) y la última recoge otros casos particulares ([Particulares](#particulares)).

## Genéricos

En esta sección se recomiendan estándares para formatos abiertos de datos de amplia utilización y fácil reutilización por parte de distintos tipos de aplicaciones y procesos.

### CSV

Los archivos CSV son archivos de texto plano donde las columnas se separan por comas y las filas por saltos de línea. Algunas versiones alternativas de esta forma de publicar datos utilizan otros separadores.

Los estándares recomendados para la publicación de archivos CSV son:

* Las filas deben finalizar con los caracteres de "retorno de carro" (\r) y "salto de línea" (\n) unidos (**\r\n**), siguiendo lo indicado por el RFC4180 [RFC4180][rfc4180] y [W3C][W3C]. Esta forma de separar las líneas se denomina usualmente **CRLF** ("Carriage Return Line Feed").

* La **primera fila** siempre contiene los nombres de los campos.

* No se deben **repetir nombres** entre los campos.

* No se debe colocar **espacios** al principio o al final del nombre de un campo, o de un valor.

* Tanto los campos como los valores deben estar **separados por comas** ("**,**").

* En el caso de que un valor contenga el caracter separador ("**,**") o cualquiera de los caracteres que separan las líneas ("**\r**", "**\n**" o "**\r\n**"), el valor debe ser encerrado entre comillas dobles **""**. Esto indica que el caracter no cumple el rol de separar columnas o filas, sino que es parte de un valor.

**Ejemplo**:
```
col1,col2\r\n
"La tasa de Juan, está vacía",La tasa de Pablo está llena\r\n
"La tasa de Juan\nestá vacía",La tasa de Pablo está llena\r\n
"La tasa de Juan\r\nestá vacía",La tasa de Pablo está llena\r\n
```

* En el caso de que un valor contenga el caracter comilla doble (**"**), el valor debe ser encerrado entre comillas dobles como en el caso anterior (**""**) y, además, los caracteres comilla doble que se encuentren dentro del valor deben escribirse dos veces (**""**).

**Ejemplo**:
```
col1,col2\r\n
"La tasa de ""Juan"" está vacía",La tasa de Pablo está llena\r\n
```

* Para todos los tipos de datos se considera válido el valor indefinido. Este se expresará con la ausencia de todo caracter y no con un caracter o string especial como podrían ser ".", "null", "none", "nan", etc.

**Ejemplo**:
```
col1,col2,col3\r\n
a,,b\r\n
a,"",b\r\n
```
*En la primera línea el valor de la columna **col2** es indefinido, mientras que en la segunda línea se considera como un string vacío.*

### JSON
(**TODO**)

## Geográficos
(**TODO**)

### Información geográfica simple

* Si el dato que se quiere incluir es solo un punto indicado por su latitud y longitud se recomienda crear dos columnas "lat" y "lon" para dicho fin en lugar de utilizar un solo campo.

### Información geográfica embebida

* **GeoJSON**: Tiene la ventaja de que es fácil de utilizar o consumir.
* **WKT**: Lenguaje de mark-up para almacenar información geográfica utilizado por PostGIS entre otros. Definido incialmente por el Open Geospatial Consortium y luego extendido por la norma ISO/IEC 13249-3:2011.
* **WKB**: Versión binaria de WKT. Mucho más compacto.
* El formato **GeoJSON** es el preferido. En la medida de lo razonable convendria incluir además una columna con los mismos datos en formato WKT y WKB.

### SHP
(**TODO**)

## Estadísticos
(**TODO**)

## Particulares
(**TODO**)

