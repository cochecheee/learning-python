

""" ========== TO CREATE YOUR OWN ENV VAR TYPE 
    $Env:Foo = 'An example'   to create env_var windows
    os.environ.get(“API_KEY_NAME”)   to access env var

    $Env:Foo = ''    to delete env var

"""

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
song_soup = soup.find_all("h3", "a-no-trucate")
song_names = [s.getText(strip=True) for s in song_soup]
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET,
                                                    redirect_uri=REDIRECT_URI,
                                                    scope="playlist-modify-private"))

user = spotify.current_user()['id']

name = f"{date} Billboard 100"
print(f"Generating a playlist for user: {user} called {name}")

# create playlist and get id of playlist
playlist_id = spotify.user_playlist_create(user, name, public=False, collaborative=False,
                                           description=f'The top 100 songs on {date}')['id']

def get_track_id(song):
    track_id = spotify.search(song, limit=1)['tracks']['items'][0]['uri']
    return track_id


track_ids = [get_track_id(song) for song in song_names]
# add song to playlist 
spotify.playlist_add_items(playlist_id, track_ids)

