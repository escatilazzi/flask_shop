import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG= True
    TESTING = True

class DevConfig(Config):
    SECRET_KEY='dev'
    DEBUG= True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'ebuysite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
