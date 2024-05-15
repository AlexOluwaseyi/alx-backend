#!/usr/bin/env python3

"""
Flask module for i18n and probably L10n
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Render index.html template
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)