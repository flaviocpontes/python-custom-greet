from flask import Flask, jsonify
from os import getenv

_VERSION = '1.1.0'

greetings = getenv('GREET', 'Hello')

app = Flask(__name__)


@app.route("/")
def greet():
    return jsonify({'message': greetings})


@app.route("/<name>")
def parameter(name):
    return jsonify({'message': f'{greetings}, {name}'})
