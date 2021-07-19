"""This module create Flask application."""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from . import config

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_world():
    """This method returns text 'Hello World!'"""
    return 'Hello World!'

from .models import director, genre_type, movie, movie_director, movie_genre, user
