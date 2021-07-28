"""This module implements fill in tables"""


from project.models.user import User
from project.models.movie import Movie
from project.models.director import Director
from project.models.movie_director import MovieDirector
from project.models.genre_type import GenreType
from project.models.movie_genre import MovieGenre

from project import db


def fill_user():
    """This method fills User"""
    db.session.add(User(login="kate1996", password="Apples11",
                        first_name="Kate", last_name="Deway",
                        email="kate_deway@gmail.com", is_admin=True))
    db.session.add(User(login="MikeDennis", password="Yello_Bee!",
                        first_name="Michael", last_name="Dennis",
                        email="michael_d@gmail.com", is_admin=False))
    db.session.add(User(login="vero_nica75", password="longpass1",
                        first_name="Veronica", last_name="Royston",
                        email="v_royston75@mail.ru", is_admin=True))

    db.session.commit()

def fill_genre_type():
    """This method fills GenreType"""
    db.session.add(GenreType(genre_title="Adventure"))
    db.session.add(GenreType(genre_title="Drama"))
    db.session.add(GenreType(genre_title="History"))

    db.session.commit()

def fill_director():
    """This method fills Director"""
    db.session.add(Director(first_name="Rob", last_name="Minkoff"))
    db.session.add(Director(first_name="Steven", last_name="Spielberg"))
    db.session.add(Director(first_name="David", last_name="Fincher"))

    db.session.commit()

def fill_movie():
    """This method fills Movie"""
    db.session.add(Movie(user_id=3, movie_title="Schindler's list",
                         release_date="2019-01-24", description="Top movie",
                         rating=9, poster="http://movie_link"))
    db.session.add(Movie(user_id=3, movie_title="Fight Club",
                         release_date="1999-10-15", description="Top movie",
                         rating=8, poster="http://movie_link"))
    db.session.add(Movie(user_id=2, movie_title="The Lion King",
                         release_date="1994-06-12", description="Top movie",
                         rating=7, poster="http://movie_link"))

    db.session.commit()

def fill_movie_director():
    """This method fills MovieDirector"""
    db.session.add(MovieDirector(movie_id=1, director_id=2))
    db.session.add(MovieDirector(movie_id=2, director_id=3))
    db.session.add(MovieDirector(movie_id=3, director_id=1))

    db.session.commit()


def fill_movie_genre():
    """This method fills MovieGenre"""
    db.session.add(MovieGenre(movie_id=1, genre_type_id=3))
    db.session.add(MovieGenre(movie_id=2, genre_type_id=2))
    db.session.add(MovieGenre(movie_id=3, genre_type_id=1))

    db.session.commit()
