#!/usr/bin/python3
"""
This module defines a Flask web application with two routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when accessing the root URL."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when accessing the /hbnb route."""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
