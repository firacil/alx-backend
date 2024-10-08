#!/usr/bin/env python3
"""module to insantiate babel object"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config(object):
    """class to configure available languages"""
    LANGUAGES = ['en', 'fr']

    # configure babels default locale
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """return the bestmatch clients preferred langs
    and supported one
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home() -> str:
    """return babel object locale"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
