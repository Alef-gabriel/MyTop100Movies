from flask import Flask
from .blueprint.bp import bp
from .models.mod import configure as config_db
from flask_migrate import Migrate
from .ma import configure as config_ma

#Function for create app. best sintax
def create_app():
    app = Flask(__name__)
    #app config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movies.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    #db configurations and migrations
    config_db(app)
    Migrate(app,app.db)
    config_ma(app)

    app.register_blueprint(bp)
    
    return app