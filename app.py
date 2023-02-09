#!/usr/bin/python3
# import os, time, json
import sqlite3 as sql
from flask import Flask, render_template

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
            

@app.route('/') # Ruta principal.
def index():
    return render_template('index.html')

@app.route('/pedidos.html') # Ruta de pedidos.
def pedidos():
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = 'SELECT * FROM Pedidos' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    pedidosDB = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    return render_template('pedidos.html', pedidosDB=pedidosDB) # Devuelve la plantilla html y una variable con los pedidos.


app.run(debug=True) # Ejecutando programa en modo prueba.
