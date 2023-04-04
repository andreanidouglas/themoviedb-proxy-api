import requests
import json
from config.config import API_keys

token = API_keys.movie_database_api


class Movie:
    """Movie represents a single movie in TheMovieDatabase API"""

    def __init__(self, id, title, popularity, overview, poster_path):
        self.id = id
        self.title = title
        self.popularity = popularity
        self.overview = overview
        self.poster_path = poster_path


class Movies:
    def __sortmovies(self, m: Movie) -> list[Movie]:
        """Helper to sort movies by popularity"""

        return m.popularity

    def get_movies(self, page=1):
        """Get movies from popular api sorted by popularity"""

        url = f"https://api.themoviedb.org/3/movie/popular?api_key={token}&page={page}"
        get = requests.get(url)
        json_get = json.loads(get.text)

        movies = []
        for movie in json_get['results']:
            m = Movie(
                    movie['id'],
                    movie['original_title'],
                    movie['popularity'],
                    movie['overview'],
                    movie['poster_path']
                )
            movies.append(m)

        movies.sort(reverse=True, key=self.__sortmovies)
        self.movies = movies

    def get_movie(self, movie_id):
        """Get a movie from api"""

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={token}"
        get = requests.get(url)
        movie = json.loads(get.text)

        m = Movie(
                    movie['id'],
                    movie['original_title'],
                    movie['popularity'],
                    movie['overview'],
                    movie['poster_path']
        )
        self.movie = m


class MovieEncoder(json.JSONEncoder):
    """Helper to allow movie to be encoded as JSON"""

    def default(self, o):
        return o.__dict__
