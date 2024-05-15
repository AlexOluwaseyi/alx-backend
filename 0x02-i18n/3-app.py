#!/usr/bin/env python3

"""
Flask module for i18n and probably L10n
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
    """Configuration class for languages availble for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Get locale from request header """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index():
    """Render index.html template
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)