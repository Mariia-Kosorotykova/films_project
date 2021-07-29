"""This module presents Director model."""

from .. import db


class Director(db.Model):
    """This class describes Director model"""
    __tablename__ = "director"

    director_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)

    def __init__(self, full_name):
        self.full_name = full_name

    def __repr__(self):
        return '<Director: full_name = {full_name}>'.format(full_name=self.full_name)

    # def repr_to_json(self):
    #     """Representation to JSON"""
    #     return {
    #         'full_name': self.full_name
    #     }

    @classmethod
    def search_by_full_name(cls, full_name):
        """This method finds genre by name"""
        return Director.query.filter(Director.full_name == full_name).first()

    @classmethod
    def get_or_create(cls, full_name):
        """This method gets or creates genre"""
        current_director = Director.search_by_full_name(full_name)
        if not current_director:
            current_director = Director(full_name=full_name)
            db.session.add(current_director)
            db.session.commit()
        return current_director
