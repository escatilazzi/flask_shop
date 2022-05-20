from flask import Flask
from werkzeug.utils import import_string
from src.database import init_db, db_session
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
import os

login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')
    #Database
    # init_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    init_db()
    #Flask-Login
    login_manager.init_app(app)

    from src.routes import home_bp
    app.register_blueprint(home_bp)
    from src.account.routes import account_bp
    app.register_blueprint(account_bp)

    @app.teardown_appcontext    
    def shutdown_session(exception=None):
        db_session.remove()

    return app

