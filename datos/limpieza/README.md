Limpieza de Datos
===

## Campos

1. Se separan en múltiples campos todos aquellos strings que puedan ser separables *con relativa seguridad* creando campos nuevos, pero se mantiene el campo original presente en el dataset.
    - Split simple: Se identifica el separador y se crean nuevos campos a partir de un split.
    - Split en base a Expresiones Regulares o Parsing Expression Grammars. 
   
## Valores de texto (strings)

1. Se ponen en mayúscula todos los comienzos de palabra
2. Se vuelven a minúscula las preposiciones
3. Se identifican las siglas (con una búsqueda en un repositorio de siglas) y se las coloca todas en MAYÚSCULAS.
4. Se normaliza las cadenas con algoritmo de *Key Collision / Keying function: fingerprint*. Se eligen todos los casos que marca el algoritmo por default.


