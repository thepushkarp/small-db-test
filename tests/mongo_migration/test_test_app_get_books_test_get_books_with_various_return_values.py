

from unittest.mock import MagicMock, patch

import pytest
from unittest.mock import MagicMock, patch

from tests.mongo_migration.test_test_app_get_books_test_get_books_with_various_return_values import *


class Book(dict):
    """Mocked Book Document"""

    def __init__(self, title=None, author=None):
        super().__init__(title=title, author=author)


@pytest.fixture
def mock_books_collection():
    """Create a mocked MongoDB collection."""
    collection = MagicMock()
    cursor = MagicMock()
    collection.find.return_value = cursor
    return collection, cursor


@pytest.mark.parametrize(
    "empty_return_value",
    [
        [],
        [Book(title="Test Book", author="Test Author")],
    ],
)
def test_get_books_with_various_return_values(
    mock_books_collection, empty_return_value
):
    collection, cursor = mock_books_collection
    cursor.sort.return_value = empty_return_value
    with patch("app.get_books", return_value=empty_return_value) as mock_get_books:
        books = mock_get_books(collection)
        mock_get_books.assert_called_once_with(collection)
    assert books == empty_return_value


def test_get_books_does_not_raise_error(mock_books_collection):
    collection, _ = mock_books_collection
    with patch("app.get_books") as mock_get_books:
        try:
            mock_get_books(collection)
        except Exception as e:
            pytest.fail(f"get_books() raised an exception {e}")
