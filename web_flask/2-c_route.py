#!/usr/bin/python3
"""Task 2"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays 'Hello HBNB!' on route '/'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' on route '/hbnb'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C' followed by val of 'text' var on route '/c/<text>'"""
    return 'C ' + str(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
