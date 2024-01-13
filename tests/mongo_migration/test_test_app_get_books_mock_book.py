from unittest.mock import MagicMock

import pytest
from pymongo.collection import Collection

from tests.mongo_migration.test_test_app_get_books_mock_book import *


@pytest.fixture
def mock_book() -> MagicMock:
    return MagicMock(spec=Collection)


def test_mock_book(mock_book):
    # Test to check if the function doesn't throw errors when it's executed
    assert mock_book is not None
    # Test to check if our mock object can mimic pymongo.collection.Collection object's behaviour
    mock_book.insert_one.assert_called
