#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask
moc = Flask(__name__)


@moc.route('/', strict_slashes=False)
def ind():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@moc.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    moc.run(host='0.0.0.0', port='5000')
