from flask import Flask
import pandas as pd
import json
from flask_cors import CORS

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

@app.route("/hello")
def hello_world():
  return "Hello from CS4800 Software Engineering"

app.run(host = "0.0.0.0")