import pymysql
import pymysql.err as pymysql_err

import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")

DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': int(os.getenv("DB_PORT")),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
    'autocommit': False,
}
TABLES = {}
SEEDS = {}
TABLES['CATEGORIAS'] = (
    "CREATE TABLE `CATEGORIAS` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") "
)
TABLES['TALLES'] = (
    "CREATE TABLE `TALLES` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") "
)
TABLES['SOCIOS'] = (
    "CREATE TABLE `SOCIOS` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `telefono` varchar(50) NOT NULL,"
    "  `direccion` varchar(50) NOT NULL,"
    "  `email` varchar(50) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") "
)
TABLES['COMPRAS'] = (
    "CREATE TABLE `COMPRAS` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `descripcion` varchar(150) NOT NULL,"
    " `precio` decimal(10,2) NOT NULL,"
    "  `cantidad` int(11) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  `talle_id` int(11) NOT NULL,"
    "  `categoria_id` int(11) NOT NULL,"
    " foreign key (`talle_id`) references TALLES(id),"
    " foreign key (`categoria_id`) references CATEGORIAS(id)"
    ") "
)
TABLES["SOCIOS_COMPRAS"] = (
    "CREATE TABLE `SOCIOS_COMPRAS` ("
    "  `compra_id` int(11) NOT NULL,"
    "  `socio_id` int(11) NOT NULL,"
    " foreign key (`compra_id`) references COMPRAS(id),"
    " foreign key (`socio_id`) references SOCIOS(id)"
    ") "
)

SEEDS['SOCIOS'] = (
    "INSERT INTO SOCIOS (nombre, telefono, direccion, email) "
    "VALUES (%s, %s, %s, %s)",
       [
        ('Juan Pérez', '1144556677', 'Av. Córdoba 1234, CABA', 'juan.perez@gmail.com'),
        ('María González', '1167891234', 'Calle Falsa 456, Rosario', 'maria.gonzalez@hotmail.com'),
        ('Carlos López', '1133445566', 'Av. San Martín 789, Mendoza', 'carlos.lopez@yahoo.com'),
        ('Ana Torres', '1122334455', 'Mitre 321, La Plata', 'ana.torres@gmail.com'),
        ('Lucía Fernández', '1198765432', 'Belgrano 987, Córdoba', 'lucia.fernandez@gmail.com'),
        ('Martín Ramírez', '1177889900', 'Av. Rivadavia 4321, CABA', 'martin.ramirez@gmail.com'),
        ('Sofía Castro', '1100112233', 'Urquiza 1111, Mar del Plata', 'sofia.castro@gmail.com'),
        ('Diego Sosa', '1188997766', 'Alsina 654, Bahía Blanca', 'diego.sosa@gmail.com'),
        ('Valentina Díaz', '1155667788', 'Av. Colon 2020, Salta', 'valentina.diaz@gmail.com'),
        ('Federico Ruiz', '1133221100', 'San Juan 3030, Tucumán', 'federico.ruiz@gmail.com')
    ]
)
 
SEEDS['TALLES'] = (
    "INSERT INTO TALLES (nombre) "
    "VALUES (%s)",
    [
        ('S',),
        ('L',),
        ('M',),
        ('XL',),
        ('XXL',),
       
    ]
)
SEEDS['CATEGORIAS'] = (
    "INSERT INTO CATEGORIAS (nombre) "
    "VALUES (%s)",
    [
        ('Short de Futbol',),
        ('Medias Largas',),
        ('Camisetas',),
        ('Gorra',),
        ('Pantalon Largo',),
        ('Buso',),
        ('Bandera',)]
)
SEEDS['COMPRAS'] = (
    "INSERT INTO compras (descripcion, precio, cantidad, talle_id, categoria_id) VALUES (%s, %s, %s, %s, %s)",
    [
        ("Camiseta titular 2024", 15000.0, 20, 1, 1),  # (descripcion, precio, cantidad, talle_id, categoria_id)
        ("Short oficial", 9000.0, 15, 2, 2),
        ("Medias deportivas", 4000.0, 30, 3, 3),
        ("Camiseta suplente 2024", 15500.0, 10, 1, 1),
        ("Buzo entrenamiento", 18000.0, 8, 4, 4)
    ]
)

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
    except pymysql_err.ProgrammingError as err:
        if err.args[0] == 1044:  # ER_ACCESS_DENIED_ERROR
            print("Something is wrong with your user name or password")
        elif err.args[0] == 1007:  # ER_DB_CREATE_EXISTS_ERROR
            print("Database already exists")
        else:
            print(err)
    else:
        print(f"Database {DB_NAME} created successfully.")

def create_tables(tables, cursor):
    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Creating table {table_name}: ", end="")
            cursor.execute(table_description)
        except pymysql_err.ProgrammingError as err:
            if err.args[0] == 1050:  # ER_TABLE_EXISTS_ERROR
                print("already exists.")
            else:
                print(err)
        else:
            print("OK")

def seeds_tables(seed, cursor):
    for table_name in seed:
        seed_description = seed[table_name]
        try:
            print(f"Seeding table {table_name}: ", end="")
            cursor.executemany(seed_description[0], seed_description[1])
        except Exception as err:
            print(err)
        else:
            print("OK")

# Crear la base de datos
cxn = pymysql.connect(**{k: v for k, v in DB_CONFIG.items() if k != 'database'})
with cxn.cursor() as cursor:
    create_database(cursor)
cxn.close()

# Crear tablas y seedear datos
CONF_DB = DB_CONFIG.copy()
CONF_DB['database'] = DB_NAME
cxn = pymysql.connect(**CONF_DB)
with cxn.cursor() as cursor:
    create_tables(TABLES, cursor)
    seeds_tables(SEEDS, cursor)
    cxn.commit()
cxn.close()