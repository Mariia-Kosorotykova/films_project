"""This module implements relationship between Movie and Director."""


from .. import db

MovieDirector = db.Table(
    "movie_director",

    db.Column(
        "movie_id", db.Integer, db.ForeignKey("movie.movie_id"), nullable=False
    ),
    db.Column(
        "director_id", db.Integer, db.ForeignKey("director.director_id")
    )
)
