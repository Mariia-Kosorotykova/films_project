"""This module implements resources for Movie"""

from flask import request
from flask_restx import Resource
from marshmallow import ValidationError

from ..models.movie import Movie
from ..schemas import MovieSchema
from .. import db

movie_schema = MovieSchema()

class MovieListResource(Resource):
    """This class describes list resource for Movie"""
    @staticmethod
    def get():
        """This method retrieves all movies"""
        movies = Movie.query.all()
        return movie_schema.dump(movies), 200

    @staticmethod
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
            movie_schema.dump(movie), 200

        return {"Error message": "Film not found"}, 404

    @staticmethod
    def put(movie_id):
        """This method updates movie"""
        current_movie = Movie.query.get_or_404(movie_id)
        current_movie_json = request.get_json()
        if current_movie:
            current_movie.user_id = current_movie_json["user_id"]
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
