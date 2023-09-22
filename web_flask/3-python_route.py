#!/usr/bin/python3
"""A Script that starts a flask web application"""
from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """print Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_cool(text):
    """dispaly 'C' followed by the value of the text"""
    return "C {}".format(text.replace('_', " "))


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text="cool"):
    return "Python {}".format(text.replace('_', " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
