from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
import os

login_manager = LoginManager()
migrate = Migrate()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')
    #Database
    # init_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)
    login_manager.init_app(app)

    from src.public.routes import public_bp
    app.register_blueprint(public_bp)
    from src.account.routes import account_bp
    app.register_blueprint(account_bp)
    from src.admin.routes import admin_bp
    app.register_blueprint(admin_bp)

    return app

