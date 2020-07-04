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
def post_movies():
    #POST
    if  request.method == 'POST':
        #data = request.get_json()
        #title = request.form['text']
        tt = 'The Bourne'
        search = tmdb.Search()
        response = search.movie(query=tt)

        new_movie = Movies(title=search.results['title'], release_date=search.results['release_date'],
         popularity=search.results['popularity'])
        db.session.add(new_movie)
        db.session.commit()
    return render_template('myMovies.htm')

    #DELETE
@bp.route('/del/<int:id>', methods =['DELETE'])
def del_movies(id):
    if request.method == 'DELETE':
        Movies.query.filter(Movies.id == id).delete()
        db.session.commit()
    return ''

    #PUT
    #movies= Movies.query.filter(Movies.id == id)
    #movies.update(request.json)
    #if not movies:
        #return ''
    #else:
        #db.session.commit()


@bp.route('/Movies',methods =['GET'])
def get_movies():
    #GET
    bs = MoviesSchema(many=True)
    movies = Movies.query.all()

    return bs.jsonify(movies)