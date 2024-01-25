from unittest.mock import Mock, patch
from sqlalchemy.exc import SQLAlchemyError

import pytest

from app import *


# Define a fixture for the session
@pytest.fixture
def mock_session():
    session = Mock()
    session.add = Mock()
    session.commit = Mock()
    session.rollback = Mock()
    return session


# Test to see if the function runs without throwing errors
def test_add_book_no_errors(mock_session):
    title = "The Great Gatsby"
    author = "F. Scott Fitzgerald"
    response = add_book(mock_session, title, author)
    assert response is not None


# Test to see if a book is added successfully
def test_add_book_added_success(mock_session):
    title = "1984"
    author = "George Orwell"
    add_book(mock_session, title, author)
    # Verify that session.add was called with a book instance and commit was called
    assert mock_session.add.called
    assert mock_session.commit.called


# Test to see if function handles exceptions by rolling back
def test_add_book_rollback_on_error(mock_session):
    mock_session.add.side_effect = SQLAlchemyError
    title = "1984"
    author = "George Orwell"

    # Execute add_book with a session that raises an SQLAlchemyError when `add` is called
    response = add_book(mock_session, title, author)
    mock_session.rollback.assert_called_once()
    assert response is None


# Test to see if function returns None when there is a SQLAlchemyError
def test_add_book_return_none_on_error(mock_session):
    mock_session.add.side_effect = SQLAlchemyError
    title = "1984"
    author = "George Orwell"

    # Execute add_book with a session that raises an SQLAlchemyError when `add` is called
    result = add_book(mock_session, title, author)
    assert result is None
