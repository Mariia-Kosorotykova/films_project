"""This module presents Director model."""


from .. import db

class Director(db.Model):
    """This class describes Director model"""
    __tablename__ = "director"

    director_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, *args):
        self.first_name, self.last_name = args
