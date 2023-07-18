#!/usr/bin/python3
"""This is my documentation maybe you need a longer comment"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """This for tearing down, not up"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """This is for the states"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states.values())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
