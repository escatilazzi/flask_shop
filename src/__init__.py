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
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'
    #Database
    # init_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)

    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    with app.app_context():
        db.create_all()

    from src.public.routes import public_bp
    app.register_blueprint(public_bp)
    from src.account.routes import account_bp
    app.register_blueprint(account_bp)
    from src.admin.routes import admin_bp
    app.register_blueprint(admin_bp)
    from src.products.routes import product_bp
    app.register_blueprint(product_bp)
    from src.cart.routes import cart_bp
    app.register_blueprint(cart_bp)

    return app

