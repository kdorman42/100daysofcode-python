from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

load_dotenv('../env_vars/100doc_python_env_vars.env')

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
my_spotify_id = sp.current_user()["id"]

results = sp.search(q=f"track:Try Again year:2000")
print(results["tracks"]["items"][0]["uri"])