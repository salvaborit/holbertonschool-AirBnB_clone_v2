#!/usr/bin/python3
""" Module 7-states_list.py """
from flask import Flask


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    from models import storage
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Renders all cities and states """
    from models import storage
    from models.state import State
    from models.city import City
    from flask import render_template

    return render_template('8-cities_by_states.html',
                           state_list=storage.all(State).values(),
                           city_list=storage.all(City).values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
