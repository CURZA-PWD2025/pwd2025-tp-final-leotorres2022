from ..database.conect_db import ConectDB
import pymysql

class CategoriasModel():

    def __init__(self, id:int=0, nombre:str=""):
        self.id = id
        self.nombre = nombre

    def serializar(self) -> dict:
        return {
            'id': self.id,
            'nombre': self.nombre   
        }
    
    @staticmethod
    def deserializar(data:dict):
        return CategoriasModel(
            id=data['id'], 
            nombre=data['nombre'],
        )
        
    @staticmethod
    def get_all():
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("SELECT * FROM categorias")
                rows = cursor.fetchall()
                categorias = []
                for row in rows:
                    categorias.append(row)
                return categorias
            except Exception as exc:
                return {'mensaje': f" error al listar categorias {exc}"}
    
    def get_by_id(self):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("SELECT * FROM categorias WHERE id = %s", (self.id,))
                row = cursor.fetchone()
                if row:
                    return row
                return False
            except Exception as exc:
                print(f"Error al obtener categoria por id {self.id}: {exc}")
              
    def create(self):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("INSERT INTO categorias (nombre) VALUES (%s)", 
                               (self.nombre,))
                result = cursor.rowcount
                print("NOMBRE A INSERTAR:", self.nombre)
                cnx.commit()
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                print(f" error crear la categoria {exc}")
            finally:
                cnx.close()
    def update(self):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("UPDATE categorias SET nombre = %s where id=%s ", 
                               (self.nombre, self.id))
                result = cursor.rowcount
                cnx.commit()
                
                if result > 0:
                    return True
                return False
                
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error actualizar una categoria {exc}"}
            finally:
                cnx.close()                
    @staticmethod
    def delete(id:int):
        cnx = ConectDB.connect()
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            try:
                cursor.execute("DELETE FROM categorias where id = %s ", 
                               (id,))
                result = cursor.rowcount
                cnx.commit()
                if result > 0:
                    return True
                return False
            except Exception as exc:
                cnx.rollback()
                return {'mensaje':f" error eliminar una categoria {exc}"}
            finally:
                cnx.close()