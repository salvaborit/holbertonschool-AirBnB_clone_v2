#!/usr/bin/python3
"""
Module c_route
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


if __name__ == '__main__':
        app.run(host=('0.0.0.0'),
                port=int('5000'), threaded=True)
