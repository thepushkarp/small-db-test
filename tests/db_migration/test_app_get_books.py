from sqlalchemy import create_engine
import pytest

from app import *
from sqlalchemy.orm import sessionmaker

# IMPORTS
# Import the Book class from the correct module / file path
# Since the actual import statement is not provided, a placeholder is used here.
# from app import Book  # Assuming Book is coming from module `app`


# Provide a session fixture that rolls back changes after each test
@pytest.fixture(scope="function")
def session():
    # Setup: connect to the database and create a session
    engine = create_engine(
        "postgresql://postgres:root@host.docker.internal:5432/code_robotics_1704373301739"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Use a transaction for the duration of the test
    connection = engine.connect()
    transaction = connection.begin()
    session.bind = connection

    yield session  # this is where the testing happens

    # Teardown: rollback transaction and close connection/session
    session.close()
    transaction.rollback()
    connection.close()


# A test to ensure the function does not throw an error and doesn't return `None`
def test_get_books_no_errors(session):
    books = get_books()
    assert books is not None


# Edge Case Test 1: Check if the empty table returns an empty list
def test_get_books_empty_table(session):
    assert get_books() == []
