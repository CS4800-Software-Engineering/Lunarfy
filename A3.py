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

@app.route('/', methods=['GET'])
def hello_rachel():
  return "<h1>hello from Rachel</h1>"

@app.route("/Emily")
def this_is_em():
  return "This is Emily wheeeee"

app.run(host = "0.0.0.0")
