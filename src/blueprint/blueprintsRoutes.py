from flask import Blueprint, json, jsonify, request, render_template
from src.models.modelsSqlalchemy import db , Movies
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
            record = []

            for info in search.results:
                record.append(info['title'])
                record.append(info['release_date'])
                record.append(info['popularity'])
            return record

        m = search('The Bourne')
        
        newMovie = Movies(title=m[0],
         release_date=m[1],popularity=m[2])

        db.session.add(newMovie)
        db.session.commit()

    return render_template('myMovies.htm')

@blueprintRote.route('/del/<int:id>', methods =['DELETE'])
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


@blueprintRote.route('/Movies',methods =['GET'])
def get_movies():
    #GET
    movies = Movies.query.all()

    return jsonify(movies)