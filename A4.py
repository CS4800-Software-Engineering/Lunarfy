from flask import Flask
import pandas as pd
import json
from flask_cors import CORS

import emojis
import wikipedia

from googletrans import Translator

app = Flask(__name__)
CORS(app)

@app.route("/panda")
def hello_panda():
  data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
  }
  #load data into a DataFrame object:
  df = pd.DataFrame(data)
  return df.to_string()

#Emily Villalba: Using Emojis and Wikipedia libraries
@app.route("/wiki/<searchTerm>")
def wiki(searchTerm):
  result = wikipedia.page(searchTerm)
  emojified = emojis.encode("What is " + searchTerm + "? :mag_right: ")
  return emojified + result.summary

@app.route('/detectLanguage/<myText>')
def detectLanguage(myText):
  translator = Translator()
  myText = str(myText)
  aString = str(translator.detect(myText))
  return aString

app.run(host = "0.0.0.0")
