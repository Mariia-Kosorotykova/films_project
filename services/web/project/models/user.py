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

    def __init__(self, login, password, first_name, last_name, email, is_admin):
        self.login = login
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    def __repr__(self):
        return '<User: login = {login}' \
               'first_name = {first_name}, '\
               'last_name = {last_name}, '\
               'email = {email}>'.format(login=self.login,
                                         first_name=self.first_name,
                                         last_name=self.last_name,
                                         email=self.email)

    def repr_to_json(self):
        """Representation to JSON"""
        return {
            'login': self.login,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

    def get_id(self):
        """This method returns user's id"""
        return self.user_id
