from flask import Flask, jsonify
from os import getenv

greetings = getenv('GREET', 'Hello')

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({'message': greetings})