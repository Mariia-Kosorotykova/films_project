"""This module implements User model."""


from .. import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    """This class describes User model"""
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True)
    is_admin = db.Column(db.Boolean(), nullable=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User: login = {login}' \
               'first_name = {first_name}, ' \
               'last_name = {last_name}, ' \
               'email = {email}>'.format(login=self.login,
                                         first_name=self.first_name,
                                         last_name=self.last_name,
                                         email=self.email)

    def get_id(self):
        """This method returns user's id"""
        return self.user_id
