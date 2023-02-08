#Programa para hacer pruebas con los datos en la base de datos

import os, time, json
import sqlite3 as sql

database = 'db/CPB.db'

def crearCursor(database): # Genera un objeto cursor a traves de una base de datos.
    conn = None
    try: # Intenta conectarse a la base de datos.
        conn = sql.connect(database) # Establece conexión con la base de datos, y en caso de no existir, la crea.
    except sql.Error as error: # En caso de no lograr conectar a la DB mostrará el error por pantalla.
        print(error)
    finally: # En caso de lograr conectar, generará el objeto cursor y lo devolverá a traves de return.
        if conn:
            cursor = conn.cursor()
            return cursor, conn # Devuelve el objeto cursor y el objeto conn para cerrar la conexión a la base de datos al final

def limpiarPantalla(): # Función que limpia la pantalla.
    if os.name == 'posix': # Sí es un OS unix se ejecutará el comando "clear".
        os.system("clear")
    else: # En otros casos (windows), se ejecutará "cls".
        os.system("cls")

def obtenerFecha(): # Función que devuelve la fecha.
    fecha = f'{time.strftime("%d/%m/%Y")} {time.strftime("%H:%M:%S")}' # Obteniendo fecha y hora.
    return fecha # Devolviendo fecha completa.

def crearPedido(cliente, total, pedido): # Función que registra un pedido en la base de datos. Argumentos necesarios: cliente=Nombre del cliente, total=total del coste de todas las ordenes, pedido=descripción de todas las ordenes.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    fecha = obtenerFecha() # Obteniendo fecha.
    query = f'INSERT INTO Pedidos ("cliente", "fecha", "total", "ordenes") VALUES("{cliente}", "{fecha}", {total}, "{pedido}")' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.

def verPedidos(): # Función que consulta los pedidos en la tabla "pedidos" de la base de datos.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = 'SELECT * FROM Pedidos' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    pedidos = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.

    return pedidos # Devuelve los datos recibidos.

def modificarPedido(id):
    pass

def borrarPedido(id): # Función para borrar un medido de la tabla pedidos a través del ID
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = f'DELETE FROM Pedidos WHERE id={id}' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.


pedido = '[["Juego de Cuellos Acrílico",30,114000,"O.verde.2-L.blanco.2-L.verde.2-F.blanco"],["Juego de Cuellos Acrílico",30,114000,"O.verde.2-L.blanco.2-L.verde.2-F.blanco"]]'
crearPedido("John Doe", 172000, pedido)

pedidos = verPedidos()

for i in pedidos:
    print(i)