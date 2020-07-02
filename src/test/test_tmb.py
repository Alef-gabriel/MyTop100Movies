import pytest

import tmdbsimple as tmdb
tmdb.API_KEY = '108c8c9eec3f15e22c2ad1db51a28436'

def test_tmb():
    movie = tmdb.Movies(603)
    response = movie.info()
    assert movie.title