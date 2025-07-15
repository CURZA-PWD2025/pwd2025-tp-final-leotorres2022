import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()
database_name = os.getenv("DB_NAME")

database_config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': os.getenv("DB_PORT"),
    'raise_on_warnings': True,
    "database": database_name
}

DROPPED_TB = {}

DROPPED_TB["articulos_categorias"] = "DROP TABLE IF EXISTS articulos_categorias;"
DROPPED_TB["articulos"] = "DROP TABLE IF EXISTS articulos;"
DROPPED_TB["proveedores"] = "DROP TABLE IF EXISTS proveedores;"
DROPPED_TB["marcas"] = "DROP TABLE IF EXISTS marcas;"
DROPPED_TB["categorias"] = "DROP TABLE IF EXISTS categorias;"


def rollback_db():
    cxn = mysql.connector.connect(**database_config)
    cursor = cxn.cursor()
    for table in DROPPED_TB:
        print(f"Dropped table: {table}", end=" ")
        try:
            cursor.execute(DROPPED_TB[table])
            print('ok')
            cxn.commit()
        except Error as e:
            print(f"{e}")
    
    cursor.close()
    cxn.close()

rollback_db()
