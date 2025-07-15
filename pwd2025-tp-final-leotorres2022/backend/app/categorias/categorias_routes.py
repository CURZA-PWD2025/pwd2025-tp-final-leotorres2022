from .categorias_controller import CategoriasController
from flask import Blueprint, jsonify, request

categoria_bp = Blueprint('categoria_bp', __name__)

@categoria_bp.route("/categorias")
def get_all():
    try:
        categorias = CategoriasController.get_all()
        if categorias:
            return jsonify(categorias), 200
        else:
            return jsonify({'mensaje': 'No hay categorías disponibles'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener categorías: {exc}"}), 500

@categoria_bp.route("/categorias/<int:id>")
def get_one(id):
    try:
        categoria = CategoriasController.get_one(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({'mensaje': 'No se encontró la categoría'}), 404
    except Exception as exc:
        return jsonify({'mensaje': f"Error al obtener categoría: {exc}"}), 500

@categoria_bp.route("/categorias/", methods=['POST'])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'mensaje': "No se recibieron datos"})
        result = CategoriasController.crear(data)
        if result:
            return jsonify({'mensaje':'Categoría creada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear la categoría'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500

@categoria_bp.route("/categorias/<int:id>", methods=["PUT"])
def modificar(id):
    try:
        data = request.get_json()
        data['id'] = id
        result = CategoriasController.modificar(data)
        if result:
            return jsonify({'mensaje':'Categoría modificada correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al modificar la categoría'}), 500
    except Exception as exc:
        return jsonify({'mensaje': f"Error: {str(exc)}"}), 500    

@categoria_bp.route("/categorias/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        result = CategoriasController.eliminar(id)
        if result:
            return jsonify({'mensaje':"Categoría eliminada con éxito"})
        else:
            return jsonify({'mensaje':"Error al eliminar la categoría"})
    except Exception as exc:
        return jsonify({'mensaje':f"Error: {exc}"})