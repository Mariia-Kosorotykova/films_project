"""This module create Flask application."""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class User(db.Model):
    """This class describes User model"""
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True)
    is_admin = db.Column(db.Boolean(), nullable=False)

    def __init__(self, *args):
        self.login, self.password, self.first_name, self.last_name,\
            self.email, self.is_admin = args

class GenreType(db.Model):
    """This class describes Genre_type model"""
    __tablename__ = "genre_type"

    genre_type_id = db.Column(db.Integer, primary_key=True)
    genre_title = db.Column(db.String(50), nullable=False)

    def __init__(self, genre_title):
        self.genre_title = genre_title

# This table implements relationship between Movie and Genre_type
MovieGenre = db.Table(
    "movie_genre",

    db.Column(
        "movie_id", db.Integer, db.ForeignKey("movie.movie_id"), nullable=False
    ),
    db.Column(
        "genre_type_id", db.Integer, db.ForeignKey("genre_type.genre_type_id"), nullable=False
    )
)

class Director(db.Model):
    """This class describes Director model"""
    __tablename__ = "director"

    director_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, *args):
        self.first_name, self.last_name = args

# This table implements relationship between Movie and Director
MovieDirector = db.Table(
    "movie_director",

    db.Column(
        "movie_id", db.Integer, db.ForeignKey("movie.movie_id"), nullable=False
    ),
    db.Column(
        "director_id", db.Integer, db.ForeignKey("director.director_id")
    )
)

class Movie(db.Model):
    """This class describes Movie model"""
    __tablename__ = "movie"

    movie_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.user_id"), nullable=False
    )
    user = db.relationship("User", backref="user", lazy=True)
    movie_title = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)
    rating = db.Column(db.Numeric(3, 1))
    poster = db.Column(db.Text, nullable=False)
    director = db.relationship(
        "Director", secondary=MovieDirector, backref="movie_director"
    )
    genre_type = db.relationship(
        "GenreType", secondary=MovieGenre, backref="movie_genre"
    )

    def __init__(self, *args):
        self.user_id, self.movie_title, self.release_date,\
            self.description, self.rating, self.poster = args

@app.route('/')
def hello_world():
    return jsonify(hello='world')
