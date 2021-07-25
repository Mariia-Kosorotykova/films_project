"""This module implements resources for Director"""

from flask import jsonify
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
        db.session.delete(current_director)
        db.session.commit()
        return jsonify({
            "Msg": 200,
            "Error msg": "Director NOT FOUND"
        })
