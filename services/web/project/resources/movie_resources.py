"""This module implements resources for Movie"""

from flask import request, jsonify
from flask_restx import Resource
from marshmallow import ValidationError

from ..models.movie import Movie
# from ..models.director import Director
# from ..models.genre_type import GenreType
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
        movie = Movie.query.get(movie_id)
        if movie:
            movie_schema.dump(movie), 200

        return {"Error message": "Film not found"}, 404

    @staticmethod
    def patch(movie_id):
        pass


    @staticmethod
    def delete(movie_id):
        """This method deletes current movie"""
        current_director = Movie.query.get_or_404(movie_id)
        db.session.delete(current_director)
        db.session.commit()
        return jsonify({
            "Msg": 200,
            "Error msg": "Director NOT FOUND"
        })
