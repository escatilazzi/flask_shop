from turtle import back
from src import login_manager , db, create_app
from sqlalchemy.orm import relationship, backref
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user
from flask_user import UserManager

@login_manager.user_loader
def load_user(usr_id):
    return User.query.get(int(usr_id))

class User(UserMixin,db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(256), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    roles = db.relationship("Role", secondary="user_roles", viewonly=True)
    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        boolPasswordCheck = check_password_hash(self.password_hash, password)
        return boolPasswordCheck


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)

    user = relationship("User", secondary="user_roles", viewonly=True)
    
    def __repr__(self):
        return '<Role {}>'.format(self.name)

class UserRoles(db.Model):
    __tablename__='user_roles'
    role_id=db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)

    role= db.relationship('Role', backref=backref('user_roles', cascade="all, delete-orphan"))
    user= db.relationship('User', backref=backref('user_roles', cascade="all, delete-orphan"))
