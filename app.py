#!/usr/bin/python3
import os, time, json
import sqlite3 as sql
from flask import Flask, render_template, request, redirect

app = Flask(__name__) # Nombre de la app de flask
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

@app.route('/') # Ruta principal.
def index():
    return render_template('index.html')

@app.route('/pedidos') # Ruta de pedidos.
def pedidos():
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
        fecha = obtenerFecha() # Obteniendo fecha.
        cliente = request.form['cliente']
        pedido = request.form['pedido']
        total = 10000
        query = f'INSERT INTO Pedidos ("cliente", "fecha", "total", "ordenes") VALUES("{cliente}", "{fecha}", {total}, "{pedido}")' # Solicitud a realizar.
        cursor.execute(query) # Ejecutar una solicitud con el cursor.
        conn.commit() # Aplicar cambios.
        conn.close() # Cerrar conexión.
        return redirect('/pedidos')

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
        return render_template('index.html', mensaje=f'No se encontraron pedidos con "{dato}"')


app.run(debug=True) # Ejecutando programa en modo prueba.
