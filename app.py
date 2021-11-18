#import test
from flask import Flask, url_for, session, request, redirect, render_template
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
'''cred = credentials.Certificate(
    'lunarfy-9c860-firebase-adminsdk-bwf4g-98b586e21d.json')'''
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/result",methods = ["POST", "GET"])
def create_account():


    # check_valid_password()


    if request.method == "POST":        #Only listen to POST
        result = request.form           #Get the data submitted
        email = result["email"]
        password = result["password"]
        try:

            if check_username(email):
                text = "Account already exist"

            else:
                text = "Congrats"

            doc_ref = db.collection(u'sampleData').document(email)
            doc_ref.set({
            u'username': email,
            u'password': password
            })


            text = "!!!Congrats"
            return render_template("confirm.html", data=text)
            #Go to welcome page
            #return redirect(url_for('confirm'), text)

        except:
            #If there is any error, redirect to register
            return redirect(url_for('weblogin'))

    else:
       return redirect(url_for('signup'))





@app.route("/confirm")
def confirm(text):
    return render_template("confirm.html", data=text)


@app.route("/login")
def weblogin():
    return render_template("login.html")






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


@app.route("/checklogin",methods = ["POST", "GET"])
def check_login():

    if request.method == "POST":        #Only listen to POST
        result = request.form           #Get the data submitted
        email = result["abc"]
        password = result["haha"]
        try:

            if check_username(email):
                text = "Account already exist"

            else:
                text = "Congrats"

            users_ref = db.collection(u'sampleData').document(email)
            db_password = users_ref.get(
            field_paths={'password'}).to_dict().get('password')

            if(db_password == password):
                return render_template("confirm.html", data="same password")
            else:
                return render_template("confirm.html", data="different password")


            #Go to welcome page
            #return redirect(url_for('confirm'), text)

        except:
            #If there is any error, redirect to register
            return render_template("confirm.html", data="error")

    else:
       return render_template("confirm.html", data="error2")





@application.route("/about.html")
def about():
    return render_template("about.html")

@application.route("/signup")
def signup():
    return render_template("signup.html", data="test")

# testing
# create_account("Lunarbit","123")
# print(check_login("Lunarbit","123#"))

# SPOTIFY
application.secret_key = 'LunarBits'
# app.config['SESSION_LunarBits'] = 'spotify-login-session'
application.config['SESSION_LunarBits13132'] = 'spotify-login-session'
TOKEN_INFO = "token_info"

@application.route('/test/<track>')
def search_sp_id(track):
    try:
        token_info = get_token()
    except:
        print("not logged in")
        return redirect("/")
        # redirect(url_for("login", _external = True))
    sp = spotipy.Spotify(auth=token_info['access_token'])

    json_data = sp.search(q='track:' + track, type='track')

    track_id = json_data['tracks']['items'][0]['id']
    embed_song = f'<iframe src="https://open.spotify.com/embed/track/{track_id}?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    temp = []
    temp.append(embed_song)
    embed_song2 = f'<iframe src="https://open.spotify.com/embed/playlist/4pU0EfbTZhIO8NcdcubEUw?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>'
    temp.append(embed_song2)
    #return track_id
    return render_template("search.html", data=temp)
    #return embed_song


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


#Genius API
client_access_token = "XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J"


@application.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":
	    lyric = request.form["lyric"] #clear previous data
	    return redirect(url_for("search_term", term=lyric))
    else:
        return render_template("search.html")


##helper method
#https://www.youtube.com/watch?v=uqr-e-dkkNI
#https://www.youtube.com/watch?v=9MHYHgh4jYc
@app.route("/searchfor<term>")
def search_term(term):
    try:
        token_info = get_token()
    except:
        print("not logged in")
        return redirect("/") #if not login in return title
        # redirect(url_for("login", _external = True))

    sp = spotipy.Spotify(auth=token_info['access_token'])

    genius_search_url = f"http://api.genius.com/search?q={term}&access_token={client_access_token}"

    response = requests.get(genius_search_url)
    json_data = response.json()

    #pdf = pd.read_json(json_data)
    pdf = pd.DataFrame.from_dict(json_data)

    hit_list = pdf['response'][1]
    #ydf = pd.DataFrame(columns={'full_title'})

#temp = 0
    text = []
    for hit in hit_list:
        #temp += 1
        #if temp > 10:
            #break

        song_title = hit['result']['title']

#song title contain () might cause error
#https://stackoverflow.com/questions/3774015/how-do-i-get-all-iframe-elements
#google list of iframes



        #container = {'full_title': song_title}
        #track_player = search_sp_id(song_title)
        json_data = sp.search(q='track:' + song_title, type='track')

        track_id = json_data['tracks']['items'][0]['id']
        embed_song = f'<iframe src="https://open.spotify.com/embed/track/{track_id}?utm_source=generator" width="450" height="80" frameBorder="0" allowfullscreen="/" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe> <br>'

        #items = song_id['artists']['items']
        #ydf = ydf.append(container, ignore_index=True)

        #text.append(song_title)
        text.append(embed_song)

    #get rid of repeat
    #"Spring" not working

    #text= ydf.to_string(header=False, index=False)
    return render_template("search.html", data=text)
    #return text



if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

#application.run(host = "0.0.0.0")