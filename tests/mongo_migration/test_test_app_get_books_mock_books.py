
from tests.mongo_migration.test_test_app_get_books_mock_books import *

import pytest


from unittest.mock import MagicMock
from unittest.mock import MagicMock


@pytest.fixture()
def mock_books():
    # A MagicMock with pymongo's collection methods mocked
    mock_book_collection = MagicMock()

    # Setup the behavior of find method to return a list of dictionaries
    # representing books
    mock_book_collection.find.return_value = [
        {"title": "Book 1", "author": "Author A"},
        {"title": "Book 2", "author": "Author B"},
    ]

    return mock_book_collection


def test_mock_books_does_not_raise_error(mock_books):
    try:
        books = list(mock_books.find())
        assert books is not None
    except Exception as ex:
        pytest.fail(f"mock_books.find() raised an exception {ex}")


def test_mock_books_returns_expected_number_of_books(mock_books):
    books = list(mock_books.find())
    assert len(books) == 2


def test_mock_books_returns_cursor_with_dicts(mock_books):
    books = mock_books.find()
    for book in books:
        assert isinstance(book, dict)


def test_mock_books_returns_books_with_title_field(mock_books):
    books = mock_books.find()
    for book in books:
        assert "title" in book
