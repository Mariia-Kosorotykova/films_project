"""This module implements GenreType model."""

from .. import db

class GenreType(db.Model):
    """This class describes Genre_type model"""
    __tablename__ = "genre_type"

    genre_type_id = db.Column(db.Integer, primary_key=True)
    genre_title = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, genre_title):
        self.genre_title = genre_title
