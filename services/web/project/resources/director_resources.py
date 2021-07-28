"""This module implements resources for Director"""


from flask_restx import Resource

from ..models.director import Director
from ..schemas import DirectorSchema
from .. import db

director_schema = DirectorSchema()

class DirectorResource(Resource):
    """This class describes resource for Director"""

    @staticmethod
    def delete(director_id):
        """This method deletes current director"""
        current_director = Director.query.get_or_404(director_id)
        if current_director:
            db.session.delete(current_director)
            db.session.commit()
            return {"Message": "Deleted successfully"}, 200
        return {"Error message": "Director not found"}, 404
