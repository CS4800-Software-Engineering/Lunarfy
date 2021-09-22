from flask import Flask
import json
#import lyricsgenius
from flask_cors import CORS
import pandas as pd
import requests
from IPython.core.display import HTML

app = Flask(__name__)
CORS(app)


client_access_token = "XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J"
#genius = lyricsgenius.Genius("XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J")


@app.route("/search/<term>")
def search_food(term):
  genius_search_url = f"http://api.genius.com/search?q={term}&access_token={client_access_token}"

  response = requests.get(genius_search_url)
  json_data = response.json()

  return json_data #What data type to return ???

  
'''def get_image_html(link):
  image_html = f"<img src='{link}' width='500px'>"
  return image_html'''

app.run(host = "0.0.0.0")
