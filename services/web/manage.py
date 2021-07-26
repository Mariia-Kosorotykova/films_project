"""This module allows to manage the app from the command line"""


from flask.cli import FlaskGroup
from project import app, db
# from .project import routes

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    """This method creates database"""
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()
