from flask import Flask
from .blueprint.bp import bp
from .models.mod import configure as config_db
from flask_migrate import Migrate

#Function for create app. best sintax
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movies.db'
    #db configurations and migrations
    config_db(app)
    Migrate(app,app.db)

    app.register_blueprint(bp)
    return app