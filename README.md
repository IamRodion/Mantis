<div align="center">
<img style="width: 60px;" src="static/Image/Mantis Purpura y Verde.svg"/>
</div>

# Mantis
Mantis es un programa web creado en Python con el framework Flask, para la gestión de pedidos de micro-empresas.


## Instalación

```
git clone https://github.com/IamRodion/Mantis.git
```
```
cd Mantis/
```
```
pip3 install -r requirements.txt
```
```
python3 app.py
```

## Requisitos

Para que el programa funcione correctamente, será **necesario instalar** las siguientes **librerias**:

* [flask](https://pypi.org/project/Flask/ "Ir a flask en PyPI"): Framework web que gestiona el servidor.
* sqlite3: Gestor de base de datos, instalado por defecto en Python.
* time: Librería para gestionar fechas y horas, instalada por defecto en Python.

Todas las librerías necesarias se instalarán en el paso 3 de la instalación:
```
pip install -r requirements.txt
```

## Como usarlo
Dentro del archivo app.py, se puede configurar el puerto en el que se ejecutará la aplicación.

```py
app.run(debug=True, host='0.0.0.0', port=8000)
```

El modo de pruebas puede ser desactivado y el puerto puede ser modificado al 80 sí lo desea, quedando de la siguiente forma:

```py
app.run(host='0.0.0.0', port=80)
```

## Recursos Utilizados

[Python 3](https://www.python.org/): Lenguaje de programación.

[SQLite](https://sqlite.org/index.html): Gestor de base de datos.

[Flask](https://flask.palletsprojects.com/en/2.2.x/): Framework de desarrollo web.

[Bootstrap 5](https://getbootstrap.com/): Librería de estilos CSS.

[Bootswatch](https://bootswatch.com/cyborg/): Plantillas de estilos CSS.

[MingCute](https://www.mingcute.com/): Librería de íconos de código abierto.

[icooon-mono.com](https://icooon-mono.com/13825-%e3%82%ab%e3%83%9e%e3%82%ad%e3%83%aa%e3%82%a2%e3%82%a4%e3%82%b3%e3%83%b31/?): Logos en SVG.