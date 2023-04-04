from flask import Flask, request
from domain.movie_view_model import MoviesViewModel

app = Flask(__name__)


@app.route("/api/movies")
def movies():
    m = MoviesViewModel()
    return m.get_movies_use_case(1)


@app.route("/api/movie")
def movie():
    m = MoviesViewModel()
    movie_id = request.args.get('id')
    return m.get_movie_use_case(movie_id)
