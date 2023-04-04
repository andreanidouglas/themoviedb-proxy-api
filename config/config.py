import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass


load_dotenv(find_dotenv())


@dataclass(frozen=True)
class API_keys:
    movie_database_api = os.getenv('THEMOVIEDATABASE_API')
