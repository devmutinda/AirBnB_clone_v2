#!/usr/bin/python3
"""
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_default():
    """Displays HTML page"""
    from models import storage
    from models.state import State
    from models.amenity import Amenity
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def tear_down(exc):
    """Removes the current sqlalchemy session"""
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
