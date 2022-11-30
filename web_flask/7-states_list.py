#!/usr/bin/python3
"""Task 7"""


from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/states_list')
def states_list():
    """ List of states """
    from models.state import State

    from models import storage
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """ Removes SQLAlchemy session after every request """
    from models import storage
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
