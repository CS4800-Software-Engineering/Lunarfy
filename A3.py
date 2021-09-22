from flask import Flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/example")
def hello_world():
  return "Hello from CS4800 Software Engineering"

@app.route("/Flora")
def hello_flora():
  return "Hello from Flora"

@app.route("/Rachel", methods=['GET'])
def hello_rachel():
  return "<h1>hi hi hi from Rachel</h1>"

@app.route("/Emily")
def this_is_em():
  return "This is Emily wheeeee"
  
@app.route("/Neha")
def neha_j():
  return "Neha has entered the group chat"

@app.route("/Nathan")
def nate_dog():
  return "Nathan from CS 4800 is here"

app.run(host = "0.0.0.0")
