#!/usr/bin/python3
"""
Task 7
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    st = storage.all(State)
    return render_template("7-states_list.html", states=st)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host=('0.0.0.0'),
            port=5000, threaded=True)
