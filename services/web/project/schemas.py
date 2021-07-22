"""This module represents schemas"""


from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models.director import Director
from .models.genre_type import GenreType
from .models.movie import Movie
from .models.user import User


class DirectorSchema(SQLAlchemyAutoSchema):
    """This schema implements Director model"""
    class Meta:
        """Describes marshmallow schema"""
        fields = ("first_name", "last_name",)
        model = Director
        load_instance = True

class GenreTypeSchema(SQLAlchemyAutoSchema):
    """This schema implements GenreType model"""
    class Meta:
        """Describes marshmallow schema"""
        fields = ["genre_title"]
        model = GenreType
        load_instance = True

class MovieSchema(SQLAlchemyAutoSchema):
    """This schema implements Movie model"""
    class Meta:
        """Describes marshmallow schema"""
        fields = ("user_id", "movie_title", "release_date",
                  "description", "rating", "poster",)
        model = Movie
        load_instance = True
        include_fk = True

class UserSchema(SQLAlchemyAutoSchema):
    """This schema implements User model"""
    class Meta:
        """Describes marshmallow schema"""
        fields = ("login", "password", "first_name", "last_name", "email", "is_admin",)
        model = User
        load_instance = True
