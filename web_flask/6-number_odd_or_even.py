#!/usr/bin/python3
""" A script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ display   'Hello HBNB'"""
    return "Hello HBNB"


@app.route('/hbnb')
def hbnb():
    """ Display HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_cool(text):
    """Display 'C' followed by the value 'text'"""
    return "C {}".format(text.replace('_', " "))


@app.route('/python/(<text>')
def python_is_cool(text="is cool"):
    """ Display "pythhon" follow by the value of the text"""
    return "Python {}".format(text.replace('_', " "))


@app.route('/number/<int:n>')
def number(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ render a html templates with the value of n"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
