#!/usr/bin/python3
"""This is my documentation"""


from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
        return render_template('number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_template(n):
    if n % 2 == 0:
        text = 'even'
    else:
        text = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
