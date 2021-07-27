"""This module implements relationship between Movie and Director."""


from .. import db

class MovieDirector(db.Model):
    """This class describes MovieGenre model"""
    __tablename__ = "movie_director"

    movie_director_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))
    director_id = db.Column(db.Integer, db.ForeignKey("director.director_id"))

    def __init__(self, movie_id, director_id):
        self.movie_id = movie_id
        self.director_id = director_id