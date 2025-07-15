import pymysql
import pymysql.err as pymysql_err

import os
from dotenv import load_dotenv

load_dotenv()

class ConectDB:
    @staticmethod
    def connect():
        try:
            conn = pymysql.connect(
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                host=os.getenv("DB_HOST", "localhost"),
                port=int(os.getenv("DB_PORT", 3306)),
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=False
            )
            return conn
        except pymysql_err.OperationalError as ex:
            print(f"Error connecting to the database: {ex}")
