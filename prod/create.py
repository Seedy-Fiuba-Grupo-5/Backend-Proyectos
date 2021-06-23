import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Instanciar la base de datos
db = SQLAlchemy()
migrate = Migrate()


def create_app(script_info=None):
    # App 'Factory'

    # Instanciar la aplicacion
    app = Flask(__name__)

    # Configuracion
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    import_blueprints(app)
    CORS(app)

    # Contexto de la 'shell' para flask cli
    # Registra las instancias app y db en la 'shell'.
    # Permite trabajar con el contexto de la aplicacion
    # y la base de datos sin tener que importarlos
    # directamente en la 'shell'
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app


def import_blueprints(app):
    from .api import api_base_bp, api_v1_bp
    app.register_blueprint(api_base_bp)
    app.register_blueprint(api_v1_bp)
