#!/usr/bin/env python3
"""simple flask route module"""
from flask import Flask


app = Flask(__name__)


# simple route "/"
@app.route('/')
def home() -> str:
    """siple route to return string"""
    return "Simple route"


if __name__ == "__main__":
    app.run(debug=True)
