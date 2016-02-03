
Project-Example-2
===

[![Coverage Status](https://coveralls.io/repos/abenassi/Project-Example-2/badge.svg?branch=master&service=github)](https://coveralls.io/github/abenassi/Project-Example-2?branch=master)
[![Build Status](https://travis-ci.org/abenassi/Project-Example-2.svg)](https://travis-ci.org/abenassi/Project-Example-2)
One liner que dice qué es el proyecto

Acá se escribe un párrafo o dos que describan un poco más el proyecto. Debe ser breve pero lo suficientemente explicativo para que el usuario entienda para qué sirve este proyecto, qué tipo de data toma y qué tipo de output o aplicación genera.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [One liner que dice qué es el proyecto](#one-liner-que-dice-qu%C3%A9-es-el-proyecto)
  - [Ejemplo](#ejemplo)
  - [Instalación](#instalaci%C3%B3n)
  - [Tests](#tests)
  - [Convenciones de estilo](#convenciones-de-estilo)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Ejemplo

En esta sección se muestra cómo usar el paquete con un ejemplo sencillo.

```python
import package_name
fib = package_name.fibonacci(20)
print fib
```

## Instalación

En esta sección se listan los pasos necesarios para instalar el paquete.

- Instalar Python 2.7 (se recomienda instalar [Anaconda](https://www.continuum.io/downloads))
- `brew install dependencia_para_mac` (instala primero cualquier dependencia necesaria)
- `conda create -n my_environment python=2` (crea un entorno virtual -copia limpia de python- donde instalar el proyecto con Anaconda)
- `source activate my_environment` (activa el entorno virtual)
- `pip install -e .` (instala el proyecto en modo edición: los packages listados en el *setup.py* se instalan en el path del entorno virtual de manera que permiten importaciones absolutas)
- `deactivate` (desactiva el entorno virtual)

Alternativamente, si no se utiliza Anaconda se puede usar *virtualenv* para crear entornos virtuales:

- `cd my_project`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -e .`
- `deactivate`

## Tests

En esta sección se muestra como correr los tests.

- `nosetests` (corre todos los tests)

## Convenciones de estilo

Este proyecto sigue las convenciones de la [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

Ver un ejemplo completo del [uso de docstrings en python según la guía de Google](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google)

