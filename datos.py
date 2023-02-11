#Programa para hacer pruebas con los datos en la base de datos

import os, time, json, random
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

def generarCliente():
    nombres = ["María", "José", "Luis", "Luz", "Ana", "Carlos", "Juan", "Jorge", "Martha", "Sandra", "Gloria", "Blanca", "Rosa", "Carmen", "Pedro", "Jesús", "Claudia", "Diana", "Óscar", "Manuel"]
    apellidos = ["Rodriguez", "Martinez", "Garcia", "Gomez", "Lopez", "Gonzalez", "Hernandez", "Sanchez", "Perez", "Ramirez", "Alvarez", "Torres", "Muñoz", "Rojas", "Moreno", "Vargas", "Ortiz", "Jimenez", "Castro", "Gutierrez"]
    cliente = f'{random.choice(nombres)} {random.choice(apellidos)}'
    return cliente

def generarPedido():
    productos = [["Juego de Cuellos Acrílico", 3800], ["Solo Cuello Acrílico", 2000], ["Solo Tira Acrílico", 2000], ["Juego de Cuello Letras", 5000], ["Cuello y Puño Letras", 6000], ["Solo Cuello Letras", 3500], ["Juego de Cuello Hilo", 4000], ["Solo Cuello Hilo", 2200], ["Juego Fajas Completo", 12000], ["Solo Faja Dobles", 6000], ["Cuello Redondo Doble", 4000]]
    producto = random.choice(productos)
    cantidad = random.randint(1, 51)
    totales = producto[1] * cantidad
    patron = 'O.verde.2-L.blanco.2-L.verde.2-F.blanco'
    pedido = f'producto: {producto[0]}, cantidad: {cantidad}, total: {totales}, patrón: {patron}'
    return totales, pedido

def crearPedido(): # Función que registra un pedido en la base de datos. Argumentos necesarios: cliente=Nombre del cliente, total=total del coste de todas las ordenes, pedido=descripción de todas las ordenes.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    cliente = generarCliente() # Función que genera un nombre aleatorio 
    fecha = obtenerFecha() # Obteniendo fecha.
    total, pedido = generarPedido() #Función que genera un pedido aleatorio 
    estado = 'Pendiente'
    query = f'INSERT INTO Pedidos ("cliente", "fecha", "total", "estado", "pedido") VALUES("{cliente}", "{fecha}", {total}, "{estado}", "{pedido}")' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    print(query)

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

def buscarPedido(dato): # Función para buscar un pedido por número de pedido o por nombre del cliente.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = f'SELECT * FROM "Pedidos" WHERE id LIKE "%{dato}%" OR cliente LIKE "%{dato}%" ORDER BY id;' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    pedidos = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.

    return pedidos # Devuelve los datos recibidos.    

for i in range(30):
    crearPedido()