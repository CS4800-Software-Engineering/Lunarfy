#import test
from flask import Flask, url_for, session, request, redirect
import json
#import lyricsgenius
import pandas as pd
import requests
from IPython.core.display import HTML
import google
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
#import unittest

# database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

application = Flask(__name__)
app = application

# database
# Use a service account
cred = credentials.Certificate(
    '/home/LunarVerse/mysite/lunarfy-9c860-firebase-adminsdk-bwf4g-98b586e21d.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()


def create_account(username, password):
    doc_ref = db.collection(u'sampleData').document(username)
    # check_valid_password()
    doc_ref.set({
        u'username': username,
        u'password': password
    })
    print(username + " successful")


def check_valid_password(password):
    if len(password) >= 8:
        valid: bool = True
    else:
        valid: bool = False
    return valid


def check_username(username):
    exists: bool = False
    try:
        tempname = db.collection(u'sampleData').document(username).get()
        if tempname == username:
            exists = True
    except google.cloud.exceptions.NotFound:
        print(u'Username not found')
    return exists


def check_wordbank(word):
    copy: bool = False
    curWord = db.collection(u'sampleData').document(word).get()
    if curWord == word:
        copy = True
    return copy


def check_login(username, password):
    if not check_username(username):
        return

    # use check_username and check_password method

    users_ref = db.collection(u'sampleData').document(username)
    db_password = users_ref.get(
        field_paths={'password'}).to_dict().get('password')
    if(db_password == password):
        return True
    else:
        return False

# testing
# create_account("Lunarbit","123")
# print(check_login("Lunarbit","123#"))


"""@application.route('/', methods=['GET'])
def hello():
  return "This is working!"
"""

client_access_token = "XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J"


@application.route("/search/<term>")
def search_term(term):
    genius_search_url = f"http://api.genius.com/search?q={term}&access_token={client_access_token}"

    response = requests.get(genius_search_url)
    json_data = response.json()

    #pdf = pd.read_json(json_data)
    pdf = pd.DataFrame.from_dict(json_data)

    hit_list = pdf['response'][1]
    ydf = pd.DataFrame(columns={'full_title'})

#temp = 0
    for hit in hit_list:
        #temp += 1
        # if temp > 10:
        # break

        song_title = hit['result']['full_title']

        container = {'full_title': song_title}

        ydf = ydf.append(container, ignore_index=True)

    text = ydf.to_string(header=False, index=False)

    return text


'''def get_image_html(link):
  image_html = f"<img src='{link}' width='500px'>"
  return image_html'''

'''if __name__ == "__main__":
  application.run()'''


def say_hello(username="World"):
    return '<p>Hello %s!</p>\n' % username


# TEST
header_text = '''
  <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
  <p><em>Hint</em>: This is a RESTful web service! Append a username
  to the URL (for example: <code>/Thelonious</code>) to say hello to
  someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

application.add_url_rule('/', 'index', (lambda: header_text +
                                        say_hello() + instructions + footer_text))

application.add_url_rule('/<username>', 'hello', (lambda username:
                                                  header_text + say_hello(username) + home_link + footer_text))


# SPOTIFY


application.secret_key = 'LunarBits'
# app.config['SESSION_LunarBits'] = 'spotify-login-session'
application.config['SESSION_LunarBits13132'] = 'spotify-login-session'
TOKEN_INFO = "token_info"


@application.route('/login_spotify')
def login_spotify():
    spotify_oauth = create_spotify_oauth()
    auth_url = spotify_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)


@application.route('/redirect')
def redirectPage():
    spotify_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get("code")
    token_info = spotify_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('getTracks', _external=True))


@application.route('/getTracks')
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
        songs = sp.current_user_saved_tracks(limit=50, offset=i*50)['items']
        for item in songs:
            track = item['track']
            song_artist_list.append(
                track['name'] + ' - ' + track['artists'][0]['name'])
        i += 1
        all_songs += songs
        if (len(songs) < 50):
            break

    # return str(all_songs)
    return str(song_artist_list)


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise Exception("exception")
    current_time = int(time.time())
    is_expired = token_info['expires_at'] - current_time < 60
    if (is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(
            token_info['refresh_token'])
    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id="fe1c7e16a583463eb0ae80eeea7970ea",
        client_secret="87df5a64860a4c98b0be4659751fa4fa",
        redirect_uri=url_for('redirectPage', _external=True),
        scope="user-library-read")


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

#application.run(host = "0.0.0.0")