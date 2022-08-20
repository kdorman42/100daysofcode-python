import requests
import os
from dotenv import load_dotenv

load_dotenv('../env_vars/100doc_python_env_vars.env')

TMDB_API_KEY = os.environ['TMDB_API_KEY']
TMDB_API_URL = 'https://api.themoviedb.org/3/search/movie'

params = {
    "api_key": TMDB_API_KEY,
    "query": "Fargo"
}
r = requests.get(TMDB_API_URL, params=params)
r.raise_for_status()
res = r.json()['results']
print(res)
