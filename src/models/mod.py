from flask_sqlalchemy import SQLAlchemy

#db definiton
db = SQLAlchemy()

#db configure for function app
def configure(app):
    db.init_app(app)
    app.db = db

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    release_date = db.Column(db.String(80))
    popularity = db.Column(db.String(120))

    def __repr__(self):
        return '<Movies %r>' % self.title