from flask import Blueprint, json, jsonify, request, render_template
from src.models.modelsSqlalchemy import db , Movies
from src.serializing.marshmallowMovie import  MoviesSchema
import tmdbsimple as tmdb

tmdb.API_KEY = '108c8c9eec3f15e22c2ad1db51a28436'
blueprintRote = Blueprint('blueprintRote', __name__)

@blueprintRote.route('/', methods =['GET','POST'])
def post_movies():
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

        try:
            movieTitle = search('The Bourne')
            queryMovie = Movies(title=movieTitle[0],
            release_date=movieTitle[1],popularity=movieTitle[2])

            db.session.add(queryMovie)
            db.session.commit()

        except Exception as exceptError:
            if exceptError != None:
                print(f'Error: {exceptError}')

    return render_template('myMovies.html')

@blueprintRote.route('/del/<int:id>', methods =['DELETE'])
def del_movies(id):
    Movies.query.filter(Movies.id == id).delete()
    db.session.commit()
    return 'MOVIE DELETED'

    #PUT
    #movies= Movies.query.filter(Movies.id == id)
    #movies.update(request.json)
    #if not movies:
        #return ''
    #else:
        #db.session.commit()


@blueprintRote.route('/Movies',methods =['GET'])
def get_movies():
    ms = MoviesSchema(many=True)
    Mymovies = Movies.query.all()

    return ms.jsonify(Mymovies)