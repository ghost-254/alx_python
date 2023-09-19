#!/usr/bin/python3
"""
This module defines a Flask web application with three routes.
"""

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' when accessing the root URL."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' when accessing the /hbnb route."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C ' followed by the value of the 'text' variable."""
    return "C " + escape(text).replace("_", " ")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
