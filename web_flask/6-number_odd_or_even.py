#!/usr/bin/python3
"""
Module 5-number_odd_or_even
"""
from flask import Flask, render_template


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


@app.route("/number_template/<int:n>")
def number_template_route(n):
        return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even_route(n):
        return render_template("6-number_odd_or_even.html", number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
