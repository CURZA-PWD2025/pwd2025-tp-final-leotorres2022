from ..database.conect_db import ConectDB
from ..socios.socios_model import SociosModel as Socio
from ..categorias.categorias_model import CategoriasModel as Categorias
from ..talles.talles_model import TallesModel as Talle

import pymysql

class ComprasModel():

    def __init__(self, id:int=0, descripcion:str="",talle:Talle = None ,
                 precio:float=0.0,categorias:Categorias=None ,cantidad:int=0,socio:list[Socio]=None):
        self.id = id
        self.descripcion = descripcion
        self.talle = talle
        self.precio = precio
        self.socio = socio
        self.cantidad = cantidad
        self.categorias = categorias
        
    def serializar(self) -> dict:
        return {
               'id': self.id,
                'descripcion': self.descripcion,
                'precio': self.precio,
                'cantidad': self.cantidad,
                'talle ': self.talle.serializar() if self.talle else None,
                'categorias': self.categorias.serializar() if self.categorias else None, 
                'socio': [socio.serializar() for socio in self.socio]
         
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
                # Obtener talle y socio
                talle =Talle(id=row['talle_id']).get_by_id()
                categorias = Categorias(id=row['categoria_id']).get_by_id()
                talle = Talle.deserializar(talle) if talle else None
                categorias=Categorias.deserializar(categorias) if categorias else None

                # Obtener socios 
                cursor.execute("SELECT socio_id FROM socios_compras WHERE compra_id = %s", (row['id'],))
                socio_ids = [cat['socio_id'] for cat in cursor.fetchall()]
                socios = []
                for soc_id in socio_ids:
                    cursor.execute("SELECT * FROM socios WHERE id = %s", (soc_id,))
                    soc_row = cursor.fetchone()
                    if soc_row:
                        socios.append(Socio.deserializar(soc_row))
                 
                compra = ComprasModel(
                    id=row['id'],
                    descripcion=row['descripcion'],
                    precio=row['precio'],
                    cantidad=row['cantidad'],
                    talle=talle,
                    categorias=categorias,
                    socio=socios
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
            categorias = Categorias(id=row['categoria_id']).get_by_id()
            talle = Talle.deserializar(talle) if talle else None
            categorias  = Categorias.deserializar(categorias) if categorias else None
            # Obtener socios 
            cursor.execute("SELECT socio_id FROM socios_compras WHERE compra_id = %s", (row['id'],))
            socio_ids = [cat['socio_id'] for cat in cursor.fetchall()]
            socios = []
            for soc_id in socio_ids:
                    cursor.execute("SELECT * FROM socios WHERE id = %s", (soc_id,))
                    soc_row = cursor.fetchone()
                    if soc_row:
                        socios.append(Socio.deserializar(soc_row))

            compra = ComprasModel(
                id=row['id'],
                descripcion=row['descripcion'],
                precio=row['precio'],
                cantidad=row['cantidad'],
                talle=talle,
                socio=socios,
                categorias=categorias
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
                "INSERT INTO compras (descripcion,precio,cantidad,talle_id,categoria_id) VALUES (%s, %s, %s, %s, %s)",
                (self.descripcion, self.precio, self.cantidad, self.talle.id, self.categorias.id)
            )
            result = cursor.rowcount
            compra_id = cursor.lastrowid  
            print("RESULTADO DE LA INSERCION:", result, "ID:", compra_id)
            if self.socio:
                for socio in self.socios:
                    soc_id = getattr(socio, 'id', socio) 
                    cursor.execute(
                        "INSERT INTO socios_compras (compra_id, socio_id) VALUES (%s, %s)",
                        (compra_id, soc_id)
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
            # Actualizar los datos principales del artículo
            cursor.execute(
                "UPDATE compras SET descripcion=%s, precio=%s, cantidad=%s, talle_id=%s, categoria_id=%s WHERE id=%s",
                (self.descripcion, self.precio, self.cantidad, self.categorias.id, self.talle.id, self.id)
            )
            # Eliminar las categorías actuales
            cursor.execute(
                "DELETE FROM socios_compras WHERE compras_id = %s",
                (self.id,)
            )
            # Insertar los nuevos socios asociados
            if self.socio:
                for socio in self.socios:
                    soc_id = getattr(socio  , 'id', socio)
                    cursor.execute(
                        "INSERT INTO socios_compras (compra_id, socio_id) VALUES (%s, %s)",
                        (self.id, soc_id)
                    )
            cnx.commit()
            return True
     except Exception as exc:
        cnx.rollback()
        print(f"Error al actualizar Compra: {exc}")
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
            # Eliminar el artículo
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
