from time import sleep
from os import getenv

from flask import Flask, jsonify, request

_VERSION = '1.3.1'

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
def header():
    name = request.headers.get('name', default_name)
    return jsonify({'message': f'{greetings}, {name}'})


@app.route("/query")
def query():
    name = request.args.get('name', default_name)
    return jsonify({'message': f'{greetings}, {name}'})


@app.route("/delay/<int:delay>")
def delayed(delay):
    sleep(delay)
    return jsonify({'message': f'{greetings} {default_name}, after {delay} milliseconds'})