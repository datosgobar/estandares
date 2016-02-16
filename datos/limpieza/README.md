Limpieza de Datos
===

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Estándares](#est%C3%A1ndares)
  - [Nombres de los campos](#nombres-de-los-campos)
  - [Fechas y horas](#fechas-y-horas)
  - [Limpieza básica de strings](#limpieza-b%C3%A1sica-de-strings)
  - [Limpieza avanzada de strings](#limpieza-avanzada-de-strings)
- [Herramientas](#herramientas)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Estándares

En las siguientes subsecciones se estipulan procedimientos de limpieza estándar que se aplican a todos los datasets.

### Nombres de los campos

* Los nombres de los campos deben renombrarse según la siguiente convención: palabras en minúsculas unidas por un guión bajo, utilizando únicamente caracteres ASCII (Ej.: *fecha_audiencia_solicitada*)

### Fechas y horas

* Los campos que expresen "fechas" y "horas" se convierten al estándar ISO 8601 (**YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM]**)
    - Ej.: **2016-02-05T14:53:00-03:00**
* Si sólo hay datos de año, mes y día, pero no hay de hora, se mantiene la primera parte del estándar
    - Ej.: **2016-02-05**
* Tanto si los campos de "fecha" y "hora" están separados, como si ambos datos están en un mismo campo, serán eliminados y reemplazados por un campo nuevo siguiendo el estándar ISO 8601 y se nombrarán de la siguiente manera:
    - *isodate_nombre_campo*: Para fechas sin hora.
    - *isodatetime_nombre_campo*: Para fechas que incluyen hora.
* En el caso menos probable de que se disponga de una "hora" pero no de una "fecha", se convierte al formato **HH:MM:SS**. No es necesario cambiar el nombre del campo en este caso.

### Limpieza básica de strings

Involucra tareas de limpieza locales, que no requieren de servicios externos al dataset ni uso de otros datasets.

* **Nombres propios:** Incluyendo nombres de personas, direcciones, ciudades, países, organismos e instituciones. Se capitalizan (primera letra de cada palabra es mayúscula, el resto de las letras es minúscula)
* **Todos los strings**: Incluyendo todos los strings que no sean números ni fechas.
    - Normalización con algoritmo de OpenRefine *Method: Key Collision / Keying function: fingerprint*. Se eligen todos los casos que marca el algoritmo por default.
* **Strings separables en múltiples campos:** Se separan en múltiples campos todos aquellos strings que puedan ser separables *con relativa seguridad* creando campos nuevos, pero se mantiene el campo original presente en el dataset.
    - Split simple con OpenRefine: Se identifica el separador y se crean nuevos campos a partir de un split.
    - Expresiones Regulares o Parsing Expression Grammars. Si la expresión regular es sencilla, se puede hacer en OpenRefine. Si no lo es, o se vuelve conveniente usar PEGs, se escribe un módulo ad-hoc en python para estos casos.

### Limpieza avanzada de strings

Involucra tareas de limpieza que requieren del uso de servicios externos al dataset o de los datos de otros datasets.

* **Normalización de campos geográficos**: (TODO)
* **Normalización de nombres de personas**: (TODO)
* **Normalización de nombres de instituciones**: (TODO)

## Herramientas

[TODO]
