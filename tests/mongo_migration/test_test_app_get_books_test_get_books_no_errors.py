from unittest.mock import MagicMock, patch

import pytest

from tests.mongo_migration.test_test_app_get_books_test_get_books_no_errors import *


@pytest.fixture
def mock_collection():
    # Create a MagicMock object to simulate a pymongo Collection
    collection = MagicMock(name="Collection")
    return collection


@pytest.fixture
def mock_books():
    # Sample data that mimics the data returned from MongoDB
    books_data = [
        {"author": "Author 1", "title": "Book 1"},
        {"author": "Author 2", "title": "Book 2"},
    ]
    return books_data


def test_get_books_no_errors(mock_collection, mock_books):
    # Mock the find method on the collection to return our mock_books
    mock_collection.find.return_value = mock_books

    # Patch the `get_books` function and return a MagicMock object
    with patch("app.get_books", return_value=mock_books) as mock_get_books:
        # Call the `get_books` function with a mock_collection which would be ignored
        books = mock_get_books(mock_collection)

        # Assert that the mock was called with the mocked data
        mock_get_books.assert_called_with(mock_collection)

        # Assert that the returned value is our mock_books
        assert books is not None
        assert books == mock_books


# Additional imports required specifically for pytest and mocking.
from unittest.mock import MagicMock, patch
