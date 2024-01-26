#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
moc = Flask(__name__)


@moc.route('/states_list', strict_slashes=False)
def states_l():
    """display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@moc.teardown_appcontext
def teardown_n(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    moc.run(host='0.0.0.0', port='5000')
