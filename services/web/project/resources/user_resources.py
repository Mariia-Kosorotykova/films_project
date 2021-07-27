"""This module implements resources for User"""

from flask import request
from flask_restx import Resource
from marshmallow import ValidationError

from ..models.user import User
from ..schemas import UserSchema
from .. import db

user_schema = UserSchema()

class UserListResource(Resource):
    """This class describes resource for User"""

    @staticmethod
    def get():
        """This method retrieves all users"""
        users = User.query.all()

        return user_schema.dump(users), 200

    @staticmethod
    def post():
        """This method adds new user"""
        new_user = request.get_json()
        try:
            new_user_data = user_schema.load(new_user, session=db.session)
        except ValidationError as er:
            return {"Error message": str(er)}, 400

        db.session.add(new_user_data)
        db.session.commit()

        return user_schema.dump(new_user_data), 201
