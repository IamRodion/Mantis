#!/usr/bin/python3

# Programa creado por Rodion (github.com/IamRodion)

# -------------Importando librerías-------------
import time, json
import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for, flash


# -------------Definiendo objetos, atributos y variables-------------
app = Flask(__name__) # Nombre de la app de flask.
app.secret_key = 'sj8rnNECUDy6ZD7' # Clave secreta para el correcto funcionamiento de la función flash. En caso de borrarla generará el error "RuntimeError: The session is unavailable because no secret key was set. Set the secret_key on the application to something unique and secret".
database = 'db/CPB.db' # Ruta de la base de datos.


# -------------Definiendo funciones-------------
def obtenerFecha(): # Función que devuelve la fecha y hora en formato "14/02/2023 21:20:53".
    fecha = f'{time.strftime("%d/%m/%Y")} {time.strftime("%H:%M:%S")}' # Obteniendo fecha y hora.
    return fecha # Devolviendo fecha y hora.

def crearCursor(database): # Genera un objeto cursor a traves de una base de datos.
    conn = None
    try: # Intenta conectarse a la base de datos.
        conn = sql.connect(database) # Establece conexión con la base de datos, y en caso de no existir, la crea.
    except sql.Error as error: # En caso de no lograr conectar a la DB mostrará el error por pantalla.
        print(error)
    finally: # En caso de lograr conectar, generará el objeto cursor y lo devolverá a traves de return.
        if conn:
            cursor = conn.cursor()
            return cursor, conn # Devuelve el objeto cursor y el objeto conn para cerrar la conexión a la base de datos al final.

def consultarQuery(query): # Función que realiza una consulta tomando como argumento una query SQL.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    respuesta = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    return respuesta # Se devuelven los datos recolectados.

def obtenerEstados(): # Función que obtiene los pedidos agrupados por estado.
    query = 'SELECT Estado, count(*) FROM Pedidos group by Estado' # Solicitud a realizar.
    estados = consultarQuery(query) # Se vuelcan los datos en una variable..
    return estados # Devuelve la cantidad de pedidos por cada estado.


# -------------Definiendo rutas-------------
@app.route('/', methods = ['GET']) # Ruta principal.
def index():
    if request.method == 'GET':
        return render_template('index.html', estados=obtenerEstados()) # Devuelve la plantilla de la página principal, junto la cantidad de pedidos por estado.

@app.route('/pedidos', methods = ['GET']) # Ruta para ver los pedidos.
def pedidos():
    if request.method == 'GET':
        query = 'SELECT * FROM Pedidos' # Solicitud a realizar.
        pedidosDB = consultarQuery(query) # Se vuelcan los datos en una variable.
        return render_template('pedidos.html', pedidosDB=pedidosDB) # Devuelve la plantilla html y una variable con los pedidos.

@app.route('/nuevo_pedido', methods = ['GET','POST']) # Ruta que entrega la plantilla para crear un pedido (GET) y para enviar los datos del pedido nuevo a la base de datos (POST).
def crearPedido():
    if request.method == 'GET': # Cuando se solicita la plantilla html para crear un pedido.
        return render_template('nuevo_pedido.html') # Devolver la plantilla que contiene el formulario a llenar.
    elif request.method == 'POST': # Cuando se está devolviendo la plantilla con los valores completados.
        cliente = request.form['cliente'] # Se obtiene el cliente indicado por el usuario en la plantilla.
        fecha = obtenerFecha() # Obteniendo fecha y hora del momento en que se realiza el registro.
        total = 10000 # Valor temporal para el total, se cambiará cuando la plantilla devuelva el total.
        estado = 'Pendiente' # Valor default para el pedido será siempre "Pendiente".
        pedido = request.form['pedido'] # Se obtiene el pedido indicado por el usuario en la plantilla.
        query = f'INSERT INTO Pedidos ("cliente", "fecha", "total", "estado", "pedido") VALUES("{cliente}", "{fecha}", {total}, "{estado}", "{pedido}")' # Solicitud a realizar.
        consultarQuery(query) # Ejecutar una solicitud SQL.

        flash(['Se creó correctamente el pedido para el cliente', f'{cliente}'], 'Verde') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('pedidos')) # Se redirige al usuario a la ruta '/pedidos'.

@app.route('/ver_pedido/<id>') # Ruta que muestra un pedido en específico.
def verPedido(id): # El argumento es el id del caso a mostrar.
    query = f'SELECT * FROM Pedidos WHERE id = {id}' # Solicitud a realizar.
    pedidoDB = consultarQuery(query) # Ejecutar una solicitud SQL, guardar el resultado en una variable.
    if pedidoDB: # Sí la consulta arroja resultados.
        return render_template('ver_pedido.html', pedidoDB=pedidoDB) # Devuelve la plantilla html y una variable con el pedido.
    else: # Sí la consulta no arroja resultados.
        flash(['No se encontraron pedidos con el id', f'{id}'], 'Rojo') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('pedidos')) # Se redirige al usuario a la ruta '/pedidos'.

@app.route('/buscar_pedido', methods=['POST']) # Ruta que muestra los pedidos que contienen el dato buscado por el usuario.
def buscarPedido():
    dato = request.form['buscar'] # Se obtiene el dato a buscar indicado por el usuario en la plantilla.
    query = f'SELECT * FROM Pedidos WHERE id like "%{dato}%" OR cliente like "%{dato}%"' # Solicitud a realizar.
    pedidosDB = consultarQuery(query) # Ejecutar una solicitud SQL, guardar el resultado en una variable.
    if pedidosDB: # Sí la consulta arroja resultados.
        return render_template('buscar_pedido.html', pedidosDB=pedidosDB, dato=dato) # Devuelve la plantilla html, una variable con el pedido y otra con el dato buscado.
    else: # Sí la consulta no arroja resultados.
        flash(['No se han encontrado pedidos con el valor ', f'{dato}'], 'Rojo') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('index')) # Se redirige al usuario a la ruta '/'.

@app.route('/ver_estado/<estado>') # Ruta que muestra todos los pedidos que se encuentran en un estado indicado.
def verEstado(estado):
    query = f'SELECT * FROM Pedidos WHERE estado = "{estado}"' # Solicitud a realizar.
    pedidosDB = consultarQuery(query) # Ejecutar una solicitud SQL, guardar el resultado en una variable.
    if pedidosDB: # Sí la consulta arroja resultados.
        return render_template('pedidos.html', pedidosDB=pedidosDB) # Devuelve la plantilla html y una variable con los pedidos.
    else: # Sí la consulta no arroja resultados.
        flash(['No se han encontrado pedidos con el estado ', f'{estado}'], 'Rojo') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('index')) # Se redirige al usuario a la ruta '/'.

app.run(debug=True) # Ejecutando programa en modo prueba.