#!/usr/bin/python3
""" A script that starts a Flask application """
from flask import Flask
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """ close a database season"""
    storage.close()


@app.route('/cities_by_state')
def states_list():
    """ /states_list route"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
