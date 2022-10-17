#!/usr/bin/python3
"""
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_optional():
    """Displays HTML page"""
    from models import storage
    from models.state import State
    from models.amenity import Amenity
    from models.place import Place
    from models.user import User
    users = storage.all(User)
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('100-hbnb.html', states=states, amenities=amenities,
                           places=places, users=users)


@app.teardown_appcontext
def tear_down(exc):
    """Removes the current sqlalchemy session"""
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
