from app import get_books

from tests.mongo_migration.test_test_app_get_books_test_get_books_with_no_result_found import *
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_books_collection():
    return MagicMock()


def test_get_books_with_no_result_found(mock_books_collection: MagicMock):
    mock_books_collection.find.return_value = []
    result = get_books(mock_books_collection)
    assert result == [], "Expected an empty list but got {}".format(result)
