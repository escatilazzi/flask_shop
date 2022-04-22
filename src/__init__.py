   
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# from config import Config

app = Flask(__name__)


#Load configuration
# app.config.from_object(Config)
from werkzeug.utils import import_string
cfg = import_string('config.DevConfig')()
app.config.from_object(cfg)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from src import routes, models

