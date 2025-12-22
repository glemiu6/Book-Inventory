from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager
DB_URL='postgresql+psycopg://postgres:@localhost:5432/DW'
engine = create_engine(DB_URL,echo=True)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()

@contextmanager
def get_connection():
    """
    Makes the database connection
    Ensures that the database connection is closed after use
    """
    session=SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


def init_db():
    """
    Initialize the database schema
    Creates all the tables defined in SQLAlchemy models
    """
    Base.metadata.create_all(bind=engine)
