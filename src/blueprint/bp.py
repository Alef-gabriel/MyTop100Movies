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
        def search(title):
            search = tmdb.Search()
            response = search.movie(query=title)
            search_info = [str(x) for x in search.results]
            return json.dumps(search_info)

        data = request.get_json()
        #t = request.form['movie']
        m = search('The Bourne')
        new_user = Movies(title=m['title'],
         release_date=m['release_date'],popularity=m['popularity'])
        db.session.add(new_user)
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