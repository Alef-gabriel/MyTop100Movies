from flask import Flask
from src.blueprint.blueprintsRoutes import blueprintRote
from src.models.modelsSqlalchemy import SqlalchemyConfigureDatabase
from flask_migrate import Migrate
from src.serializing.marshmallowSqlalchemy import MarshmallowConfigure

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True

    sqlalchemyConfigureDatabase(app)
    Migrate(app,app.database)
    marshmallowConfigure(app)

    app.register_blueprint(blueprintRote)   
    return app