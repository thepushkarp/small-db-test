from unittest.mock import Mock

from app import *
from sqlalchemy.orm import sessionmaker

import pytest

# Tests for add_book function


# The SQLAlchemy session and Book model are assumed to be in scope from the provided
# source code.

# We do not import the existing Book model and session.
# Instead, we will create mock objects for them within our tests.

# Assuming the file is named app.py and the folder structure starts from the root
# directory where app.py is located.


@pytest.fixture
def mock_book_class():
    """Fixture to create a mock Book class."""
    with patch("app.Book", autospec=True) as mock_book:
        # We satisfy the autospec requirement by providing a dummy class for the mock to represent
        class DummyBook:
            def __init__(self, title, author):
                self.title = title
                self.author = author

        mock_book.side_effect = DummyBook
        yield mock_book


@pytest.fixture
def mock_session():
    """Fixture to provide a mock session for the add_book function."""
    with patch("app.session") as mock:
        # Mock the commit function to do nothing
        mock.commit = Mock()
        # Mock the add function to accept any arguments
        mock.add = Mock()
        yield mock


def test_add_book_runs_without_errors(mock_session, mock_book_class):
    """Test that the 'add_book' function runs without throwing errors."""
    title = "Sample Book"
    author = "Jane Doe"
    # We are only checking that the function can run without errors
    assert add_book(title, author) is not None


def test_add_book_correctly_creates_book_instance(mock_session, mock_book_class):
    """Test if 'add_book' correctly creates an instance of 'Book' class."""
    title = "Sample Book"
    author = "Jane Doe"
    add_book(title, author)
    mock_book_class.assert_called_once_with(title=title, author=author)


def test_add_book_correctly_adds_book_to_session(mock_session, mock_book_class):
    """Test if 'add_book' correctly adds a new book to the session."""
    title = "Sample Book"
    author = "Jane Doe"
    add_book(title, author)
    mock_session.add.assert_called_once()


def test_add_book_commits_to_session(mock_session, mock_book_class):
    """Test if after adding, 'add_book' commits the new book to the session."""
    title = "Sample Book"
    author = "Jane Doe"
    add_book(title, author)
    mock_session.commit.assert_called_once()


def test_add_book_return_value(mock_session, mock_book_class):
    """Test the return value of 'add_book'"""
    title = "Sample Book"
    author = "Jane Doe"
    result = add_book(title, author)
    expected_result = f"Book '{title}' by {author} added!"
    assert result == expected_result


# Insert at the end of the response
from unittest.mock import patch
