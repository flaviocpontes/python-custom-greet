from flask import Flask, jsonify
from os import getenv

_VERSION = '1.0.0'

greetings = getenv('GREET', 'Hello')

app = Flask(__name__)


@app.route("/")
def greet():
    return jsonify({'message': greetings})
