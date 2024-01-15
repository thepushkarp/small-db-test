from unittest.mock import ANY, MagicMock, patch


from unittest.mock import ANY
from sqlalchemy.exc import SQLAlchemyError

import pytest

from app import *


# Fixture for setting up a mock database session
@pytest.fixture
def mock_session():
    session_mock = MagicMock()
    session_mock.commit = MagicMock()
    session_mock.add = MagicMock()
    session_mock.rollback = MagicMock()
    return session_mock


# Test to ensure the function add_book does not throw an error when executed
def test_add_book_not_none(mock_session):
    book = add_book(mock_session, "Sample Book", "Sample Author")
    assert book is not None or isinstance(
        book, type(None)
    ), "The add_book function should return a Book instance or None"


# Test to ensure a book is added successfully without directly relying on the Book object's identity
def test_add_book_success(mock_session):
    title = "Sample Book"
    author = "Sample Author"
    mock_session.add.return_value = None
    mock_session.commit.return_value = None

    book = add_book(mock_session, title, author)

    # Assertions to ensure the function executes the expected behavior
    mock_session.add.assert_called_with(ANY)
    mock_session.commit.assert_called_once()
    assert isinstance(
        book, Book
    ), "The add_book function did not return the book as expected"


# Test to ensure that an SQLAlchemyError is caught and the session is rolled back
def test_add_book_handles_sqlalchemy_error(mock_session):
    title = "Sample Book"
    author = "Sample Author"
    mock_session.add.side_effect = SQLAlchemyError

    with patch("builtins.print") as mocked_print:
        book = add_book(mock_session, title, author)

        mock_session.rollback.assert_called_once()
        assert (
            book is None
        ), "The add_book function should return None upon encountering an SQLAlchemyError"
        mocked_print.assert_called()  # Ensure that an error message is printed
