"""This module implements resources for Movie"""

from flask import request, current_app, jsonify
from flask_restx import Resource, fields
from marshmallow import ValidationError
from flask_login import login_required, current_user
from flask_restx.reqparse import RequestParser

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
        "movie_title": fields.String,
        "release_date": fields.Date,
        "description": fields.String,
        "rating": fields.Integer(min=0, max=10),
        "poster": fields.String,
        "movie_directors": fields.List(fields.String),
        "movie_genres": fields.List(fields.String),
    },
)

parser = RequestParser()
parser.add_argument("Match search", type=str,
                    required=False, help="Enter part of movie name")
parser.add_argument("Genre filter", type=str,
                    required=False, help="Enter genre for desire movie")
parser.add_argument("Filter year FROM", type=str,
                    required=False, help="Enter start year")
parser.add_argument("Filter year TO", type=str,
                    required=False, help="Enter end year")
parser.add_argument("Director filter", type=str,
                    required=False, help="Enter director name for desire movie")

options = ("Rating DESC", "Rating ASC", "Release date DESC", "Release date ASC")
parser.add_argument("Order by", choices=options, help="Select field to order by")

class MovieListResource(Resource):
    """This class describes list resource for Movie"""

    @staticmethod
    @api.expect(parser)
    def get():
        """This method retrieves all movies"""
        args_of_parser = parser.parse_args()

        match_search = args_of_parser.get("Match search", "")
        sort_by = args_of_parser.get("Order by", "")
        genre_filter = args_of_parser.get("Genre filter", "")
        year_from = args_of_parser.get("Filter year FROM", "")
        year_to = args_of_parser.get("Filter year TO", "")
        director_fullname = args_of_parser.get("Director filter", "")

        movies = Movie.query.all()

        # Implements search by partial match
        if match_search:
            movies = Movie.query.filter(Movie.movie_title.ilike(f"%{match_search}%")).all()

        # Implements filter by genre
        if genre_filter:
            current_genre = GenreType.query.filter(
                GenreType.genre_title.ilike(f"{genre_filter}")).first()
            if not current_genre:
                return {"Error": "Movie with such genre isn't exist"}, 404
            else:
                movies = Movie.query.join(Movie.movie_genres).filter(
                    GenreType.genre_title.ilike(f"{genre_filter}")
                )

        # Implements filter by release date
        if year_from:
            movies = Movie.query.filter(Movie.release_date >= f"{year_from}-01-01")
        if year_to:
            movies = Movie.query.filter(Movie.release_date <= f"{year_to}-12-31")

        # Implements filter by director name
        if director_fullname:
            movies = Movie.query.join(Movie.movie_directors).filter(
                Director.full_name.ilike(f"%{director_fullname}%"))

        # Implements sorting by options
        if sort_by and sort_by in options:
            if sort_by == "Rating DESC":
                movies = Movie.query.order_by(Movie.rating.desc())
            elif sort_by == "Rating ASC":
                movies = Movie.query.order_by(Movie.rating)
            elif sort_by == "Release date DESC":
                movies = Movie.query.order_by(Movie.release_date.desc())
            elif sort_by == "Release date ASC":
                movies = Movie.query.order_by(Movie.release_date)

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
        return {"Error message": "User is not logged in"}, 401

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
    @login_required
    def put(movie_id, validate=True):
        """This method updates movie"""
        current_movie = Movie.query.get_or_404(movie_id)
        current_movie_json = request.get_json()
        if current_user.user_id == current_movie.user_id or current_user.is_admin:
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
        return {"Error message": "Not enough permissions"}, 403

    @staticmethod
    @login_required
    def delete(movie_id):
        """This method deletes current movie"""
        current_movie = Movie.query.get_or_404(movie_id)
        if current_movie:
            if current_user.user_id == current_movie.user_id or current_user.is_admin:
                db.session.delete(current_movie)
                db.session.commit()
                return {"Message": "Deleted successfully"}, 200
            return {"Error message": "Not enough permissions"}, 403
        return {"Error message": "Film not found"}, 404
