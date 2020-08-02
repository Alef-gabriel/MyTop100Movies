from flask_marshmallow import Marshmallow
from src.models.modelsSqlalchemy import Movies

ma = Marshmallow()

def marshmallowConfigure(app):
    ma.init_app(app)
    app.ma = ma

class MoviesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Movies

    id = ma.auto_field()
    title = ma.auto_field()
    release_date = ma.auto_field()
    popularity = ma.auto_field()
