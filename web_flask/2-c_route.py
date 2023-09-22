#!/usr/bin/python3
""" A script that start up a flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """ print Hello HBNB!"""
    return "Hello HBNB!"



@app.route('/hbnb')
def hello():
    """ print HBNB"""
    return "HBNB"



@app.route('/c/<text>')
def c_is_fun(text):
    """ Display 'C' follow by the value of text"""
    return "C {}".format(text.replace("_", " "))



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
