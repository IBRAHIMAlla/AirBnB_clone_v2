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


@moc.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@moc.route('/python', strict_slashes=False)
@moc.route('/python/<text>', strict_slashes=False)
def py_is_cool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    moc.run(host='0.0.0.0', port='5000')
