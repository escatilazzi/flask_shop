import click

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, create_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///dev.db")
#metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

# def init_engine(uri, **kwargs):
#     global engine
#     engine = create_engine(uri, **kwargs)
#     return engine

def init_db():
    import src.models
    Base.metadata.create_all(bind=engine)

