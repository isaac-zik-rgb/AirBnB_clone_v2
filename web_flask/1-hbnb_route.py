#!/usr/bin/python3
"""A script that start up a flask web application"""
from flask import Flask
app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """print Hello"""
    return "Hello HBNB!"


@app.route('/hbnb')
def text():
    """print HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
