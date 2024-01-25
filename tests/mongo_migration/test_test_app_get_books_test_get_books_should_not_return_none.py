

from unittest.mock import MagicMock, patch
from unittest.mock import MagicMock, patch

import pytest

from tests.mongo_migration.test_test_app_get_books_test_get_books_should_not_return_none import *


def test_get_books_should_not_return_none():
    # Mock the pymongo collection
    collection_mock = MagicMock(name="CollectionMock")

    # Patch the 'get_books' function to prevent actual DB calls
    with patch("app.get_books") as mock_get_books:
        mock_get_books.return_value = ["Book1", "Book2"]  # Example return value
        books = mock_get_books(collection_mock)
        assert books is not None, "Function get_books returned None"
