import pytest

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