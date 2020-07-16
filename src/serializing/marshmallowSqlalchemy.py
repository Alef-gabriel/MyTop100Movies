from flask_marshmallow import Marshmallow
from src.models.modelsSqlalchemy import Movies

marshmallow = Marshmallow()

def MarshmallowConfigure(app):
    marshmallow.init_app(app)
    app.db = marshmallow

class MoviesSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Movies

    id = marshmallow.auto_field()
    title = marshmallow.auto_field()
    release_date = marshmallow.auto_field()
    popularity = marshmallow.auto_field()