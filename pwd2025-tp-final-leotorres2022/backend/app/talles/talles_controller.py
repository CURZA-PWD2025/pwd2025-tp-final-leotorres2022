from .talles_model import TallesModel
class TallesController:
    @staticmethod
    def get_all():
        marcas = TallesModel.get_all()
        return marcas

    @staticmethod    
    def get_one(id):
        marca = TallesModel(id=id).get_by_id()
        return marca

    @staticmethod
    def crear(data: dict):
        print(data)
        marca = TallesModel(nombre=data['nombre'])
        result = marca.create()
        return result

    @staticmethod
    def modificar(data:dict):
        marca = TallesModel.deserializar(data)
        result = marca.update()
        return result

    @staticmethod    
    def eliminar(id):
        result = TallesModel.delete(id)
        return result