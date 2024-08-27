#!/usr/bin/env python3
"""module to insantiate babel object"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """class to configure available languages"""
    LANGUAGES = ['en', 'fr']

    # configure babels default locale
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def home() -> str:
    """return babel object locale"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
