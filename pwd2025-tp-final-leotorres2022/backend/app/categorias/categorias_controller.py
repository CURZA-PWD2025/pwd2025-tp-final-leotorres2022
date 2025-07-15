from .categorias_model import CategoriasModel

class CategoriasController:
    @staticmethod
    def get_all():
        categorias = CategoriasModel.get_all()
        return categorias

    @staticmethod    
    def get_one(id):
        categoria = CategoriasModel(id=id).get_by_id()
        return categoria

    @staticmethod
    def crear(data: dict):
        print(data)
        categoria = CategoriasModel(nombre=data['nombre'])
        result = categoria.create()
        return result

    @staticmethod
    def modificar(data:dict):
        categoria = CategoriasModel.deserializar(data)
        result = categoria.update()
        return result

    @staticmethod    
    def eliminar(id):
        result = CategoriasModel.delete(id)
        return result
        
          
          
          
    
    