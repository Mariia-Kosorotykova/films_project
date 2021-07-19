"""This module implements relationship between Movie and Genre_type."""


from .. import db

MovieGenre = db.Table(
    "movie_genre",

    db.Column(
        "movie_id", db.Integer, db.ForeignKey("movie.movie_id"), nullable=False
    ),
    db.Column(
        "genre_type_id", db.Integer, db.ForeignKey("genre_type.genre_type_id"), nullable=False
    )
)
