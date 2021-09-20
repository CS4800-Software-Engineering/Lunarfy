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

@app.route("/Rachel")
def hi_rachel():
  return "Hi! -Rachel"

@app.route("/Emily")
def this_is_em():
  return "This is Emily wheeeee"

app.run(host = "0.0.0.0")
