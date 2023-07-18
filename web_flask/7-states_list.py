#!/usr/bin/python3
"""This is my documentation maybe you need a longer comment """
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)
    

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
