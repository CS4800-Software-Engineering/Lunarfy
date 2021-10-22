import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, url_for, session, request, redirect
import time
<<<<<<< Updated upstream:SpotifyTest/app.py
=======
import os
>>>>>>> Stashed changes:Spotify Login/app.py

# App config
app = Flask(__name__)


<<<<<<< Updated upstream:SpotifyTest/app.py
=======
app.secret_key = 'LunarBits'
# app.config['SESSION_LunarBits'] = 'spotify-login-session'
app.config['SESSION_LunarBits13132'] = 'spotify-login-session'
TOKEN_INFO = "token_info"


>>>>>>> Stashed changes:Spotify Login/app.py
@app.route('/')
def login():
    spotify_oauth = create_spotify_oauth()
    auth_url = spotify_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)


@app.route('/redirect')
def redirectPage():
    spotify_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get("code")
    token_info = spotify_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('getTracks', _external = True))


@app.route('/getTracks')
def getTracks():
    try:
        token_info = get_token()
    except:
        print("not logged in")
        return redirect("/")
        # redirect(url_for("login", _external = True))
    sp = spotipy.Spotify(auth=token_info['access_token'])

    all_songs = []
    i = 0
    song_artist_list = []
    # song_list = []
    while True:
        songs = sp.current_user_saved_tracks(limit=50, offset = i*50)['items']
        for item in songs:
            track = item['track']
            song_artist_list.append(track['name'] + ' - ' + track['artists'][0]['name'])
        i += 1
        all_songs += songs
        if (len(songs) < 50):
            break
<<<<<<< Updated upstream:SpotifyTest/app.py
    return str(len(all_songs))
    # return str(all_songs)
=======

    # return str(all_songs)
    return str(song_artist_list)

>>>>>>> Stashed changes:Spotify Login/app.py

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise Exception("exception")
    current_time = int(time.time())
    is_expired = token_info['expires_at'] - current_time < 60
    if (is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
            client_id = "fe1c7e16a583463eb0ae80eeea7970ea",
            client_secret = "87df5a64860a4c98b0be4659751fa4fa",
            redirect_uri=url_for('redirectPage', _external=True),
<<<<<<< Updated upstream:SpotifyTest/app.py
            scope="user-library-read")

app.run(host = "0.0.0.0")

# @app.route('/')
# def login():
#     sp_oauth = create_spotify_oauth()
#     auth_url = sp_oauth.get_authorize_url()
#     print(auth_url)
#     return redirect(auth_url)

# @app.route('/authorize')
# def authorize():
#     sp_oauth = create_spotify_oauth()
#     session.clear()
#     code = request.args.get('code')
#     token_info = sp_oauth.get_access_token(code)
#     session["token_info"] = token_info
#     return redirect("/getTracks")

# @app.route('/logout')
# def logout():
#     for key in list(session.keys()):
#         session.pop(key)
#     return redirect('/')

# @app.route('/getTracks')
# def get_all_tracks():
#     session['token_info'], authorized = get_token()
#     session.modified = True
#     if not authorized:
#         return redirect('/')
#     sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
#     results = []
#     iter = 0
#     while True:
#         offset = iter * 50
#         iter += 1
#         curGroup = sp.current_user_saved_tracks(limit=50, offset=offset)['items']
#         for idx, item in enumerate(curGroup):
#             track = item['track']
#             val = track['name'] + " - " + track['artists'][0]['name']
#             results += [val]
#         if (len(curGroup) < 50):
#             break
    
#     df = pd.DataFrame(results, columns=["song names"]) 
#     df.to_csv('songs.csv', index=False)
#     return "done"


# # Checks to see if token is valid and gets a new token if not
# def get_token():
#     token_valid = False
#     token_info = session.get("token_info", {})

#     # Checking if the session already has a token stored
#     if not (session.get('token_info', False)):
#         token_valid = False
#         return token_info, token_valid

#     # Checking if token has expired
#     now = int(time.time())
#     is_token_expired = session.get('token_info').get('expires_at') - now < 60

#     # Refreshing token if it has expired
#     if (is_token_expired):
#         sp_oauth = create_spotify_oauth()
#         token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

#     token_valid = True
#     return token_info, token_valid


# def create_spotify_oauth():
#     return SpotifyOAuth(
#             client_id="id",
#             client_secret="secret",
#             redirect_uri=url_for('authorize', _external=True),
#             scope="user-library-read")
=======
            scope="user-library-read")
>>>>>>> Stashed changes:Spotify Login/app.py
