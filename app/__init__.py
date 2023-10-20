import os
from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.py'))
    app.config.from_pyfile(config_path)
    from .routes import main
    app.register_blueprint(main)
    
    return app
