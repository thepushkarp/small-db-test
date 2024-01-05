import pytest

from app import *
from sqlalchemy.orm import Session, sessionmaker


from sqlalchemy import create_engine

# Assuming `create_engine` is defined in the same file as `get_books`
# since there is no 'create_db_engine' function, we need to import create_engine
from sqlalchemy import create_engine

# Pytest code below:


# Setup for database
@pytest.fixture(scope="module")
def db_engine():
    # Using the provided database connection string
    engine = create_engine(
        "postgresql://refactorybot:22r)pGKLcaeP@refactory.cluster-cw4q9y97boua.us-east-1.rds.amazonaws.com:5432/code_robotics_1704453498046"
    )
    return engine


@pytest.fixture(scope="module")
def db_session(db_engine):
    # Assuming that the scoped session is already declared in the main code
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = SessionLocal()
    yield session
    # Session teardown
    session.close()


# Test cases


def test_get_books_without_errors(db_session: Session):
    """
    Test that the get_books function does not throw any errors when called.
    """
    # Test is calling .all() method which requires to be executed in session
    assert (
        get_books(db_session) is not None
    ), "get_books() should return a result, not None."


def test_get_books_returns_list(db_session: Session):
    """
    Test that get_books returns a list.
    """
    books = get_books(db_session)
    assert isinstance(books, list), "get_books() should return a list."


def test_get_books_empty_session(db_session: Session):
    """
    Test get_books on an empty session.
    """
    books = get_books(db_session)
    assert (
        books == []
    ), "get_books() should return an empty list when there are no books."

# Place these imports at the top of your test file.
from sqlalchemy.orm import sessionmaker
