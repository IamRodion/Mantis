#Programa para hacer pruebas con los datos en la base de datos

import os, random, hashlib
import sqlite3 as sql
from faker import Faker

database = 'db/pruebaMantis.db'
# database = 'db/Mantis.db'

fake = Faker("es_CO")

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

def consultarDatos(query): # Función que realiza una consulta tomando como argumento una query SQL.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    respuesta = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    return respuesta # Se devuelven los datos recolectados.

def consultarScript(query): # Función que realiza una consulta tomando como argumento una query SQL.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    cursor.executescript(query) # Ejecutar una solicitud con el cursor.
    respuesta = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    return respuesta # Se devuelven los datos recolectados.


def limpiarPantalla(): # Función que limpia la pantalla.
    if os.name == 'posix': # Sí es un OS unix se ejecutará el comando "clear".
        os.system("clear")
    else: # En otros casos (windows), se ejecutará "cls".
        os.system("cls")

def generarOrden():
    productos = [["Juego de Cuellos Acrílico", 3800], ["Solo Cuello Acrílico", 2000], ["Solo Tira Acrílico", 2000], ["Juego de Cuello Letras", 5000], ["Cuello y Puño Letras", 6000], ["Solo Cuello Letras", 3500], ["Juego de Cuello Hilo", 4000], ["Solo Cuello Hilo", 2200], ["Juego Fajas Completo", 12000], ["Solo Faja Dobles", 6000], ["Cuello Redondo Doble", 4000]]
    producto = random.choice(productos)
    cantidad = random.randint(30, 101)
    precio = producto[1] * cantidad
    estado = random.choice(['Pendiente', 'En Producción', 'Terminado', 'Entregado'])
    prioridad = random.choice(['Alta', 'Media', 'Baja'])
    patron = 'O.verde.2-L.blanco.2-L.verde.2-F.blanco'
    orden = [producto[0], cantidad, precio, estado, prioridad, patron]
    return orden

def generarPedido():
    cliente = fake.name() # Función que genera un nombre aleatorio 
    fecha = str(fake.date_time()) # Obteniendo fecha.
    total = []
    comentarios = fake.text()
    ordenes = []
    for _ in range(random.randint(1, 5)):
        orden = generarOrden()
        ordenes.append(orden)
        total.append(orden[2])
    
    if [orden[3] for orden in ordenes].count('Pendiente') == len(ordenes):
        estado = 'Pendiente'
    elif [orden[3] for orden in ordenes].count('Terminado') == len(ordenes):
        estado = 'Terminado'
    elif [orden[3] for orden in ordenes].count('Entregado') == len(ordenes):
        estado = 'Entregado'
    else:
        estado = 'En Producción'
    
    pedido = [cliente, fecha, sum(total), estado, comentarios]
    return pedido, ordenes

def crearPedido(id): # Función que registra un pedido en la base de datos. Argumentos necesarios: cliente=Nombre del cliente, total=total del coste de todas las ordenes, pedido=descripción de todas las ordenes.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    pedido, ordenes = generarPedido()
    queryPedido = f'INSERT INTO Pedidos ("id", "cliente", "fecha", "total", "estado", "comentarios") VALUES ({id}, "{pedido[0]}", "{pedido[1]}", {pedido[2]}, "{pedido[3]}", "{pedido[4]}")'
    #queryID = f'SELECT max(id) FROM Pedidos'
    cursor.execute(queryPedido)# Ejecutar una solicitud con el cursor.
    for orden in ordenes:
        queryOrden = f'INSERT INTO Ordenes ("id_Pedidos", "producto", "cantidad", "precio", "estado", "prioridad", "patron") VALUES ({id}, "{orden[0]}", {orden[1]}, {orden[2]}, "{orden[3]}", "{orden[4]}", "{orden[5]}")'
        cursor.execute(queryOrden) # Ejecutar una solicitud con el cursor.
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

def buscarPedido(dato): # Función para buscar un pedido por número de pedido o por nombre del cliente.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = f'SELECT * FROM "Pedidos" WHERE id LIKE "%{dato}%" OR cliente LIKE "%{dato}%" ORDER BY id;' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    pedidos = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    return pedidos # Devuelve los datos recibidos.    

def mostrarEstado(): # Esta función cuenta la cantidad de pedidos por el estado en que están.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    query = 'SELECT Estado, count(*) FROM "Pedidos" group by Estado' # Solicitud a realizar.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    pedidos = cursor.fetchall() # Se vuelcan los datos en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    print(pedidos)


def verPedido(id):
    pedido = consultarDatos(f'SELECT * FROM Pedidos WHERE id = {id}')
    ordenes = consultarDatos(f'SELECT * FROM Ordenes WHERE id_Pedidos = {id}')
    return pedido, ordenes

def consultarUsuario(usuario, contraseña): # Función que revisa sí un usuario está en la base de datos.
    contraseña = hashlib.sha256(contraseña).hexdigest()
    query = f'SELECT * FROM Usuarios WHERE usuario="{usuario}" AND contraseña={contraseña}'
    if consultarDatos(query):
        return True
    else:
        return False

#for i in range(1, 201):
#    crearPedido(i)

# ---------Funciones para l manejo de la base de datos---------
    
TABLAS = """
CREATE TABLE IF NOT EXISTS "Usuarios" (
    "id" INTEGER NOT NULL UNIQUE,
    "usuario" VARCHAR NOT NULL,
    "contraseña" VARCHAR NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Productos" (
    "id" INTEGER NOT NULL UNIQUE,
    "nombre_producto" VARCHAR NOT NULL,
    "precio" INT DEFAULT 0,
    PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Pedidos" (
	"id" INTEGER NOT NULL UNIQUE,
	"cliente" TEXT NOT NULL,
	"fecha" TEXT NOT NULL,
	"total" NUMERIC NOT NULL DEFAULT 0,
	"estado" TEXT NOT NULL DEFAULT "Pendiente",
	"comentarios" TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Ordenes" (
	"id" INTEGER NOT NULL UNIQUE,
	"id_pedidos" INTEGER NOT NULL,
	"producto" TEXT NOT NULL,
	"cantidad" INTEGER NOT NULL,
	"precio" NUMERIC NOT NULL,
    "estado" TEXT NOT NULL DEFAULT 'Pendiente',
	"prioridad" TEXT NOT NULL DEFAULT 'Baja',
	"patron" TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_pedidos") REFERENCES "Pedidos"("id")
);"""

consultarScript(TABLAS)

# def crearTablaUsuarios():
#     QUERY = """
#     CREATE TABLE IF NOT EXISTS "Usuarios" (
#         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         usuario VARCHAR(255) NOT NULL PRIMARY KEY,
#         contraseña VARCHAR(255) NOT NULL
#     );"""
#     try:
#         consultarDatos(QUERY)
#         print('Se creo la tabla "Usuarios" correctamente.')
#     except:
#         print('No se pudo crear la tabla "Usuarios".')    

# def crearTablaProductos():
#     QUERY = """
#     CREATE TABLE IF NOT EXISTS "Productos" (
#         id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#         nombre_producto VARCHAR NOT NULL,
#         precio INT
#     );"""
#     try:
#         consultarDatos(QUERY)
#         print('Se creo la tabla "Productos" correctamente.')
#     except:
#         print('No se pudo crear la tabla "Productos".')

# def crearTablaPedidos():
#     QUERY = """
#     CREATE TABLE IF NOT EXISTS "Pedidos" (
#         "id"	INTEGER NOT NULL UNIQUE,
#         "cliente"	TEXT NOT NULL,
#         "fecha"	TEXT NOT NULL,
#         "total"	NUMERIC NOT NULL DEFAULT 0,
#         "estado"	TEXT NOT NULL DEFAULT 'Pendiente',
#         "comentarios"	TEXT,
#         PRIMARY KEY("id" AUTOINCREMENT)
#     );"""
#     try:
#         consultarDatos(QUERY)
#         print('Se creo la tabla "Pedidos" correctamente.')
#     except:
#         print('No se pudo crear la tabla "Pedidos".')

# def crearTablaOrdenes():
#     QUERY = """
#     CREATE TABLE IF NOT EXISTS "Ordenes" (
# 	    "id"	INTEGER NOT NULL UNIQUE,
# 	    "id_pedidos"	INTEGER NOT NULL,
# 	    "producto"	TEXT NOT NULL,
# 	    "cantidad"	INTEGER NOT NULL,
# 	    "precio"	NUMERIC NOT NULL,
#         "estado"	TEXT NOT NULL DEFAULT 'Pendiente',
# 	    "prioridad" TEXT NOT NULL DEFAULT 'Baja',
# 	    "patron"	TEXT NOT NULL,
# 	    PRIMARY KEY("id" AUTOINCREMENT),
# 	    FOREIGN KEY("id_Pedidos") REFERENCES "Pedidos"("id")
#     );"""
#     try:
#         consultarDatos(QUERY)
#         print('Se creo la tabla "Ordenes" correctamente.')
#     except:
#         print('No se pudo crear la tabla "Ordenes".')

# crearTablaProductos()
# crearTablaUsuarios()
# crearTablaOrdenes()
# crearTablaPedidos()