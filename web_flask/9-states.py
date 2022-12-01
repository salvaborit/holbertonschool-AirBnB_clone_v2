#!/usr/bin/python3
""" Module 7-states_list.py """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    from models import storage
    storage.close()


app.route('/states')
def states():
    """ Renders all states """
    from models import storage
    from models.state import State
    from flask import render_template

    return render_template('9-states.html',
                           states=storage.all(State).values())

app.route('/states/<id>')
def state_id(id):
    """ Renders state by id """
    from models import storage
    from models.state import State
    from models.city import City
    from flask import render_template

    for state in storage.all(State).values():
        st_name = False
        if state.id == id:
            st_name = state.name

    return render_template('9-states.html',
                           states=storage.all(State).values(),
                           cities=storage.all(City).values(),
                           state_id=id,
                           state_name=st_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
