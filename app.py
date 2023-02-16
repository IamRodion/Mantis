#!/usr/bin/python3
import time, json
import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__) # Nombre de la app de flask
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
database = 'db/CPB.db' # Ruta de la base de datos

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

def obtenerFecha(): # Función que devuelve la fecha.
    fecha = f'{time.strftime("%d/%m/%Y")} {time.strftime("%H:%M:%S")}' # Obteniendo fecha y hora.
    return fecha # Devolviendo fecha completa            

def obtenerEstados(): # Función que obtienes los estados de los pedidos
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = 'SELECT Estado, count(*) FROM "Pedidos" group by Estado' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    estados = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    return estados # Devuelve la cantidad de pedidos por estados

@app.route('/', methods = ['GET']) # Ruta principal.
def index():
    if request.method == 'GET':
        return render_template('index.html', estados=obtenerEstados())

@app.route('/pedidos', methods = ['GET']) # Ruta de pedidos.
def pedidos():
    if request.method == 'GET':
        cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
        query = 'SELECT * FROM Pedidos' # Solicitud a realizar.
        cursor.execute(query) # Ejecutar una solicitud con el cursor.
        pedidosDB = cursor.fetchall() # Se vuelcan los datos en una variable.
        conn.commit() # Aplicar cambios.
        conn.close() # Cerrar conexión.
        return render_template('pedidos.html', pedidosDB=pedidosDB) # Devuelve la plantilla html y una variable con los pedidos.

@app.route('/nuevo_pedido', methods = ['GET','POST']) # Recibe los datos llenados en el formato para crear pedidos y lo registra en la base de datos.
def crearPedido(): # Función que registra un pedido en la base de datos. Argumentos necesarios: cliente=Nombre del cliente, total=total del coste de todas las ordenes, pedido=descripción de todas las ordenes.
    if request.method == 'GET':
        return render_template('nuevo_pedido.html')
    elif request.method == 'POST':
        cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
        cliente = request.form['cliente']
        fecha = obtenerFecha() # Obteniendo fecha.
        total = 10000
        estado = 'Pendiente'
        pedido = request.form['pedido']
        query = f'INSERT INTO Pedidos ("cliente", "fecha", "total", "estado", "pedido") VALUES("{cliente}", "{fecha}", {total}, "{estado}", "{pedido}")' # Solicitud a realizar.
        cursor.execute(query) # Ejecutar una solicitud con el cursor.
        conn.commit() # Aplicar cambios.
        conn.close() # Cerrar conexión.

        flash(['Se creó correctamente el pedido para el cliente', f'{cliente}'], 'Verde')
        return redirect(url_for('pedidos'))

@app.route('/ver_pedido/<id>')
def verPedido(id):
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = f'SELECT * FROM Pedidos WHERE id = {id}' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    pedidoDB = cursor.fetchall() # Se vuelcan los datos en una variable.
    if pedidoDB:
        conn.commit() # Aplicar cambios.
        conn.close() # Cerrar conexión.
        return render_template('ver_pedido.html', pedidoDB=pedidoDB)
    else:
        return render_template('index.html', mensaje='El id indicado no existe')

@app.route('/buscar_pedido', methods=['POST'])
def buscarPedido():
    dato = request.form['buscar']
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = f'SELECT * FROM Pedidos WHERE id like "%{dato}%" OR cliente like "%{dato}%"' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    pedidosDB = cursor.fetchall() # Se vuelcan los datos en una variable.
    if pedidosDB:
        conn.commit() # Aplicar cambios.
        conn.close() # Cerrar conexión
        return render_template('buscar_pedido.html', pedidosDB=pedidosDB, dato=dato)
    else:
        flash(['No se han encontrado pedidos con el valor ', f'{dato}'], 'Rojo')
        return redirect(url_for('index'))

@app.route('/ver_estado/<estado>')
def verEstado(estado):
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = f'SELECT * FROM Pedidos WHERE estado = "{estado}"' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    pedidosDB = cursor.fetchall() # Se vuelcan los datos en una variable.
    if pedidosDB:
        conn.commit() # Aplicar cambios.
        conn.close() # Cerrar conexión.
        return render_template('pedidos.html', pedidosDB=pedidosDB)
    else:
        return render_template('index.html', mensaje='El id indicado no existe')

app.run(debug=True) # Ejecutando programa en modo prueba.
