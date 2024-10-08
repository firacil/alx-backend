#!/usr/bin/env python3
"""module to insantiate babel object"""
from flask import Flask, request, render_template, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns a user dictionary or none if the id can't found
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """summary"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """return the bestmatch clients preferred langs
    and supported one
    """
    # locale from url parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale

    # locale from user settings
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.cofig['LANGUAGES']:
            return locale

    # locale from rquest header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """select and return tz"""

    # find tz parameter in url param
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezoe(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # find time zone from user settings
    if g.user:
        try:
            tzoe = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # default utc
    default_tz = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_tz


@app.route('/')
def home():
    """return babel object locale"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
