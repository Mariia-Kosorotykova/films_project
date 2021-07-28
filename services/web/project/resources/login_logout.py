"""This module implements login and logout"""

import logging
from datetime import datetime
from flask import request, jsonify
from flask_login import login_user, logout_user, current_user
from flask_restx import Resource, fields
from .. import db, app, api

from ..models.user import User
from ..login import login_manager

login_manager.init_app(app)

user_fields = api.model(
    "Authorization",
    {
        "login": fields.String,
        "password": fields.String,
    },
)

class LoginResource(Resource):
    """This class describes of login user"""
    @staticmethod
    @api.expect(user_fields)
    def post():
        """Realization of login"""
        user_data = request.get_json()
        password = user_data["password"]
        user = User.query.filter_by(login=user_data['login']).first()

        if user and password == user.password:
            login_user(user)
            db.session.commit()
            # logging.info(f"{datetime.now()} -Successful login")
            return jsonify(
                {"Status": 200, "Message": "Successful login"}
            )
        else:
            return jsonify(
                {"Status": 401, "Message": "Wrong login or password"}
            )


class LogoutResource(Resource):
    """This class describes of logout user"""
    @staticmethod
    def post():
        """Realization of logout"""
        try:
            login = current_user.login
            logout_user()
        # logging.info(f"{datetime.now()} - Successful logout")
            return jsonify(
                {"Status": 200, "Message": "Successful logout"}
            )
        except AttributeError as er:
            return jsonify(
                {"Status": 401, "Error message": "User isn't login yet"}
            )