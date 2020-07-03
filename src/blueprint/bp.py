from flask import Blueprint, json, jsonify, request, render_template
from src.models.mod import db , Movies
from src.ma import MoviesSchema
import tmdbsimple as tmdb

#key of api
tmdb.API_KEY = '108c8c9eec3f15e22c2ad1db51a28436'
#Create blueprint
bp = Blueprint('bp', __name__)

#first route
@bp.route('/', methods =['GET','POST'])
def get_all():
    #GET
    bs = MoviesSchema(many=True)
    movies = Movies.query.all()
    #POST
    if request.method == 'POST':
        data = request.get_json()

        title = request.form['text']

        search = tmdb.Search()
        response = search.movie(query=title)

        if search:
            new_movie = search.results(title=data['title'], release_date=data['release_date'],
            popularity=data['popularity'])
            db.session.add(new_movie)
            db.session.commit()

    #DELETE
    Movies.query.filter(Movies.id == id).delete()
    db.session.commit()

    #PUT
    movies= Movies.query.filter(Movies.id == id)
    movies.update(request.json)
    if not movies:
        return ''
    else:
        db.session.commit()

    return render_template('myMovies.htm', movies=movies)
