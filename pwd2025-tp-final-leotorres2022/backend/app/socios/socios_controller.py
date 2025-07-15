from .socios_model import SociosModel
class SociosController:
    @staticmethod
    def get_all():
        socios = SociosModel.get_all()
        return socios
    @staticmethod    
    def get_one(id):
        socio = SociosModel(id=id).get_by_id()
        return socio

    @staticmethod
    def crear(data: dict):
        print(data)
        socio = SociosModel(nombre=data['nombre'],direccion=data['direccion'],telefono=data['telefono'],email=data['email'])
        result = socio.create()
        return result

    @staticmethod
    def modificar(data:dict):
        socio = SociosModel.deserializar(data)
        result = socio.update()
        return result

    @staticmethod    
    def eliminar(id):
        result = SociosModel.delete(id)
        return result