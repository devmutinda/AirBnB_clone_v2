#!/usr/bin/python3
"""
This module creates a Flask application
which manipulates storage
"""
from flask import Flask, render_template
# from models import storage
# from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def html_page():
    """
    Renders a html template
    """
    from models import storage
    from models.state import State
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def tear_down(exc):
    """Removes the current sqlalchemy session"""
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
