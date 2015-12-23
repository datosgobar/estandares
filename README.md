# Project-Development-Guide
Guía de desarrollo de proyectos para equipos del Ministerio de Modernización de la Nación. 

En este documento se fijan estándares mínimos para la producción de código y la gestión de proyectos de desarrollo. Se proveen templates y se sugieren herramientas adicionales para agilizar el trabajo bajo estos estándares.

## Convenciones generales

* El código y sus comentarios escrito en módulos, se escribe en **inglés**.
* El README, los issues, los mensajes de los commits y la documentación en general, se escribe en **español**, a menos que el proyecto plantee una colaboración con desarrolladores de otros países no hispanoparlantes.
* El caso de los *ipython notebooks* plantea un uso mixto del idioma, ya que reúne en un mismo documento código ejecutable y documentación. Debe preferirse el **inglés** para los bloques de código y el **español** para los bloques de documentación.
* Los commits deben ser *chicos y fácilmente abordables por un tercero*. Debe buscarse avanzar en la producción de código de manera incremental, y realizar commits con avances mínimos que tengan una cierta unidad conceptual.
* En proyectos con 2 o más personas, el código nuevo debe trabjarse en una *branch* separada e incluirse en una *pull request* para ser revisado por un tercero antes de su incorporación definitiva al *master branch*.

## Iniciar un nuevo proyecto

Algunos aspectos de la estructuración de un repositorio pueden cambiar dependiendo del stack -más adelante se proveen templates para cada caso- pero todos deben respetar las siguientes indicaciones desde el momento en que se inicia un nuevo proyecto:

* **Nuevo canal en Slack**: Cada proyecto abre un nuevo canal en Slack, donde se comunican los miembros del equipo que participan del proyecto y se puede seguir el estado del mismo. El canal se integrará con:
    - *Travis CI*: para controlar que el proyecto se compila sin errores.
    - *Coveralls*: para controlar el % de cobertura de los tests del proyecto.
    - *Github*: para seguir los commits del equipo.

* **README**: Donde se listan:
    - El *objetivo* del proyecto
    - Las instrucciones de *instalación*
    - Un *ejemplo rápido* de uso
    - El resto de la documentación pertinente.

* **Integración continua con Travis CI**: Travis CI controla luego de cada push al repositorio que el proyecto puede compilarse en un entorno Linux sin errores. Es esencial para asegurar que:
    - Todas las *dependencias y requisitos de instalación* están documentados
    - Todos los tests pasan sin errores el último push
    - El código respeta la guía de estilo que sigue el equipo
Para integrar un repositorio con Travis CI:
    - Un archivo *.travis.yml* debe agregarse al repositorio con las configuraciones pertinentes (ver templates para cada lenguaje)
    - La integración continua del repositorio debe activarse en la cuenta de Travis CI del propietario

* **Waffle.io para gestionar los issues** (completar con cómo integrar Waffle!!)

## Python

Los proyectos en python deben seguir las convenciones de la [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html). Ver un ejemplo completo del [uso de docstrings en python según la guía de Google](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google)

*Linters en Sublime Text*

Para corregir los errores de estilo mientras se escribe código, es útil instalar algunos paquetes al Sublime Text con el [Package Control](https://packagecontrol.io/installation):

* **Anaconda** (contiene un linter automático que sigue las convenciones de PEP8)
* **PEP8 Autoformat**: Setear las preferencias con `"autoformat_on_save": true` (los errores más comunes se corrigen automáticamente cuando se guarda un archivo)

*Snippets en Sublime Text*

Para iniciar la escritura de estructuras comunes, es muy útil el uso de *snippets* en Sublime. Estos permiten cargar el esqueleto de una estructura predefinida e ir completando las primeras partes haciendo *tabs*.

1. Tools > New Snippet
2. Copiar y pegar contenido

    * [pyscript](python/snippets/pyscript.sublime-snippet): Tipear *pyscript* en un nuevo archivo de extensión .py para cargar un template de módulo nuevo en python.
    * [testmodule](python/snippets/testmodule.sublime-snippet): Tipear *testmodule* en un nuevo archivo de extensión .py para cargar un template de módulo de testing en python.

Instalar paquetes estándares de snippets con el Package Control: **Sublime Text 3 Snippets** o **Sublime Text 2 Snippets**

*Convenciones para proyectos en python*

* Los repositorios deben ser estructurados como muestra el [template](python/Project-Name)

* **setup.py**: el template muestra el caso de un proyecto que incluye un archivo *setup.py*, este permite instalar los *packages* del proyecto en el *path* del entorno virtual donde lo instalemos. 
    - Instalar el paquete permite realizar importaciones absolutas desde cualquier módulo del proyecto (tal como haríamos cuando usamos un paquete instalado haciendo *pip install package_name*) lo que simplifica el código en proyectos medianos y grandes. 
    - Siguiendo las intrucciones del *README* de ejemplo en el template, el proyecto debe instalarse en el entorno virtual mediante `pip install -e .` para poder editarlo sin instalarlo nuevamente.
    - Debe tenerse en cuenta que al agregar un paquete nuevo (una carpeta con un __init__.py en el interior) debe agregarse a la lista de la variable *packages* del *setup.py* y correr el comando de instalación nuevamente.
    - Un proyecto muy simple puede omitir el archivo *setup.py* y desarrollarse con importaciones relativas, aunque esta decisión debe reverse si la complejidad del proyecto lo hace deseable.

* **requirements.txt**: todos los proyectos en python tienen un archivo *requirements.txt* en la root folder del proyecto. Este contiene la lista de dependencias utilizadas por los módulos del proyecto.
    - Si el proyecto incluye un *setup.py*, estas dependencias se instalarán al correr el comando `pip install -e .`
    - Si el proyecto no incluye un *setup.py*, estas dependencias deben instalarse corriendo el comando `pip install -r requirements.txt`

* **Tests**: todos los módulos escritos en python (`module.py`) deben tener un espejo (`test_module.py`) donde se escriben los tests (ver [template](python/Project-Name/package_name/test_project_euler.py)).
    - Los tests se estructuran según la [documentación de unittest](https://docs.python.org/2/library/unittest.html) y se corren con [nose](http://pythontesting.net/framework/nose/nose-introduction/)
    - Todos los métodos públicos de un módulo `module.py` deben tener al menos un test en `test_module.py`. Deben testearse los casos especiales, así como algunos errores de input esperables por parte del usuario del método.
    - Los métodos privados (cuyo nombre debe comenzar con un **_**, para distinguirlos de los públicos) pueden omitir su test bajo las siguientes condiciones:
        + Son privados (no se espera que el usuario del módulo los use, son sólo para uso interno dentro del módulo)
        + Son muy sencillos de entender y no tienen más de unas pocas líneas.
        + Su funcionalidad está siendo testeada como parte de algún otro método.
    - Para la mayoría de los proyectos bastará la convención general de colocar el `test_module.py` en el mismo directorio que `module.py` (que es la estructura sugerida en el template). Para proyectos más complejos puede ser conveniente mover todos los tests a una carpeta **tests** en la root folder del proyecto, cuya estructura replica la estructura del proyecto. 
        + En este caso se requiere el uso de un *setup.py* ya que la única forma de estructurar los tests de esta manera es con importaciones absolutas.

## JavaScript

## HTML/CSS

