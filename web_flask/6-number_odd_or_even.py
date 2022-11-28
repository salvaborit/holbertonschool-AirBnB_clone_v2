#!/usr/bin/python3
"""Task 4"""
from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def number(n):
    """Displays 'n is a number' only if 'n' var is an int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Displays an html page if 'n' is an int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Displays an html page if 'n' is an int"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)