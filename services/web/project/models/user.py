"""This module implements User model."""


from .. import db

class User(db.Model):
    """This class describes User model"""
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True)
    is_admin = db.Column(db.Boolean(), nullable=False)

    def __init__(self, *args):
        self.login, self.password, self.first_name, self.last_name,\
            self.email, self.is_admin = args
