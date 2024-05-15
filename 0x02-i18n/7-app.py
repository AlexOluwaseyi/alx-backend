#!/usr/bin/env python3

"""
Flask module for i18n and probably L10n
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    """Configuration class for languages availble for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """
    returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Run before requests"""
    g.user = get_user()


@babel.localeselector  # Line needs to be commented to run successfully
def get_locale():
    """Get locale from request header """
    user_locale = request.args.get('locale')
    if user_locale:
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    if g.user:
        if g.user['locale'] in app.config['LANGUAGES']:
            return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector  # Line needs to be commented to run successfully
def get_timezone():
    """Get locale from request header """
    timezone_query = request.args.get('timezone')
    if timezone_query:
        try:
            pytz.timezone(timezone_query)
            return timezone_query
        except pytz.UnknownTimeZoneError:
            pass

    # Check if there is a logged-in user and use their timezone if valid
    if g.get('user') and g.user.get('timezone'):
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


# babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/", strict_slashes=False)
def index():
    """Render index.html template
    """
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
