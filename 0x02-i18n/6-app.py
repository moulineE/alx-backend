#!/usr/bin/env python3
"""a basic Flask app"""
from flask import (Flask, render_template, request, g)
from flask_babel import Babel
from typing import Dict, Union


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
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    user = g.get('user')
    if user and user['locale'] in Config.LANGUAGES:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id: int) -> Union[Dict, None]:
    """
    returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed
    """
    if id and id in users.keys():
        return users[id]
    return None


@app.before_request
def before_request() -> None:
    """
    use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    setattr(g, 'user', get_user(int(request.args.get('login_as', 0))))


@app.route('/')
def hello_world():
    """render 5-index.html"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
