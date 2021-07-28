"""This module describes implementation of login manager"""


from flask_login import LoginManager
from .models.user import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    """This method returns JSON with info about user or error"""
    return User.query.get(int(user_id))
