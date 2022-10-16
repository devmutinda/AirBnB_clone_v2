from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exc):
    """Removes the current sqlalchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def html_page():
    """Renders a html template"""
    return render_template('7-states_list.html', states=storage.all('State'))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
