#!/usr/bin/python3
"""Task 4"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """Displays 'Hello HBNB!' on route '/'"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Displays 'HBNB' on route '/hbnb'"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """Displays 'C' followed by val of 'text' var on route '/c/<text>'"""
    return 'C ' + str(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """Displays 'Python' followed by val of
    'text' var on route '/python/<text>'"""
    return 'Python ' + str(text.replace('_', ' '))


@app.route('/number/<n>')
def number(n):
    """Displays 'n is a number' only if 'n' var is an int"""
    if type(n) is int:
        return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
