#!/usr/bin/env python3
"""simple flask route module"""
from flask import Flask, render_template


app = Flask(__name__)


# simple route "/"
@app.route('/')
def home() -> str:
    """simple route to return string"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
