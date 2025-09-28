import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "###"
SPOTIPY_CLIENT_SECRET = "###"
SPOTIPY_REDIRECT_URI = "###"
SCOPE = "playlist-modify-private"

year_choice = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

URL = f"https://www.billboard.com/charts/hot-100/{year_choice}"

response = requests.get(URL, headers=header)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
titles = soup.find_all(name = "h3", class_ = "lrv-u-font-size-18@tablet", id="title-of-a-story")
list_of_songs = [item.getText().strip()for item in titles]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))
user = sp.current_user()
user_id = user["id"]

spotify_song_uris = []
for song in list_of_songs:
    try:
        result = sp.search(song)
    except Exception as e:
        pass
        print("Not a song")
    else:
        all = result["tracks"]["items"]
        popularity = [int(all[num]["popularity"]) for num in range (0, len(all))]
        uri = [all[num]["uri"] for num in range (0, len(all))]
        index_for_max_score = popularity.index(max(popularity))
        spotify_song_uris.append(uri[index_for_max_score])

new_playlist = sp.user_playlist_create(user_id, f"{year_choice}", public=False, collaborative=False, description="My new playlist!")
sp.playlist_add_items(new_playlist["id"], spotify_song_uris, position = None)



