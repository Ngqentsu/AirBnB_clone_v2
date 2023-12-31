#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Message that will display when executing / """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Message that will display when executing / """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """Message that will display when executing /c/<text> """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python(text='is cool'):
    """Message that will display when executing /python/<text> """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display “n is a number” only if n is an integer"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer"""
    if n % 2 == 0:
        number = 'even'
    else:
        number = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           number=number)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)