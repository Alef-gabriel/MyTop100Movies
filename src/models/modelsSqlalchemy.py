from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

def SqlalchemyConfigureDatabase(app):
    database.init_app(app)
    app.database = database

class Movies(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(80))
    release_date = database.Column(database.String(80))
    popularity = database.Column(database.String(120))

    def __repr__(self):
        return '<Movies %r>' % self.title