import pytest


import pytest

from app import *
from sqlalchemy import create_engine

# Define the necessary imports for the pytest setup
from sqlalchemy.orm import sessionmaker


# Setting up the test environment
def setup_module(module):
    # Establishing a connection to the test database
    engine = create_engine(
        "postgresql://postgres:root@host.docker.internal:5432/code_robotics_1704369504122"
    )
    Base.metadata.create_all(engine)

    # Creating a new session for the tests
    global session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Preparing a clean state
    session.query(Book).delete()
    session.commit()


# Fixture for creating and returning a sample book
@pytest.fixture()
def sample_book():
    return {"title": "Sample Title", "author": "Sample Author"}


# The first test ensures that the function does not raise an error and it returns a value
def test_add_book_no_error(sample_book):
    try:
        result = add_book(sample_book["title"], sample_book["author"])
        assert result is not None
    except Exception as e:
        pytest.fail(f"An exception occurred: {e}", pytrace=True)


# Test that adding a book will result in that book being retrievable from get_books
def test_add_book_in_get_books(sample_book):
    add_book(sample_book["title"], sample_book["author"])
    books = get_books()
    found_book = any(
        book.title == sample_book["title"] and book.author == sample_book["author"]
        for book in books
    )
    assert found_book, "The book added should be in the list retrieved by get_books"


# A test to ensure the correct string is returned when adding a book
def test_add_book_return_string(sample_book):
    result = add_book(sample_book["title"], sample_book["author"])
    expected_string = f"Book '{sample_book['title']}' by {sample_book['author']} added!"
    assert (
        result == expected_string
    ), "The return string is not matching the expected string"


# Clean up after tests have run
def teardown_module(module):
    session.close()
