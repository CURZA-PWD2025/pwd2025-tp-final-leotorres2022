
from .compras_model import ComprasModel
from ..categorias.categorias_model import CategoriasModel as Categorias
from ..talles.talles_model import TallesModel as Talle
from ..socios.socios_model import SociosModel as Socios
class ComprasController:
    
    @staticmethod
    def get_all():
        compras = ComprasModel.get_all()
        return compras
    @staticmethod
    def get_one(id):
        compra = ComprasModel(id=id).get_by_id()
        return compra
    @staticmethod
    def crear(data: dict):
        categoria_data = Categorias(id=data['categoria_id']).get_by_id()
        talle_data = Talle(id=data['talle_id']).get_by_id()
        categoria = Categorias.deserializar(categoria_data) if categoria_data else None
        talle = Talle.deserializar(talle_data) if talle_data else None
        socio_data =Socios (id=data['socio_id']).get_by_id()
        socio = Socios.deserializar(socio_data) if socio_data else None
        compra = ComprasModel(
            descripcion=data['descripcion'],
            precio=data['precio'],
            cantidad=data['cantidad'],
            talle=talle,
            categoria=categoria,
            socio=socio
                               )
        result = compra.create()
        return result
    @staticmethod
    def update(id, data: dict):
        categoria_data = Categorias(id=data['categoria_id']).get_by_id()
        talle_data = Talle(id=data['talle_id']).get_by_id()
        socio_data = Socios(id=data['socio_id']).get_by_id()
        categoria = Categorias.deserializar(categoria_data) if categoria_data else None
        talle = Talle.deserializar(talle_data) if talle_data else None
        socio = Socios.deserializar(socio_data) if socio_data else None
       
        compra = ComprasModel(
            id=id,
            descripcion=data['descripcion'],
            precio=data['precio'],
            cantidad=data['cantidad'],
            talle=talle,
            categoria=categoria,
            socio=socio
        )
        result = compra.update()
        return result
    @staticmethod
    def eliminar(id):
     compra = ComprasModel(id=id)
     return compra.delete()
    
    