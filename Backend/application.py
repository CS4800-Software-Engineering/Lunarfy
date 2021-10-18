#import test
from flask import Flask
import json
#import lyricsgenius
from flask_cors import CORS
import pandas as pd
import requests
from IPython.core.display import HTML
import google
#import unittest

#database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

application = Flask(__name__)
app = application
CORS(application)

#database
# Use a service account
cred = credentials.Certificate('lunarfy-9c860-firebase-adminsdk-bwf4g-98b586e21d.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

def create_account(username, password):
  doc_ref = db.collection(u'sampleData').document(username)
  #check_valid_password()
  doc_ref.set({
    u'username': username,
    u'password': password
  })
  print(username + " successful")

def check_valid_password(password):
  if len(password) >= 8:
    valid:bool = True
  else:
    valid:bool = False
  return valid


def check_username(username):
  exists:bool = False
  try:
    tempname = db.collection(u'sampleData').document(username).get()
    if tempname == username:
      exists = True
  except google.cloud.exceptions.NotFound:
    print(u'Username not found')
  return exists

def check_wordbank(word):
  copy:bool = False
  curWord = db.collection(u'sampleData').document(word).get()
  if curWord == word:
    copy = True
  return copy

def check_login(username, password):
  if not check_username(username):
    return

  #use check_username and check_password method




  users_ref = db.collection(u'sampleData').document(username)
  db_password = users_ref.get(field_paths={'password'}).to_dict().get('password')
  if(db_password == password):
    return True
  else:
    return False

#testing
#create_account("Lunarbit","123")
#print(check_login("Lunarbit","123#"))

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

#title, artist, img, in  dict **maybe lyric that contain the keyword (link to lyric)
#title: [artist, img, link to lyric]

#wordpress player -> lyric
  return json_data #What data type to return ???

  
'''def get_image_html(link):
  image_html = f"<img src='{link}' width='500px'>"
  return image_html'''

'''if __name__ == "__main__":
  application.run()'''

def say_hello(username = "World"):
  return '<p>Hello %s!</p>\n' % username

#TEST
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

if __name__ == "__main__":
  # Setting debug to True enables debug output. This line should be
  # removed before deploying a production app.
  application.debug = True
  application.run()

#application.run(host = "0.0.0.0")