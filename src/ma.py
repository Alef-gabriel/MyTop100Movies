from flask_marshmallow import Marshmallow
from .models.mod import Movies
#define flask-marshmallow
ma = Marshmallow()
#function for configure in app
def configure(app):
    ma.init_app(app)
    app.db = ma
#class for serialize db models
class MoviesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Movies

    id = ma.auto_field()
    title = ma.auto_field()
    release_date = ma.auto_field()
    popularity = ma.auto_field()