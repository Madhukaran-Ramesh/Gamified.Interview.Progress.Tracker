from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'gamified_interview.db')
DB_URL = f'sqlite:///{DB_PATH}'

def get_engine():
    return create_engine(DB_URL, connect_args={"check_same_thread": False})

def create_db():
    engine = get_engine()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == "__main__":
    create_db()
