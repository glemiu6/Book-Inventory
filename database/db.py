import os
from contextlib import contextmanager

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
db_url = os.getenv("DB_URL")
if db_url is None:
    raise ValueError("DB_URL environment variable not set")
engine = create_engine(db_url, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


@contextmanager
def get_connection():
    """
    Makes the database connection
    Ensures that the database connection is closed after use
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def init_db():
    """
    Initialize the database schema
    Creates all the tables defined in SQLAlchemy models
    """
    Base.metadata.create_all(bind=engine)
