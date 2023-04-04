import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass


load_dotenv(find_dotenv())


@dataclass(frozen=True)
class API_keys:
    """Store all sensitive key as they are read from config/.env file"""

    movie_database_api = os.getenv('THEMOVIEDATABASE_API')
