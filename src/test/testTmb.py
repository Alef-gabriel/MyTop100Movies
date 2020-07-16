import pytest
import json
import io
import tmdbsimple as tmdb

tmdb.API_KEY = '108c8c9eec3f15e22c2ad1db51a28436'

def test_tmb():
    movie = tmdb.Movies(603)
    response = movie.info()
    assert movie.title

def test_title():
    title = 'The Bourne'
    search = tmdb.Search()
    response = search.movie(query=title)

    for s in search.results:
        print(s['title'], s['id'], s['release_date'], s['popularity'])

def test_list():
    lista = []
    morango = 'morango'

    lista.append(morango)

    print(lista)


def test_t():
    title = 'The Bourne'
    search = tmdb.Search()
    response = search.movie(query=title)

def search(title):
    title = title
    search = tmdb.Search()
    response = search.movie(query=title)

def string(i):
    i = str(i)
    return i

def test_int():
    s = string(236)
    assert s == '236'
        

def search(title):
    """search movie
    
    Keyword arguments:
    argument -- search for a movie title in an api of the movie
    Return: returns a dump in json
    """
    search = tmdb.Search()
    response = search.movie(query=title)
    search_info = [str(x) for x in search.results]
    return json.dumps(search_info)
    


def test_movie():
    y = search('The Bourne')
    print(y)


