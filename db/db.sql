--          Queries para crear tablas
CREATE TABLE IF NOT EXISTS "Usuarios" ( -- Tabla que almacena los usuarios 
    usuario VARCHAR(255) NOT NULL PRIMARY KEY,
    contraseña VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "Pedidos" ( -- Tabla que almacena los pedidos
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    cliente VARCHAR(255) NOT NULL,
    fecha VARCHAR(255) NOT NULL,
    total INT NOT NULL,
    ordenes TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "Productos" ( -- Tabla que almacena productos y precios.
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre_producto VARCHAR(255) NOT NULL,
    precio INT(255)
);


--          Queries registrar datos en las tablas
INSERT INTO "Usuarios" ("usuario", "contraseña") -- Registrar usuarios para la app.
VALUES
    ('admin', "1234"),
    ('recepcion', "1234"),
    ('produccion', "1234");

INSERT INTO "Pedidos" ("cliente", "fecha", "total", "ordenes") -- Registrar pedidos en base de datos.
VALUES
    ("Pablo Tapias", "28/01/2023 21:22:37" ,114000, '["Juego de Cuellos Acrílico",30,114000,"O.verde.2-L.blanco.2-L.verde.2-F.blanco"]'), --OLCF (Orillo, Linea, Caracter, Fondo)
    ("Maria Gomez", "28/01/2023 18:13:47", 560000, "['Juego de Cuello Hilo', '20', '80000', 'O.rojo.2-L.verde.4-F.rojo'], ['Juego Fajas Completo', '40', '480000', 'O.amarillo.2-F.amarillo']"); --OLCF (Orillo, Linea, Caracter, Fondo)

INSERT INTO "Productos" ("producto", "precio") -- Registrar los productos disponibles en la tabla productos.
VALUES
    ("Juego de Cuellos Acrílico", 3800),
    ("Solo Cuello Acrílico", 2000),
    ("Solo Tira Acrílico", 2000),
    ("Juego de Cuello Letras", 5000),
    ("Cuello y Puño Letras", 6000),
    ("Solo Cuello Letras", 3500),
    ("Juego de Cuello Hilo", 4000),
    ("Solo Cuello Hilo", 2200),
    ("Juego Fajas Completo", 12000),
    ("Solo Faja Dobles", 6000),
    ("Cuello Redondo Doble", 4000);


--          Queries para borrar tablas
DROP TABLE IF EXISTS "Usuarios"; -- Borrar la tabla Usuarios
DROP TABLE IF EXISTS "Pedidos"; -- Borrar la tabla Pedidos
DROP TABLE IF EXISTS "Productos"; -- Borrar la tabla Productos


--          Queries para borrar contenido de las tablas
DELETE FROM "Usuarios"; -- Borrar contenido de la tabla Usuarios
DELETE FROM "Pedidos"; -- Borrar contenido de la tabla Pedidos
DELETE FROM "Productos"; -- Borrar contenido de la tabla Productos


--          Queries para ver tablas
SELECT * FROM "Usuarios"; -- Ver contenido de la tabla Usuarios
SELECT * FROM "Pedidos"; -- Ver contenido de la tabla Pedido
SELECT * FROM "Productos"; -- Productos contenido de la tabla Usuarios


--          Queries para modificar datos en la tabla
UPDATE "Pedidos" SET cliente = 'Maria Gomez' WHERE id = 11;