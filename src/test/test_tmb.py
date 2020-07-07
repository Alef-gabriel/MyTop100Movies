import pytest
import json

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

def test_a():
    t = 'The Bourne'

    movie = tmdb.Movies(t)
    response = movie.info()
    movie.title

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
        
def web_movie(title):
    title = title
    search = tmdb.Search()
    response = search.movie(query=title)

    srr = search.results.decode('utf-8')
        
    return json.loads(srr)

def test_movie():
    web_movie('The Bourne')