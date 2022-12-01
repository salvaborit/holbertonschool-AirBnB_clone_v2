#!/usr/bin/python3
"""
Module 1-hbnb_route
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
