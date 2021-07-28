"""This module create Flask application."""

import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import config
from flask_restx import Api

app = Flask(__name__)
app.secret_key = "qwerty"
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)

@app.route('/')
def hello_world():
    """This method returns text 'Hello World!'"""
    return 'Hello World!'

from .models import director, genre_type, movie, movie_director, movie_genre, user
from . import routes
from . import login
from .resources import login_logout
