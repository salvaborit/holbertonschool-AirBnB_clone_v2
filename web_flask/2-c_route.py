#!/usr/bin/python3
"""Task 1"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route(f'/c/{str(text)}', strict_slashes=False)
def c():
    return str(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
