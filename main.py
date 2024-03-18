from flask import Flask, jsonify, request
from os import getenv

_VERSION = '1.2.0'

greetings = getenv('GREET', 'Hello')
default_name = getenv('DEFAULT_NAME', 'Stranger')

app = Flask(__name__)


@app.route("/")
def greet():
    return jsonify({'message': greetings})


@app.route("/name/<name>")
def parameter(name):
    return jsonify({'message': f'{greetings}, {name}'})


@app.route("/header")
def parameter():
    name = request.headers.get('name', default_name)
    return jsonify({'message': f'{greetings}, {name}'})


@app.route("/query")
def parameter():
    name = request.args.get('name', default_name)
    return jsonify({'message': f'{greetings}, {name}'})
