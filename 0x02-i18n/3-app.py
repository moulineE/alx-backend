#!/usr/bin/env python3
"""a basic Flask app"""
from flask import (Flask, render_template, request)
from flask_babel import Babel


class Config:
    """config for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """render 3-index.html"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
