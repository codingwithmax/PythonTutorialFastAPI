from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from app.config import Config

Base = declarative_base()
config = Config()

engine = create_engine(config.host)


def recreate_tables(engine: Engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
