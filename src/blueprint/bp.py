from flask import Blueprint, json, jsonify
from src.models.mod import db , Movies
from src.ma import MoviesSchema

#Create blueprint
bp = Blueprint('bp', __name__)

#first route
@bp.route('/my-Movies', methods =['GET'])
def get_all():
    bs = MoviesSchema(many=True)

    movies = Movies.query.all()

    return bs.jsonify(movies)
    