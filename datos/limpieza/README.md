# Limpieza de Datos

## Estándares

### Fechas

* Los campos que expresen "fechas" se convierten al estándar ISO 8601 (**YYYY-MM-DDTHH:MM:SS[.mmmmmm][+HH:MM]**)
    - Ej.: **2016-02-05T14:53:00-03:00**
* Si sólo hay datos de año, mes y día, pero no hay de hora, se mantiene la primera parte del estándar
    - Ej.: **2016-02-05**

### Limpieza básica de strings

* **Nombres propios:** Incluyendo nombres de personas, direcciones, ciudades, países, organismos e instituciones. Se capitalizan (primera letra de cada palabra es mayúscula, el resto de las letras es minúscula)
* **Todos los strings**: Incluyendo todos los strings que no sean números ni fechas.
    - Normalización con algoritmo de OpenRefine *Method: Key Collision / Keying function: fingerprint*
* **Strings separables en múltiples campos:** Se separan en múltiples campos todos aquellos strings que puedan ser separables *con relativa seguridad* creando campos nuevos, pero se mantiene el campo original presente en el dataset.
    - Split simple con OpenRefine: Se identifica el separador y se crean nuevos campos a partir de un split.
    - Expresiones Regulares o Parsing Expression Grammars. Si la expresión regular es sencilla, se puede hacer en OpenRefine. Si no lo es, o se vuelve conveniente usar PEGs, se escribe un módulo ad-hoc en python estos casos.


### Limpieza avanzada de strings
(TODO)
    
