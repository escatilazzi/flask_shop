import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    #UPLOAD_FOLDER = environ.get('UPLOAD_FOLDER')
    UPLOAD_FOLDER = os.path.join('src/static/images')
    
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG= True
    TESTING = True
    # AWS Secrets
    # AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    # AWS_KEY_ID = environ.get('AWS_KEY_ID')

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('PROD_DATABASE_URI')

class Test_Config(Config):
    DEBUG= True
    TESTING = True

