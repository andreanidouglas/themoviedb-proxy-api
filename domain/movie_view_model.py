import json

from data.movies import Movies, MovieEncoder


class MoviesViewModel:
    def get_movies_use_case(self, page=1):
        m = Movies()
        m.get_movies(page)
        return json.dumps(m.movies, indent=4, cls=MovieEncoder)

    def get_movie_use_case(self, movie_id):
        m = Movies()
        m.get_movie(movie_id)
        return json.dumps(m.movie, indent=4, cls=MovieEncoder)
