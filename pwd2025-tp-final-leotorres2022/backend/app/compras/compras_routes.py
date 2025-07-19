from flask import jsonify, request, Blueprint
from .compras_controller import ComprasController

compra_bp=Blueprint("compra", __name__)

@compra_bp.route("/compras/", methods=['GET', 'OPTIONS'])
def get_all():
    try:
        compras = ComprasController.get_all()
        if compras:
            return jsonify(compras), 200
        else:
            return jsonify({'mensaje': 'no se encontraron compras'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
     
@compra_bp.route("/compras/<int:id>")
def get_one(id):
    try:
        compra = ComprasController.get_one(id)
        if compra:
            return jsonify(compra), 200
        else:
            return jsonify({'mensaje': 'no se encontro la compra'}),404
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500  
@compra_bp.route("/compras/", methods=['POST', 'OPTIONS'])
def crear():
    try:
        data = request.get_json()
        if data is None:
            return  jsonify({'mensaje': "no se recibieron dato"})
        result = ComprasController.crear(data)
        if result:
            return jsonify({'mensaje':'compra creado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'error al crear la compra'}),500
        
    except Exception as exc:
         return jsonify({'mensaje': f" error : {str(exc)}"}), 500
@compra_bp.route("/compras/<int:id>", methods=["PUT", "OPTIONS"])
def modificar_compra(id):
    if request.method == "OPTIONS":
        return jsonify({'mensaje': 'ok'}), 200
    data = request.get_json()
    result = ComprasController.update(id, data)
    if result:
        return {"mensaje": "compra actualizada correctamente"}, 200
    else:
        return {"mensaje": "Error al actualizar la compra"}, 500     
@compra_bp.route("/compras/<int:id>", methods=["DELETE"])
def eliminar_compra(id):
    result = ComprasController.eliminar(id)
    if result:
        return {"mensaje": "Compra eliminada correctamente"}, 200
    else:
        return {"mensaje": "Error al eliminar la compra"}, 500
         