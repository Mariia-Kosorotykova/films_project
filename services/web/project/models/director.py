"""This module presents Director model."""

from .. import db


class Director(db.Model):
    """This class describes Director model"""
    __tablename__ = "director"

    director_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<Director: first_name = {first_name}, ' \
               'last_name = {last_name}>'.format(first_name=self.first_name,
                                                 last_name=self.last_name)

    def repr_to_json(self):
        """Representation to JSON"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name
        }
