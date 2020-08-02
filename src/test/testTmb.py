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


def string(i):
    i = str(i)
    return i

def test_int():
    s = string(236)
    assert s == '236'
        

def search(title):
    search = tmdb.Search()
    response = search.movie(query=title)
    record = []
    for info in search.results:
        record.append(info['title'])
        record.append(info['release_date'])
        record.append(info['popularity'])
    return record
    


def test_movie():
    try:      
        result = search('ggigiuiug')
        tittle = result[0]
        assert print(tittle)

    


