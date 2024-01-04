#from sqlalchemy.orm import Session, sessionmaker
#import pytest
#from sqlalchemy import create_engine
#from app import *
#
#
#from sqlalchemy import create_engine
#
## Given database connection string
#DATABASE_URL = "postgresql://postgres:root@localhost:5432/code_robotics_1703746812331"
#
## Creating a new engine
#engine = create_engine(DATABASE_URL)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
#@pytest.fixture(scope="module")
#def db_session() -> Session:
#    """Create a new database session for a test."""
#    session = SessionLocal()
#    yield session
#    session.close()
#
#
#def test_get_books_exists(db_session):
#    assert get_books(db_session) is not None
#
#
#def test_get_books_return_type(db_session):
#    books = get_books(db_session)
#    assert isinstance(books, list)
#
#
#def test_get_books_item_type(db_session):
#    books = get_books(db_session)
#    # if there is at least one book in the db
#    if books:
#        assert isinstance(books[0], Book)
#