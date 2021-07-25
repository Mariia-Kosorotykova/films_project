"""This module implements resources for Movie"""

from flask import request, jsonify
from flask_restx import Resource
from marshmallow import ValidationError

from ..models.movie import Movie
from ..models.director import Director
from ..models.genre_type import GenreType
from ..schemas import MovieSchema
from .. import db

movie_schema = MovieSchema()

class MovieListResource(Resource):
    """This class describes list resource for Movie"""
    @staticmethod
    def get():
        """This method displays get method"""
        # movies = Movie.query.all()
        # movie_list = []
        # for movie in movies:
        #     director = Director.query.filter_by(director_id=movie.director_id).first()
        #     if director is None:
        #         director = 'unknown'
        #     else:
        #         director = Movie.director_id
        #     genre_type = []
        #     if movie.genres:
        #         for genre in movie.genres:
        #             genre_type.append(genre.genre_title)
        #     movie_list.append({
        #         'movie_id': movie.movie_id,
        #         'user': movie.user_id,
        #         'movie_title': movie.movie_title,
        #         'release_date': movie.release_date,
        #         'description': movie.description,
        #         'rating': movie.rating,
        #         'director': director,
        #         'genre_type': genre_type
        #     })
        # return jsonify(movie_list)

    @staticmethod
    def post():
        """This method displays post method"""
        data = request.json
        movie = Movie()

        movie.user_id = data["user_id"]
        movie.movie_title = data["movie_title"]
        movie.release_date = data["release_date"]
        movie.description = data["description"]
        movie.rating = data["rating"]
        movie.poster = data["poster"]
        movie.director_id = data["director_id"]
        for genre_id in data["genres"]:
            movie.genres.append(GenreType.query.get_or_404(genre_id))
        try:
            db.session.add(movie)
            db.session.commit()
        except ValidationError as er:
            return {"Error message": str(er)}, 400
        return movie_schema.dump(movie), 201


class MovieResource(Resource):
    """This class describes resource for Movie"""
    @staticmethod
    def get(movie_id):
        """This method get movie by id"""
        movie = Movie.query.get_or_404(movie_id)
        return movie_schema.dump(movie)

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
