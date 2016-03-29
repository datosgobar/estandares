Anexo 1: Herramientas y referencias
===

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Referencias](#referencias)
  - [Formatos de archivos propiamente geográficos](#formatos-de-archivos-propiamente-geogr%C3%A1ficos)
  - [Estándares para fines específicos](#est%C3%A1ndares-para-fines-espec%C3%ADficos)
- [Validación](#validaci%C3%B3n)
  - [CSV](#csv)
  - [JSON](#json)
  - [GeoJSON](#geojson)
- [Conversión entre formatos](#conversi%C3%B3n-entre-formatos)
  - [Geográficos](#geogr%C3%A1ficos)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

En este anexo se consignan algunas referencias a herramientas útiles para convertir formatos o validar estándares, así como a discusiones que pueden clarificar la utilización de algunos de ellos.

Este anexo es un *trabajo en progreso*, de manera que no debe considerarse como completo.

# Referencias

## Formatos de archivos propiamente geográficos

* **SHP**: Es una especificacion abierta definida y manejada por la empresa Esri (Cuyo producto principal es el software propietario ArcGIS) - https://en.wikipedía.org/wiki/Shapefile
* **GeoJSON**: Formato JSON simple para especificar informacion geografica facilmente consumible. - http://geojson.org/
* **KML**: Formato abierto de información geográfica definido por Google - http://www.opengeospatial.org/standards/kml
* **TopoJSON**: Extensión de GeoJSON para manejar información topográfica de manera compacta. - https://github.com/mbostock/topojson/wiki
* **GML**: Estándar del Open Geospatial Consortium normalizado en el estándar ISO 19136:2007.
    - http://www.opengeospatial.org/standards/gml
    - http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=32554

## Estándares para fines específicos

* Open Budget
    - https://github.com/open-data-standards/data-schemas/blob/gh-pages/schemas/Open_Budget.md
* Building & Land Development Specification
    - http://permitdata.org/
    - https://github.com/open-data-standards/permitdata.org/wiki
* Varias
    - https://www.codeforamerica.org/our-work/data-formats/

# Validación

Se listan herramientas para validar el correcto formato de distintos tipos de archivos.

## CSV

Se recomienda el uso de alguna herramienta como csvlint para asegurarse de que el formato del CSV es correcto y eliminar los errores más básicos:

* http://csvlint.io/
* https://github.com/theodi/csvlint

## JSON
(**TODO**)

## GeoJSON
Se recomienda utilizar alguna herramienta como la siguiente para asegurarse de que el formato del archivo GeoJSON sea correcto:

* http://geojsonlint.com/

# Conversión entre formatos

## Geográficos

* **ogr2ogr**: Soporta varios formatos - https://www.gdal.org/ogr2ogr.html
    - **GeoJSON -> SHP**: http://gis.stackexchange.com/questions/68175/geojson-to-esri-shapefile-using-ogr2ogr
* **WKT -> GeoJSON**: Wellknown - https://github.com/mapbox/wellknown
* **WKT -> GeoJSON**: Shapely - http://lists.geojson.org/pipermail/geojson-geojson.org/2008-August/000459.html
* **SHP -> GeoJSON**: GDAL - http://ben.balter.com/2013/06/26/how-to-convert-shapefiles-to-geojson-for-use-on-github/


