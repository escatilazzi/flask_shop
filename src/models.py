from src.database import Base
from src import login_manager
from sqlalchemy import Column, Integer,Text, String, DateTime
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(usr_id):
    return User.query.get(int(usr_id))

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    username = Column(String(256), unique=True, index=True)
    password_hash = Column(String(128))
    created = Column(DateTime, default=datetime.utcnow(), nullable=False)

    # def __init__(self, username, email, password):
    #     self.username = username
    #     self.email = email
    #     self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
