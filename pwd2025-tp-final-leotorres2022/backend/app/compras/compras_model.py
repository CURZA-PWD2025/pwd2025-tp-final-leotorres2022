from ..database.conect_db import ConectDB
from ..socios.socios_model import SociosModel as Socio
from ..categorias.categorias_model import CategoriasModel as Categorias
from ..talles.talles_model import TallesModel as Talle

import pymysql

class ComprasModel():

    def __init__(self, id:int=0, descripcion:str="",talle:Talle = None ,
                 precio:float=0.0,categoria:Categorias=None ,cantidad:int=0,socio:Socio=None):
        self.id = id
        self.descripcion = descripcion
        self.talle = talle
        self.precio = precio
        self.socio = socio
        self.cantidad = cantidad
        self.categoria = categoria
        
    def serializar(self) -> dict:
        return {
               'id': self.id,
                'descripcion': self.descripcion,
                'precio': self.precio,
                'cantidad': self.cantidad,
                'talle': self.talle.serializar() if self.talle else None,
                'categoria': self.categoria.serializar() if self.categoria else None, 
                'socio':self.socio.serializar() if self.socio else None
         
        }  
    
    @staticmethod
    def deserializar(data:dict):
        return ComprasModel(
          **data  
        )
    @staticmethod    
    def get_all() -> list[dict]:
     cnx = ConectDB.connect()
     try:
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:  
            cursor.execute("SELECT * FROM compras")
            rows = cursor.fetchall()
            compras = []
            for row in rows:
                talle =Talle(id=row['talle_id']).get_by_id()
                categoria = Categorias(id=row['categoria_id']).get_by_id()
                socio = Socio(id=row['socio_id']).get_by_id()
                socio = Socio.deserializar(socio) if socio else None
                talle = Talle.deserializar(talle) if talle else None
                categoria=Categorias.deserializar(categoria) if categoria else None
                
                            
                compra = ComprasModel(
                    id=row['id'],
                    descripcion=row['descripcion'],
                    precio=row['precio'],
                    cantidad=row['cantidad'],
                    talle=talle,
                    categoria=categoria,
                    socio=socio
                )
                compras.append(compra.serializar())
            return compras
     except Exception as exc:
        print(f"Error al listar compras: {exc}")
        return {'mensaje': f" error al listar compras {exc}"}
     finally:
        cnx.close()
        
    def get_by_id(self)->dict:
     cnx = ConectDB.connect()
     try:
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM compras WHERE id = %s", (self.id,))
            row = cursor.fetchone()
            print("Row encontrado:", row)
            if not row:
                return False

            talle = Talle(id=row['talle_id']).get_by_id()
            categoria= Categorias(id=row['categoria_id']).get_by_id()
            talle = Talle.deserializar(talle) if talle else None
            categoria  = Categorias.deserializar(categoria) if categoria else None
            socio = Socio(id=row['socio_id']).get_by_id()
            socio = Socio.deserializar(socio) if socio else None

            compra = ComprasModel(
                id=row['id'],
                descripcion=row['descripcion'],
                precio=row['precio'],
                cantidad=row['cantidad'],
                talle=talle,
                socio=socio,
                categoria=categoria
            )
                       
            return compra.serializar()
     except Exception as exc:
           print("Error en get_by_id:", exc)
           return {'mensaje': f" error buscar una compra {exc}"}
     finally:
        cnx.close() 
    def create(self):
     cnx = ConectDB.connect()
     try:
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(
                "INSERT INTO compras (descripcion,precio,cantidad,talle_id,categoria_id,socio_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.descripcion, self.precio, self.cantidad, self.talle.id, self.categoria.id,self.socio.id)
            )
            result = cursor.rowcount
            compra_id = cursor.lastrowid  
            print("RESULTADO DE LA INSERCION:", result, "ID:", compra_id)
            if self.socio:
             cursor.execute(
        "INSERT INTO socios_compras (compra_id, socio_id) VALUES (%s, %s)",
        (compra_id, self.socio.id)
    )
            cnx.commit()
            if result > 0:
                return True
            return False
     except Exception as exc:
        cnx.rollback()
        print(f" error crear la compra {exc}")
        return False
     finally:
        cnx.close()
    def update(self):
     cnx = ConectDB.connect()
     try:
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(
                "UPDATE compras SET descripcion=%s, precio=%s, cantidad=%s, talle_id=%s, categoria_id=%s,socio_id=%s  WHERE id=%s",
                 
                (self.descripcion, self.precio, self.cantidad, self.talle.id, self.categoria.id, self.socio.id, self.id)
            )
            # Eliminar las socios actuales
            cursor.execute(
                "DELETE FROM socios_compras WHERE compra_id = %s",
                (self.id,)
            )
            
            if self.socio:
             cursor.execute(
        "INSERT INTO socios_compras (compra_id, socio_id) VALUES (%s, %s)",
        (self.id, self.socio.id)
    )

            cnx.commit()
            return True
     except Exception as exc:
        cnx.rollback()
        import traceback
        traceback.print_exc()  # Esto muestra la traza completa del error
        print(f"Error al actualizar Compra: {exc.__class__.__name__}: {exc}")
        return False
       
     finally:
        cnx.close()    
    
    def delete(self):
     cnx = ConectDB.connect()
     try:
        with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
            # Eliminar relaciones en la tabla intermedia primero
            cursor.execute(
                "DELETE FROM socios_compras WHERE compra_id = %s",
                (self.id,)
            )
            # Eliminar la compra
            cursor.execute(
                "DELETE FROM compras WHERE id = %s",
                (self.id,)
            )
            cnx.commit()
            return True
     except Exception as exc:
        cnx.rollback()
        print(f"Error al eliminar Compra : {exc}")
        return False
     finally:
        cnx.close()    
