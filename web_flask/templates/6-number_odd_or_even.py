#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask, render_template
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
def c_i_s_fun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@moc.route('/python', strict_slashes=False)
@moc.route('/python/<text>', strict_slashes=False)
def py_is_cool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@moc.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@moc.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@moc.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        ev = 'even'
    else:
        ev = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           ev=ev)

if __name__ == '__main__':
    moc.run(host='0.0.0.0', port='5000')
