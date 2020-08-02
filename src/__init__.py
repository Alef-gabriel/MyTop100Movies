from flask import Flask
from src.models.modelsSqlalchemy import SqlalchemyConfigureDatabase
from src.blueprint.blueprintsRoutes import blueprintRote
from src.serializing.marshmallowMovie import marshmallowConfigure
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True

    SqlalchemyConfigureDatabase(app)
    marshmallowConfigure(app)
    Migrate(app,app.db)

    app.register_blueprint(blueprintRote)   
    return app