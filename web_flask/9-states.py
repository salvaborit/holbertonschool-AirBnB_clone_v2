#!/usr/bin/python3
"""
Module 9-states
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    from models import storage
    from models.state import State
    return render_template("9-states.html",
                           states=storage.all(State))


@app.route("/states/<id>")
def state_cities(id):
    from models import storage
    from models.state import State
    from models.city import City
    for state in storage.all(State).values():
        state_name = False
        if state.id == id:
            state_name = state.name
            break

    return render_template("9-states.html",
                           states=storage.all(State),
                           cities=storage.all(City),
                           state_id=id,
                           state_name=state_name)


@app.teardown_appcontext
def teardown_db(exception):
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.run(host=('0.0.0.0'),
            port=int('5000'), threaded=True)
