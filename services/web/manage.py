"""This module allows to manage the app from the command line"""


from flask.cli import FlaskGroup
from project import app, db

from filling import fill_user, fill_movie, fill_director,\
                    fill_movie_director, fill_genre_type, fill_movie_genre

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    """This method creates database"""
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    """This method fills tables"""
    fill_user()
    fill_movie()
    fill_director()
    fill_movie_director()
    fill_genre_type()
    fill_movie_genre()

    db.session.commit()

if __name__ == '__main__':
    cli()
