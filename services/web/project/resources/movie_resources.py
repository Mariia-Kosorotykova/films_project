"""This module implements resources for Movie"""

from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError
from flask_login import login_required, current_user

from ..models.movie import Movie
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
        new_movie = request.get_json()
        try:
            new_movie_data = movie_schema.load(new_movie, session=db.session)
        except ValidationError as er:
            return {"Error message": str(er)}, 400

        db.session.add(new_movie_data)
        db.session.commit()

        return movie_schema.dump(new_movie_data), 201


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
