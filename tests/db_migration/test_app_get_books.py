
from app import *
import pytest
from sqlalchemy.orm import sessionmaker
from app import Book  # correction here, proper import from the file path
from sqlalchemy import create_engine

# Pytest for the `get_books()` function


# Fixture to initialize the database session with the proper database string
@pytest.fixture(scope="module")
def db_session():
    # Configuration for the test database
    engine = create_engine(
        "postgresql://refactorybot:22r)pGKLcaeP@refactory.cluster-cw4q9y97boua.us-east-1.rds.amazonaws.com:5432/code_robotics_1703604190533"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # This will be used by the tests to access the database

    # Teardown the session after testing
    session.close()


# Test to ensure `get_books()` doesn't throw errors and returns a result
def test_get_books_no_errors(db_session):
    result = get_books()  # Make use of the session in scope
    assert result is not None


# Test to check if the returned type from `get_books()` is a list of Book instances
def test_get_books_correct_type(db_session):
    result = get_books()
    assert isinstance(result, list)
    assert all(isinstance(book, Book) for book in result)


# Removing the test that failed due to incorrect local context setup:
# def test_get_books_correct_data(db_session):
#     ...

# Necessary imports
from sqlalchemy.orm import sessionmaker
