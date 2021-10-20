
import json
from flask_cors import CORS
import pandas as pd
import requests

client_access_token = "XeImR34nFU5IF4bocaMMdB9WST0JPDN3wXMsIla34bZzY8uOyzMmON2_lvBLNR5J"

def search_term(term):
    genius_search_url = f"http://api.genius.com/search?q={term}&access_token={client_access_token}"

    response = requests.get(genius_search_url)
    json_data = response.json()

    #pdf = pd.read_json(json_data)
    pdf = pd.DataFrame.from_dict(json_data)
    print(pdf['response'])

    xdf = pdf['response'].to_dict()
    ydf = pd.DataFrame(columns={'song_title'})

#temp = 0
    for i in xdf.keys():
        #temp += 1
        #if temp > 10:
            #break

        print(xdf[i])
        song_title = xdf[i]['result']['full_title']
        container = {'full_title': song_title}

        ydf = ydf.append(container, ignore_index=True)

    text= ydf.to_string(header=False)

    print(text)

    return text

search_term('moon')


    