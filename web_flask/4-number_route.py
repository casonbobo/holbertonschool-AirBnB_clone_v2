#!/usr/bin/python3
from flask import Flask
"""This is my documentation"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
