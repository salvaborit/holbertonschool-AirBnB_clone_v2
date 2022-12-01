#!/usr/bin/python3
"""
    Module 10-hbnb_filters
"""


from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


app.route('/hbnb_filters')
def hbnb_filt():
    """ Renders filters """
    from models import storage
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    return render_template('10-hbnh_filters.html',
                           states=storage.all(State),
                           cities=storage.all(City),
                           amenities=storage.all(Amenity))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
