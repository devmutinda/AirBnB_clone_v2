#!/usr/bin/python3
"""
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_default():
    """Displays HTML page"""
    from models import storage
    from models.state import State
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Displays a HTML page"""
    from models import storage
    from models.state import State
    states = storage.all(State)
    if id:
        id = "State.{}".format(id)
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def tear_down(exc):
    """Removes the current sqlalchemy session"""
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
