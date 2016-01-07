# Style-Guide
Guía de estilo y estructuración de proyectos para equipos de la SSIPyGA. 

En este documento se fijan estándares mínimos para la producción de código y la gestión de proyectos de desarrollo. Se proveen templates y se sugieren herramientas adicionales para agilizar el trabajo bajo estos estándares.

## Convenciones generales

* Todo **código escrito en módulos** se escribe en **inglés**, salvo el caso de variables que representan *campos de una base de datos* que deben nombrarse en *español*.
* **README, issues, commits, docstrings y documentación** en general se escriben en **español**, a menos que el proyecto plantee una colaboración con desarrolladores no hispanoparlantes.
* Los **ipython notebooks** reúnen en un mismo documento código ejecutable y documentación. Debe preferirse el **inglés** para los bloques de código y el **español** para los bloques de documentación.
* Los **commits** deben ser *chicos y fácilmente abordables por un tercero*. Debe buscarse avanzar en la producción de código de manera incremental.
* En proyectos con 2 o más personas, el código nuevo debe trabajarse en una *branch* separada e incluirse en una *pull request* para ser revisado por un tercero antes de su incorporación definitiva al *master branch*.

## Python

### Guía de estilo: [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
* Todos los proyectos en python deben seguir la [guía de estilo de Google](https://google.github.io/styleguide/pyguide.html) para nombrar variables, nombrar métodos, documentar módulos, escribir docstrings, etc.
* Ver [ejemplo completo](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google) de un módulo en python según la guía de estilo de Google.

### Estructura de un proyecto en python

#### Templates

* [Ejemplo 1: con tests junto a sus módulos](python/Project-Example-1)
* [Ejemplo 2: con tests en una carpeta aparte](python/Project-Example-2)
* [Ejemplo 3: con scrapy](https://github.com/ssipyga/contratos_argentina)
* [Ejemplo 4: con django](https://github.com/chadad/propiedades)

#### Convenciones

* **requirements.txt**: todos los proyectos llevan un archivo *requirements.txt* en la root folder del proyecto. Este contiene la lista de dependencias utilizadas por los módulos del proyecto.
    - Si el proyecto incluye un *setup.py*, estas dependencias se instalarán al correr el comando `pip install -e .`
    - Si el proyecto no incluye un *setup.py*, estas dependencias deben instalarse corriendo el comando `pip install -r requirements.txt`

* **Tests**: todos los módulos escritos en python (`module.py`) deben tener un espejo (`test_module.py`) donde se escriben los tests (ver [template](python/Project-Example-1/package_name/test_project_euler.py)).
    - Los tests se estructuran según la [documentación de unittest](https://docs.python.org/2/library/unittest.html) y se corren con [nose](http://pythontesting.net/framework/nose/nose-introduction/) (En la línea de comandos: `$ nosetests`)
    - Todos los métodos públicos de un módulo `module.py` deben tener al menos un test en `test_module.py`. Deben testearse los casos especiales, así como algunos errores de input esperables por parte del cliente del método.
    - Los métodos privados (cuyo nombre debe comenzar con un **_**, para distinguirlos de los públicos) pueden omitir su test bajo las siguientes condiciones:
        + Son privados (no se espera que el cliente del módulo los use, son de uso interno dentro del módulo)
        + Son muy sencillos de entender y tienen pocas líneas.
        + Su funcionalidad está siendo testeada como parte de algún método público.

* **setup.py**: la inclusión de un *setup.py* es opcional, pero recomendable para proyectos grandes/complejos. Permite instalar el proyecto en el *path* del entorno virtual utilizado y utilizar importaciones absolutas como cualquier otra librería descargada de **pip**.
    - El proyecto se instala en el entorno virtual con `pip install -e .` (modo edición, sin crear una distribución) para poder editarlo sin instalarlo nuevamente.
    - Debe tenerse en cuenta que al agregar un paquete nuevo (una carpeta con un __init__.py en el interior) debe agregarse a la lista de la variable *packages* del *setup.py* y correr el comando de instalación nuevamente.
    - Un proyecto simple puede omitir el *setup.py* y desarrollarse con importaciones relativas. Aunque esta decisión debe reveerse si el proyecto se torna complejo.

### Linters en Sublime Text

Para observar los errores de estilo mientras se escribe código, es útil instalar algunos paquetes al Sublime Text con el [Package Control](https://packagecontrol.io/installation):

* **Anaconda** (contiene un linter automático que sigue las convenciones de PEP8)
* **PEP8 Autoformat**: Setear las preferencias con `"autoformat_on_save": true` (los errores más comunes se corrigen automáticamente cuando se guarda un archivo)

### Snippets en Sublime Text

Para iniciar la escritura de estructuras comunes, es muy útil el uso de *snippets* en Sublime. Estos permiten cargar el esqueleto de una estructura predefinida e ir completando las primeras partes haciendo *tabs*.

Para agregar snippets:

1. Tools > New Snippet
2. Copiar y pegar contenido del snippet

    *Estos snippets sólo funcionan en archivos de extensión .py*

    * [pyscript](python/snippets/pyscript.sublime-snippet): Tipear *pyscript*  para cargar un template de módulo nuevo en python.
    * [testmodule](python/snippets/testmodule.sublime-snippet): Tipear *testmodule* para cargar un template de módulo de testing en python.
    * [function](python/snippets/function.sublime-snippet): Tipear *function* para cargar un template de nuevo método con docstrings.
    * [objfunction](python/snippets/objfunction.sublime-snippet): Tipear *objfunction* para cargar un template de nuevo método de un objeto con docstrings.

Instalar paquetes estándares de snippets con el Package Control: **Sublime Text 3 Snippets** o **Sublime Text 2 Snippets**

## Iniciar un nuevo proyecto

Algunos aspectos de la estructuración de un repositorio pueden cambiar dependiendo del stack -más adelante se proveen templates para cada caso- pero todos deben respetar las siguientes indicaciones desde el momento en que se inicia un nuevo proyecto:

* **Nuevo canal en Slack**: Cada proyecto abre un nuevo canal en Slack, donde se comunican los miembros del equipo que participan del proyecto y se puede seguir el estado del mismo. El canal se integrará con:
    - *Travis CI*: para controlar que el proyecto se compila sin errores.
    - *Coveralls*: para controlar el % de cobertura de los tests del proyecto.
    - *Github*: para seguir los commits del equipo.

* **README**: Donde se listan:
    - El *objetivo* del proyecto
    - Un *ejemplo rápido* de uso
    - Las instrucciones de *instalación*
    - El resto de la documentación pertinente.

* **Integración continua con Travis CI**: Travis CI controla luego de cada push al repositorio que el proyecto puede compilarse en un entorno Linux sin errores. Es esencial para asegurar que:
    - Todas las *dependencias y requisitos de instalación* están documentados
    - Todos los tests pasan sin errores el último push
    - El código respeta la guía de estilo que sigue el equipo
Para integrar un repositorio con Travis CI:
    - Un archivo *.travis.yml* debe agregarse al repositorio con las configuraciones pertinentes (ver templates para cada lenguaje)
    - La integración continua del repositorio debe activarse en la cuenta de Travis CI del propietario

* **Waffle.io para gestionar los issues** (completar con cómo integrar Waffle!!)

## JavaScript
(TODO)

## HTML/CSS
(TODO)

