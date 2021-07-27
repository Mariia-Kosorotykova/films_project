"""This module implements relationship between Movie and Genre_type."""


from .. import db

class MovieGenre(db.Model):
    """This class describes MovieGenre model"""
    __tablename__ = "movie_genre"

    movie_genre_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))
    genre_type_id = db.Column(db.Integer, db.ForeignKey("genre_type.genre_type_id"))

    def __init__(self, movie_id, genre_type_id):
        self.movie_id = movie_id
        self.genre_type_id = genre_type_id
