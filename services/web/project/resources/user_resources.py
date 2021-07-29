"""This module implements resources for User"""


from flask import request
from flask_restx import Resource, fields
from marshmallow import ValidationError

from ..models.user import User
from ..schemas import UserSchema
from .. import db, api

user_schema = UserSchema()

user_fields = api.model(
    "User",
    {
        "last_name": fields.String,
        "login": fields.String,
        "first_name": fields.String,
        "email": fields.String,
        "is_admin": fields.String("False"),
        "password": fields.String,
    },
)

class UserListResource(Resource):
    """This class describes resource for User"""

    @staticmethod
    def get():
        """This method retrieves all users"""
        users = User.query.all()

        return user_schema.dump(users, many=True), 200

    @staticmethod
    @api.expect(user_fields)
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
