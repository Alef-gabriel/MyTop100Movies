from flask import Flask
from .blueprint.bp import bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(bp)
    return app