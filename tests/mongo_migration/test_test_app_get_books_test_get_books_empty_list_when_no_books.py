from unittest.mock import MagicMock, patch

import pytest

from tests.mongo_migration.test_test_app_get_books_test_get_books_empty_list_when_no_books import *


# Assuming get_books uses a pymongo collection and returns a list of books
# The function name 'get_books' is guessed from the context and may differ
def get_books(collection):
    return list(collection.find({}))


# This test checks that the get_books function returns an empty list when the collection is empty
def test_get_books_empty_list_when_no_books_pymongo():
    mock_collection = MagicMock()
    mock_collection.find.return_value = []

    with patch("app.get_books", return_value=mock_collection) as mock_get_books:
        books = get_books(mock_get_books)
    assert (
        books == []
    ), "Function get_books should return an empty list when no books are found."


# Imports necessary for the mock and patch
from unittest.mock import MagicMock, patch
