#!/usr/bin/python3
"""
Module number_route
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_hello():
        return "HBNB"


@app.route("/c/<text>")
def c_route(text):
        res = text.replace('_', ' ')
        return "C " + res


@app.route("/python")
@app.route("/python/<text>")
def python_route(text="is cool"):
        res = text.replace('_', ' ')
        return "Python " + res


@app.route("/number/<int:n>")
def number_route(n):
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
