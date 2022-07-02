from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

load_dotenv('../env_vars/100doc_python_env_vars.env')


BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'  # + date in YYYY-MM-DD format
# TEST_DATE = '2000-08-12'

SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']

date_input = input("Which date do you want to travel to? YYYY-MM-DD:  ")
is_private = input("Should the playlist be private? Y or N:  ")
# date_input = TEST_DATE
date_year = date_input[:4]
bb_url = f"{BILLBOARD_URL}{date_input}/"

response = requests.get(url=bb_url)
top_100_page = response.text

soup = BeautifulSoup(top_100_page, 'html.parser')
songs = soup.find_all(class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
song_titles = [song.get_text().strip() for song in songs]

if is_private.lower() == 'y':
    scope = "playlist-modify-private"
    is_public = False;
else:
    scope = "playlist-modify-public"
    is_public = True

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
my_spotify_id = sp.current_user()["id"]

song_uris = []
for song in song_titles:
    results = sp.search(q=f"track:{song} year:{date_year}")
    if int(results["tracks"]["total"]) == 0:
        continue
    song_uris.append(results["tracks"]["items"][0]["uri"])

playlist_create = sp.user_playlist_create(user=my_spotify_id,
                                          name=f"{date_input} Billboard 100",
                                          public=is_public,
                                          description=f"Generated from a simple python project")
playlist_uri = playlist_create["uri"]
playlist_add = sp.playlist_add_items(playlist_uri, song_uris)






