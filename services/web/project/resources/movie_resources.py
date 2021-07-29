"""This module implements resources for Movie"""

from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from flask_login import login_required, current_user

from ..models.movie import Movie
from ..models.user import User
from ..models.director import Director
from ..models.genre_type import GenreType

from ..schemas import MovieSchema
from .. import db, api

movie_schema = MovieSchema()

movie_fields = api.model(
    "Movie",
    {
        # "user_id": fields.Integer,
        "movie_title": fields.String,
        "release_date": fields.Date,
        "description": fields.String,
        "rating": fields.Integer(min=0, max=10),
        "poster": fields.String,
        "movie_directors": fields.List(fields.String),
        "movie_genres": fields.List(fields.String),
    },
)

class MovieListResource(Resource):
    """This class describes list resource for Movie"""

    @staticmethod
    def get():
        """This method retrieves all movies"""
        movies = Movie.query.all()
        return movie_schema.dump(movies, many=True), 200

    @staticmethod
    @api.expect(movie_fields)
    def post():
        """This method adds new movie"""
        if current_user.is_authenticated:
            movie_data = request.json
            movie = Movie()

            movie.user_id = current_user.get_id()
            movie.movie_title = movie_data["movie_title"]
            movie.release_date = movie_data["release_date"]
            movie.description = movie_data["description"]
            movie.rating = movie_data["rating"]
            movie.poster = movie_data["poster"]

            for current_director in movie_data["movie_directors"]:
                movie.movie_directors.append(Director.get_or_create(current_director))

            for current_genre in movie_data["movie_genres"]:
                movie.movie_genres.append(GenreType.get_or_create(current_genre))

            try:
                db.session.add(movie)
                db.session.commit()
            except ValidationError as er:
                return {"Error message": str(er)}, 400

            return movie_schema.dump(movie), 201
        return {"Error message": "User isn't authenticated"}, 401

class MovieResource(Resource):
    """This class describes resource for Movie"""
    @staticmethod
    def get(movie_id):
        """This method get movie by id"""
        movie = Movie.query.get_or_404(movie_id)
        if movie:
            return movie_schema.dump(movie), 200

        return {"Error message": "Film not found"}, 404

    @staticmethod
    @api.expect(movie_fields)
    def put(movie_id, validate=True):
        """This method updates movie"""
        current_movie = Movie.query.get_or_404(movie_id)
        current_movie_json = request.get_json()
        if current_movie:
            current_movie.movie_title = current_movie_json["movie_title"]
            current_movie.release_date = current_movie_json["release_date"]
            current_movie.description = current_movie_json["description"]
            current_movie.rating = current_movie_json["rating"]
            current_movie.poster = current_movie_json["poster"]
        else:
            current_movie = movie_schema.load(current_movie_json, session=db.session)
        db.session.add(current_movie)
        db.session.commit()

        return movie_schema.dump(current_movie), 200

    @staticmethod
    def delete(movie_id):
        """This method deletes current movie"""
        current_movie = Movie.query.get_or_404(movie_id)
        if current_movie:
            db.session.delete(current_movie)
            db.session.commit()
            return {"Message": "Deleted successfully"}, 200
        return {"Error message": "Film not found"}, 404
