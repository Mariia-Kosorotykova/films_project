"""This module represents schemas"""


from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_sqlalchemy.fields import Nested
from .models.director import Director
from .models.genre_type import GenreType
from .models.movie import Movie
from .models.user import User

class DirectorSchema(SQLAlchemyAutoSchema):
    """This schema implements Director model"""
    class Meta:
        """Describes marshmallow schema"""
        fields = ("full_name",)
        model = Director
        load_instance = True

class GenreTypeSchema(SQLAlchemyAutoSchema):
    """This schema implements GenreType model"""
    class Meta:
        """Describes marshmallow schema"""
        fields = ["genre_title"]
        model = GenreType
        load_instance = True

class UserSchema(SQLAlchemyAutoSchema):
    """This schema implements User model"""
    class Meta:
        """Describes marshmallow schema"""
        fields = ("login", "password", "first_name", "last_name", "email", "is_admin",)
        model = User
        load_instance = True

class MovieSchema(SQLAlchemyAutoSchema):
    """This schema implements Movie model"""
    class Meta:
        """Describes marshmallow schema"""
        exclude = ["user_id"]
        model = Movie
        load_instance = True
        include_fk = True
        include_relationships = True

        movie_directors = Nested(DirectorSchema, many=True)
        movie_genres = Nested(GenreTypeSchema, many=True)
        movie_id = auto_field()
        user = Nested(
            UserSchema,
            many=False,
            only=["user_id", "login", "first_name", "last_name", "email"],
        )
