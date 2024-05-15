#!/usr/bin/env python3

"""
Flask module for i18n and probably L10n
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


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


def get_user():
    """
    returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed.
    """
    logged_id = request.get('login_as')
    if logged_id:
        return users.get(int(logged_id))
    return None


@app.before_request
def before_request():
    pass


def get_locale():
    """Get locale from request header """
    user_locale = request.args.get('locale')
    if user_locale:
        if user_locale in app.config['LANGUAGES']:
            print(user_locale)
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index():
    """Render index.html template
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
