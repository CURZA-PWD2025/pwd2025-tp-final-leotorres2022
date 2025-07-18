from flask import Flask
from flask_cors import CORS
from .categorias.categorias_routes import categoria_bp
from .socios.socios_routes import socio_bp
from .talles.talles_routes import talle_bp
# from .compras.compras_routes import compra_bp


def create_app():
    app= Flask(__name__)
    CORS(app, supports_credentials=True)  
    app.register_blueprint(categoria_bp)
 #   app.register_blueprint(compra_bp)
    app.register_blueprint(socio_bp)
    app.register_blueprint(talle_bp)
    @app.route("/")
    def home():
        return    "<h1>Hola bienvenidos a la pagina</h1>"
    return app
      