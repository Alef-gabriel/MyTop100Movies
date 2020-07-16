from flask import Blueprint, json, jsonify, request, render_template
from src.models.modelsSqlalchemy import database , Movies
from src.serializing.marshmallowSqlalchemy import MoviesSchema
import tmdbsimple as tmdb

tmdb.API_KEY = '108c8c9eec3f15e22c2ad1db51a28436'
blueprintRote = Blueprint('blueprintRote', __name__)

@blueprintRote.route('/', methods =['GET','POST'])
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
         release_date=str(m['release_date']),popularity=str(m['popularity']))
        database.session.add(new_user)
        database.session.commit()

    return render_template('myMovies.htm')

@blueprintRote.route('/del/<int:id>', methods =['DELETE'])
def del_movies(id):
    if request.method == 'DELETE':
        Movies.query.filter(Movies.id == id).delete()
        database.session.commit()
    return ''

    #PUT
    #movies= Movies.query.filter(Movies.id == id)
    #movies.update(request.json)
    #if not movies:
        #return ''
    #else:
        #db.session.commit()


@blueprintRote.route('/Movies',methods =['GET'])
def get_movies():
    #GET
    bs = MoviesSchema(many=True)
    movies = Movies.query.all()

    return bs.jsonify(movies)