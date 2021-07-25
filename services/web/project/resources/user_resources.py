"""This module implements resources for User"""

from flask import request
from flask_restx import Resource
from marshmallow import ValidationError

from ..schemas import UserSchema
from .. import db

user_schema = UserSchema()


class UserListResource(Resource):
    """This class describes resource for User"""

    @staticmethod
    def post():
        """This method adds new user"""
        try:
            new_user = user_schema.load(request.json, session=db.session)
        except ValidationError as er:
            return {"Error message": str(er)}, 401

        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
