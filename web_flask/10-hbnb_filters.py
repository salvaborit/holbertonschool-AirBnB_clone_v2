#!/usr/bin/python3
"""
    Module 10-hbnb_filters
"""


from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


app.route('/hbnb_filters')
def filters():
    """ Renders filters """
    return render_template('10-hbnh_filters.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
