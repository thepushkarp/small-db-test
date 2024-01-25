
from tests.mongo_migration.test_test_app_get_books_test_get_books_success import *
from unittest.mock import patch

import pytest
from app import get_books


@pytest.fixture
def mock_pymongo_collection():
    with patch("pymongo.collection.Collection") as mock_collection:
        yield mock_collection


@pytest.fixture
def mock_pymongo_cursor():
    with patch("pymongo.cursor.Cursor") as mock_cursor:
        yield mock_cursor


@pytest.fixture
def book_data():
    return {"_id": 1, "author": "Test author", "title": "Test title"}


def test_get_books_success_pymongo(
    mock_pymongo_collection, mock_pymongo_cursor, book_data
):
    mock_pymongo_cursor.return_value = [book_data]
    mock_pymongo_collection.find.return_value = mock_pymongo_cursor.return_value

    books = get_books(mock_pymongo_collection)
    assert (
        books is not None
    ), "Function get_books should execute successfully without raising an error."
    assert isinstance(books, list), "get_books function should return a list."
    assert len(books) > 0, "Function get_books should return list with elements."
    assert isinstance(
        books[0], dict
    ), "Elements returned by get_books should be of type dict."
    assert (
        books[0].get("title") == "Test title"
    ), "The book title in the returned list should match the expected title."
    assert (
        books[0].get("author") == "Test author"
    ), "The book author in the returned list should match the expected author."


# This test assumes that the function `get_books` accepts a PyMongo collection as its argument.


from unittest.mock import patch
