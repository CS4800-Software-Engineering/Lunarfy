from flask import Flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/example")
def hello_world():
  return "Hello from CS4800 Software Engineering"

app.run(host = "0.0.0.0")
