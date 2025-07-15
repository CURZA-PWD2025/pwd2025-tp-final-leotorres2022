from .socios_controller import SociosController
from flask import Blueprint, jsonify, request

socio_bp = Blueprint('socio_bp', __name__)

@socio_bp.route("/socios")
def get_all():
    try:
        socios = SociosController.get_all()
        if socios:
            return jsonify(socios), 200
        else:
            return jsonify({'mensaje': 'No hay socios disponibles'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener socios: {exc}"}), 500

@socio_bp.route("/socios/<int:id>")
def get_one(id):
    try:
        socio = SociosController.get_one(id)
        if socio:
            return jsonify(socio), 200
        else:
            return jsonify({'mensaje': 'No se encontró el socio'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener socio: {exc}"}), 500

@socio_bp.route("/socios/", methods=['POST'])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'mensaje': "No se recibieron datos"})
        result = SociosController.crear(data)
        if result:
            return jsonify({'mensaje':'proveedor creada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear la proveedor'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@socio_bp.route("/socios/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        result = SociosController.modificar(data)
        if result:
            return jsonify({'mensaje':'socio modificado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al modificar  socio'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500    

@socio_bp.route("/socios/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        result = SociosController.eliminar(id)
        if result:
            return jsonify({'mensaje':"socio eliminado con éxito"})
        else:
            return jsonify({'mensaje':"Error al eliminar socio"})
    except Exception as exc:
        return jsonify({'mensaje':f"Error: {exc}"})