#!/usr/bin/python3

# Programa creado por Rodion (github.com/IamRodion)

# -------------Importando librerías-------------
import time, hashlib
import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for, flash


# -------------Definiendo objetos, atributos y variables-------------
app = Flask(__name__) # Nombre de la app de flask.
app.secret_key = 'sj8rnNeCUDy6ZD7' # Clave secreta para el correcto funcionamiento de la función flash. En caso de borrarla generará el error "RuntimeError: The session is unavailable because no secret key was set. Set the secret_key on the application to something unique and secret".
database = 'db/Mantis.db' # Ruta de la base de datos.


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

def consultarDato(query): # Función que realiza una consulta tomando como argumento una query SQL.
    cursor, conn = crearCursor(database) # Creando cursor y conexión con la base de datos.
    cursor.execute(query) # Ejecutar una solicitud con el cursor.
    respuesta = cursor.fetchone() # Se vuelcan el dato en una variable.
    conn.commit() # Aplicar cambios.
    conn.close() # Cerrar conexión.
    return respuesta # Se devuelven los datos recolectados.

def consultarPorcentaje(tabla, columna, consulta):
    cantidad = consultarDato(f'SELECT IFNULL(COUNT(*), 0) FROM {tabla} WHERE {columna}="{consulta}"')[0]
    total = consultarDato(f'SELECT IFNULL(COUNT(*), 0) FROM {tabla}')[0]

    if cantidad == 0:
        return 0
    else:
        porcentaje = cantidad * 100 / total
        return round(porcentaje, 1)


def obtenerPedidos(): # Función que devuelve un diccionario con la cantidad de pedidos por estado.
    pedidos = {
        "Total": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Pedidos')[0],

        "Pendiente": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Pedidos WHERE estado="Pendiente"')[0],
        "En Producción": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Pedidos WHERE estado="En Producción"')[0],
        "Terminado": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Pedidos WHERE estado="Terminado"')[0],
        "Entregado": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Pedidos WHERE estado="Entregado"')[0],

        "Porcentaje Pendiente": consultarPorcentaje("Pedidos", "estado", "Pendiente"),
        "Porcentaje En Producción": consultarPorcentaje("Pedidos", "estado", "En Producción"),
        "Porcentaje Terminado": consultarPorcentaje("Pedidos", "estado", "Terminado"),
        "Porcentaje Entregado": consultarPorcentaje("Pedidos", "estado", "Entregado")
    }

    return pedidos

def obtenerOrdenes(): # Función que devuelve un diccionario con la cantidad de ordenes por prioridad.
    ordenes = {
        "Total": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes')[0],

        "Pendiente": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE estado="Pendiente"')[0],
        "En Producción": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE estado="En Producción"')[0],
        "Terminado": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE estado="Terminado"')[0],
        "Entregado": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE estado="Entregado"')[0],
        "Porcentaje Pendiente": consultarPorcentaje("Ordenes", "estado", "Pendiente"),
        "Porcentaje En Producción": consultarPorcentaje("Ordenes", "estado", "En Producción"),
        "Porcentaje Terminado": consultarPorcentaje("Ordenes", "estado", "Terminado"),
        "Porcentaje Entregado": consultarPorcentaje("Ordenes", "estado", "Entregado"),


        "Alta": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE prioridad="Alta"')[0],
        "Media": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE prioridad="Media"')[0],
        "Baja": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE prioridad="Baja"')[0],
        "Porcentaje Alta": consultarPorcentaje("Ordenes", "prioridad", "Alta"),
        "Porcentaje Media": consultarPorcentaje("Ordenes", "prioridad", "Media"),
        "Porcentaje Baja": consultarPorcentaje("Ordenes", "prioridad", "Baja")
    }

    return ordenes

def consultarUsuario(usuario, contraseña): # Función que revisa sí un usuario está en la base de datos.
    query = f'SELECT * FROM Usuarios WHERE usuario="{usuario}" AND contraseña={contraseña}'
    if consultarQuery(query):
        return True
    else:
        return False


# -------------Definiendo rutas principales-------------
@app.route('/') # Ruta principal.
def index():
    datos = { # Datos a mostrar en la página.
        'pestaña': 'Mantis',
        'titulo': 'Mantis'
        }
    return render_template('pagina_principal/pagina_principal.html', datos=datos) # Devuelve la plantilla de la página principal, junto la cantidad de pedidos por estado.

@app.route('/recepcion')
def recepcion():
    datos = {
        'pestaña': 'Recepción',
        'titulo': 'Recepción'
    }
    return render_template('recepcion/recepcion.html', datos=datos)

@app.route('/produccion')
def produccion():
    datos = {
        'pestaña': 'Producción',
        'titulo': 'Producción'
    }
    return render_template('produccion/produccion.html', datos=datos)

@app.route('/administracion')
def administracion():
    datos = {
        'pestaña': 'Administración',
        'titulo': 'Administración'
    }
    return render_template('administracion/administracion.html', datos=datos)

@app.route('/usuario')
def usuario():
    datos = {
        'pestaña': 'Usuario',
        'titulo': 'Usuario'
    }
    return render_template('usuario/usuario.html', datos=datos)

# -------------Definiendo rutas secundarias-------------
@app.route('/estadisticas') # Ruta principal.
def estadisticas():
    datos = { # Datos a mostrar en la página.
        'pestaña': 'Estadísticas',
        'titulo': 'Estadísticas',
        'pedidos': obtenerPedidos(),
        'ordenes': obtenerOrdenes()
        }
    return render_template('pagina_principal/estadisticas.html', datos=datos) # Devuelve la plantilla de la página principal, junto la cantidad de pedidos por estado.

@app.route('/acerca_de') # Ruta principal.
def acercaDe():
    datos = { # Datos a mostrar en la página.
        'pestaña': 'Acerca De',
        'titulo': 'Acerca De'
        }
    return render_template('pagina_principal/acerca_de.html', datos=datos) # Devuelve la plantilla de la página principal, junto la cantidad de pedidos por estado.


@app.route('/pedidos') # Ruta para ver los pedidos.
def pedidos():
    datos = { # Datos a mostrar en la página.
        'pestaña': 'Pedidos',
        'titulo': 'Pedidos',
        'pedidos': consultarQuery('SELECT id, cliente, fecha, total, estado FROM Pedidos'),
        "total": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Pedidos')[0]
        }
    return render_template('recepcion/pedidos.html', datos=datos) # Devuelve la plantilla html y una variable con los pedidos.

@app.route('/ordenes') # Ruta para ver las ordenes.
def ordenes():
    datos = { # Datos a mostrar en la página.
        'pestaña': 'Ordenes',
        'titulo': 'Ordenes',
        'ordenes': consultarQuery('SELECT id, id_Pedidos, producto, cantidad, precio, estado, prioridad, patron FROM Ordenes'),
        "total": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes')[0]
        }
    return render_template('recepcion/ordenes.html', datos=datos) # Devuelve la plantilla html y una variable con los pedidos.

@app.route('/nuevo_pedido', methods = ['GET','POST']) # Ruta que entrega la plantilla para crear un pedido (GET) y para enviar los datos del pedido nuevo a la base de datos (POST).
def crearPedido():
    if request.method == 'GET': # Cuando se solicita la plantilla html para crear un pedido.
        query = 'SELECT * FROM Productos'
        productos = consultarQuery(query)
        datos = { # Datos a mostrar en la página.
            'pestaña': 'Nuevo Pedido',
            'titulo': 'Nuevo Pedido',
            'productos': productos
            }
        return render_template('recepcion/nuevo_pedido.html', datos=datos) # Devolver la plantilla que contiene el formulario a llenar.
        
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

@app.route('/pedidos/<id>') # Ruta que muestra un pedido en específico.
def verPedido(id): # El argumento es el id del caso a mostrar.
    pedido = consultarDato(f'SELECT * FROM Pedidos WHERE id = {id}') # Ejecutar una solicitud SQL, guardar el resultado en una variable.
    if pedido: # Sí la consulta arroja resultados.
        datos = { # Datos a mostrar en la página.
            'pestaña': f'Pedido #{id}',
            'titulo': f'Pedido #{id}',
            'pedido': consultarDato(f'SELECT id, cliente, fecha, total, estado, comentarios FROM Pedidos WHERE id = {id}'),
            'ordenes': consultarQuery(f'SELECT id, producto, cantidad, precio, estado, prioridad, patron FROM Ordenes WHERE id_Pedidos = {id}')
            }
        return render_template('recepcion/pedido.html', datos=datos) # Devuelve la plantilla html y una variable con el pedido.
    else: # Sí la consulta no arroja resultados.
        flash(['No se encontraron pedidos con el #', f'{id}'], 'Rojo') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('pedidos')) # Se redirige al usuario a la ruta '/pedidos'.

@app.route('/buscar_pedido', methods=['POST']) # Ruta que muestra los pedidos que contienen el dato buscado por el usuario.
def buscarPedido():
    buscar = request.form['buscar'] # Se obtiene el dato a buscar indicado por el usuario en la plantilla.
    query = f'SELECT * FROM Pedidos WHERE id like "%{buscar}%" OR cliente like "%{buscar}%"' # Solicitud a realizar.
    pedidos = consultarQuery(query) # Ejecutar una solicitud SQL, guardar el resultado en una variable.
    if pedidos: # Sí la consulta arroja resultados.
        datos = { # Datos a mostrar en la página.
            'pestaña': f'Buscar "{buscar}"',
            'titulo': f'Pedidos encontrados con "{buscar}"',
            'pedidos': consultarQuery(query), # Ejecutar una solicitud SQL, guardar el resultado en una variable.
            'total': consultarDato(f'SELECT IFNULL(COUNT(*), 0) FROM Pedidos WHERE id like "%{buscar}%" OR cliente like "%{buscar}%"')[0]
            }
        return render_template('recepcion/pedidos.html', datos=datos) # Devuelve la plantilla html, una variable con el pedido y otra con el dato buscado.
    else: # Sí la consulta no arroja resultados.
        flash(['No se han encontrado pedidos con el valor ', f'{buscar}'], 'Rojo') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('index')) # Se redirige al usuario a la ruta '/'.

@app.route('/pedidos/estado/<estado>') # Ruta que muestra todos los pedidos que se encuentran en un estado indicado.
def verPedidosEstado(estado):
    query = f'SELECT * FROM Pedidos WHERE estado = "{estado}"' # Solicitud a realizar.
    pedidos = consultarQuery(query) # Ejecutar una solicitud SQL, guardar el resultado en una variable.
    if pedidos: # Sí la consulta arroja resultados.
        datos = { # Datos a mostrar en la página.
            'pestaña': f'Pedidos "{estado}"',
            'titulo': f'Pedidos en estado "{estado}"',
            'pedidos': pedidos,
            "total": len(pedidos)
            }
        return render_template('recepcion/pedidos.html', datos=datos) # Devuelve la plantilla html y una variable con los pedidos.
    else: # Sí la consulta no arroja resultados.
        flash(['No se han encontrado pedidos con el estado ', f'{estado}'], 'Rojo') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('index')) # Se redirige al usuario a la ruta '/'.

@app.route('/ordenes/prioridad/<prioridad>')
def verOrdenesPrioridad(prioridad):
    query = f'SELECT id, id_Pedidos, producto, cantidad, precio, estado, prioridad, patron FROM Ordenes WHERE prioridad = "{prioridad}"' # Solicitud a realizar.
    ordenes = consultarQuery(query) # Ejecutar una solicitud SQL, guardar el resultado en una variable.
    if ordenes: # Sí la consulta arroja resultados.
        datos = { # Datos a mostrar en la página.
            'pestaña': f'Prioridad "{prioridad}"',
            'titulo': f'Ordenes con Prioridad "{prioridad}"',
            'ordenes': ordenes,
            "total": len(ordenes)
            }
        return render_template('recepcion/ordenes.html', datos=datos) # Devuelve la plantilla html y una variable con los pedidos.
    else: # Sí la consulta no arroja resultados.
        flash(['No se han encontrado ordenes con la prioridad ', f'{prioridad}'], 'Rojo') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('index')) # Se redirige al usuario a la ruta '/'.

@app.route('/ordenes/estado/<estado>')
def verOrdenesEstado(estado):
    query = f'SELECT id, id_Pedidos, producto, cantidad, precio, estado, prioridad, patron FROM Ordenes WHERE estado = "{estado}"' # Solicitud a realizar.
    ordenes = consultarQuery(query) # Ejecutar una solicitud SQL, guardar el resultado en una variable.
    if ordenes: # Sí la consulta arroja resultados.
        datos = { # Datos a mostrar en la página.
            'pestaña': f'Ordenes "{estado}"',
            'titulo': f'Ordenes en estado "{estado}"',
            'ordenes': ordenes,
            "total": len(ordenes)
            }
        return render_template('recepcion/ordenes.html', datos=datos) # Devuelve la plantilla html y una variable con los pedidos.
    else: # Sí la consulta no arroja resultados.
        flash(['No se han encontrado ordenes con el estado ', f'{estado}'], 'Rojo') # Se envía un mensaje, la categoría del mensaje y un dato a la próxima página en mostrarse.
        return redirect(url_for('index')) # Se redirige al usuario a la ruta '/'.

@app.route('/productos')
def productos():
    query = 'SELECT * FROM Productos'
    productos = consultarQuery(query)
    if productos:
        datos = {
            'pestaña': 'Productos',
            'titulo': 'Productos',
            'productos': productos
        }
        return render_template('recepcion/productos.html', datos=datos)
    else:
        flash(['No se han encontrado productos registrados'], 'Rojo')
        return redirect(url_for('recepcion'))

@app.route('/trabajo')
def trabajo():
    datos = {
        'pestaña': 'Área de Trabajo',
        'titulo': 'Área de Trabajo',
        'pendiente': consultarQuery('SELECT id, id_Pedidos, producto, cantidad, precio, estado, prioridad, patron, CASE prioridad WHEN "Alta" THEN "A" WHEN "Media" THEN "B" WHEN "Baja" THEN "C" ELSE "D" END categoria FROM Ordenes WHERE estado="Pendiente" ORDER BY categoria'),
        "total_pendiente": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE estado="Pendiente"')[0],
        'en_produccion': consultarQuery('SELECT id, id_Pedidos, producto, cantidad, precio, estado, prioridad, patron, CASE prioridad WHEN "Alta" THEN "A" WHEN "Media" THEN "B" WHEN "Baja" THEN "C" ELSE "D" END categoria FROM Ordenes WHERE estado="En Producción" ORDER BY categoria'),
        "total_en_produccion": consultarDato('SELECT IFNULL(COUNT(*), 0) FROM Ordenes WHERE estado="En Producción"')[0],
    }
    return render_template('produccion/trabajo.html', datos=datos)

@app.route('/login')
def login():
    if request.method == 'GET': # Cuando se solicita la plantilla html para iniciar sesión.
        return render_template('usuario/login.html')
    elif request.method == 'POST': # Cuando se está devolviendo la plantilla con usuario y contraseña.
        return redirect(url_for('index')) # Se redirige al usuario a la ruta '/'.

@app.errorhandler(404)
def page_not_found(e):
    datos = {
            'pestaña': 'Error',
            'titulo': 'Ha Ocurrido Un Error'
        }
    return render_template('errores/404.html', datos=datos), 404
    # flash(['La página que buscas no existe'], 'Rojo')
    # return redirect(url_for('index'))

app.run(debug=True, host='0.0.0.0', port=8000) # Ejecutando programa en modo prueba.
