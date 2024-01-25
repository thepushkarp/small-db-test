
from tests.mongo_migration.test_test_app_get_books_mock_books import *
from pymongo.collection import Collection


from unittest.mock import MagicMock, patch
from pytest import fixture
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def mock_books():
    # Create a mock cursor that can iterate over a list of dictionaries
    # These mimic documents in a MongoDB collection
    mock_cursor = MagicMock()
    mock_cursor_return_value = iter(
        [
            {"title": "Book 1", "author": "Author A"},
            {"title": "Book 2", "author": "Author B"},
        ]
    )
    mock_cursor.__iter__.return_value = mock_cursor_return_value

    # Mock MongoDB collection and assign the fake cursor to its find method
    mock_collection = MagicMock(spec=Collection)
    mock_collection.find.return_value = mock_cursor

    # Here we're patching the pymongo.MongoClient to return our mock collection
    with patch("pymongo.MongoClient") as mock_client:
        mock_client().db.collection = mock_collection
        yield mock_collection


def test_mock_books_does_not_raise_error(mock_books):
    # We're only testing that mock_books does not raise an error
    assert mock_books is not None


def test_mock_books_returns_expected_number_of_books(mock_books):
    books = list(mock_books.find())
    assert len(books) == 2


def test_mock_books_returns_cursor_with_dicts(mock_books):
    books = list(mock_books.find())
    assert all(isinstance(book, dict) for book in books)


def test_mock_books_returns_books_with_title_field(mock_books):
    books = list(mock_books.find())
    assert all("title" in book for book in books)

# Import statements required for the test cases
from pymongo.collection import Collection
