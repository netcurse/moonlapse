from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.models import Base

DATABASE_URL = "sqlite:///game.db"

def init_engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return engine

def get_session_factory(engine):
    SessionFactory = sessionmaker(bind=engine)
    return SessionFactory
