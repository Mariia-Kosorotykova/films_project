"""This module implements GenreType model."""

from .. import db

class GenreType(db.Model):
    """This class describes Genre_type model"""
    __tablename__ = "genre_type"

    genre_type_id = db.Column(db.Integer, primary_key=True)
    genre_title = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, genre_title):
        self.genre_title = genre_title

    @classmethod
    def search_by_title(cls, genre_title):
        """This method finds genre by name"""
        return GenreType.query.filter(GenreType.genre_title == genre_title).first()

    @classmethod
    def get_or_create(cls, genre_title):
        """This method gets or creates genre"""
        current_genre = GenreType.search_by_title(genre_title)
        if not current_genre:
            current_genre = GenreType(genre_title=genre_title)
            db.session.add(current_genre)
            db.session.commit()
        return current_genre
