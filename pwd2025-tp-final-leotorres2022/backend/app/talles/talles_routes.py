from .talles_controller import TallesController
from flask import Blueprint, jsonify, request

talle_bp = Blueprint('talle_bp', __name__)

@talle_bp.route("/talles", methods=['GET'])

def get_all():
    try:
        marcas = TallesController.get_all()
        if marcas:
            return jsonify(marcas), 200
        else:
            return jsonify({'mensaje': 'No hay talle disponibles'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener talle: {exc}"}), 500

@talle_bp.route("/talles/<int:id>")
def get_one(id):
    try:
        categoria = TallesController.get_one(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({'mensaje': 'No se encontró el talle'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener talle: {exc}"}), 500

@talle_bp.route("/talles/", methods=['POST'])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'mensaje': "No se recibieron datos"})
        result = TallesController.crear(data)
        if result:
            return jsonify({'mensaje':'Talle creada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear Talle'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@talle_bp.route("/talles/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        result = TallesController.modificar(data)
        if result:
            return jsonify({'mensaje':'Talle modificada correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al modificar talle'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500    

@talle_bp.route("/talles/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        result = TallesController.eliminar(id)
        if result:
            return jsonify({'mensaje':"talle eliminada con éxito"})
        else:
            return jsonify({'mensaje':"Error al eliminar la talle"})
    except Exception as exc:
        return jsonify({'mensaje':f"Error: {exc}"})