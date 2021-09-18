from flask import Flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


food_db = [
  {
    "name" : "Subway Sepcial 1",
    "price" : 5.99    
  },
  {
    "name" : "Starbucks Lunch",
    "price" : 4.29    
  },
  {
    "name" : "Burger King",
    "price" : 4.99    
  }
]

@app.route("/search/<budget>")
def search_food(budget):
  budget = float(budget)
  res = []
  for food in food_db:
    if food["price"] <= budget:
      res.append(food)
  return json.dumps(res)

@app.route("/hello")
def hello_world():
  return "Hello from CS4800 Software Engineering"

app.run(host = "0.0.0.0")
'''

#import lyricsgenius
import pandas as pd
import requests
from IPython.core.display import HTML

client_access_token = "XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J"
#genius = lyricsgenius.Genius("XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J")
search_term = "Missy Elliott"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"


response = requests.get(genius_search_url)
json_data = response.json()

missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']['pageviews']])
    
#Make a Pandas dataframe from a list
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views']
print(missy_df)

def get_image_html(link):
  image_html = f"<img src='{link}' width='500px'>"
  return image_html

missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']['pageviews'], song['result']['song_art_image_url']])
    
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views','album_cover_url']

#Use the function get_image_html()
missy_df['album_cover'] = missy_df['album_cover_url'].apply(get_image_html)
#print(missy_df)
HTML(missy_df[['album_cover', 'page_views', 'song_title']].to_html(escape=False))
'''