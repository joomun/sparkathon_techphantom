import os
from flask import Flask
from .routes import main


def create_app():
    app = Flask(__name__)
    
    # Registering the blueprint
    
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.py'))
    app.config.from_pyfile(config_path)
    from .routes import main
    from .routes.upload import upload_blueprint
    app.register_blueprint(main)
    app.register_blueprint(upload_blueprint)
    
    return app
