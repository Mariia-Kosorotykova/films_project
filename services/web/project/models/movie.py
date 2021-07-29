"""This module presents Movie model."""


from .. import db
from .movie_director import MovieDirector
from .movie_genre import MovieGenre

class Movie(db.Model):
    """This class describes Movie model"""
    __tablename__ = "movie"

    movie_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.user_id"), nullable=False
    )
    user = db.relationship("User", backref="user", lazy=True)
    movie_title = db.Column(db.String(50), nullable=False)
    release_date = db.Column(db.Date)
    description = db.Column(db.Text)
    rating = db.Column(db.Integer)
    poster = db.Column(db.Text, nullable=False)

    movie_directors = db.relationship('Director', secondary='movie_director')

    movie_genres = db.relationship("GenreType", secondary='movie_genre')

    # def __init__(self, user_id, movie_title, release_date, description, rating, poster):
    #     self.user_id = user_id
    #     self.movie_title = movie_title
    #     self.release_date = release_date
    #     self.description = description
    #     self.rating = rating
    #     self.poster = poster

    def __repr__(self):
        return '<Movie: movie_title = {movie_title}' \
               'release_date = {release_date}, '\
               'description = {description}, ' \
               'rating = {rating}, ' \
               'poster = {poster}>'.format(movie_title=self.movie_title,
                                         release_date=self.release_date,
                                         description=self.description,
                                         rating=self.rating,
                                         poster=self.poster)

    # def repr_to_json(self):
    #     """Representation to JSON"""
    #     return {
    #         'movie_title': self.movie_title,
    #         'release_date': self.release_date,
    #         'description': self.description,
    #         'rating': self.rating,
    #         'poster': self.poster
    #     }
