from flask import Flask
import requests
import json
from flask_cors import CORS
import emojis
# from googletrans import Translator
import wikipedia
from googlesearch import search
import numpy as np


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
  return "hello world"

client_access_token = "XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J"

@app.route("/search/<term>")
def search_term(term):
  genius_search_url = f"http://api.genius.com/search?q={term}&access_token={client_access_token}"

  response = requests.get(genius_search_url)
  json_data = response.json()

  return json_data

@app.route("/google/<topic>")
def google(topic):
  user = str(topic)
  result = str(search(user, num_results=1, lang="en", proxy=None))
  return result

@app.route("/array2str")
def array2string() :
  arr = np.array([4, -8, 7 ])
  out_arr = np.array_str(arr)
  return(out_arr)


# @app.route("/wiki/<searchTerm>")
# def wiki(searchTerm):
#   result = wikipedia.page(searchTerm)
#   emojified = emojis.encode("What is " + searchTerm + "? :mag_right: ")
#   return emojified + result.summary


# @app.route('/detectLanguage/<myText>')
# def detectLanguage(myText):
#   translator = Translator()
#   myText = str(myText)
#   aString = str(translator.detect(myText))
#   return aString

# @app.route('/baseball_playoff_app/<teamName>')
# def playoffApp(teamName):
#   team = str(teamName)
#   result = sports.get_team_info(sports.BASEBALL, team)
#   return result


app.run(host = "0.0.0.0")
