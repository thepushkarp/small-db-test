from pymongo.collection import Collection


from unittest.mock import MagicMock, patch
from tests.mongo_migration.test_test_app_add_book_test_add_book_no_error import *
from unittest.mock import MagicMock, patch

from app import add_book
from pymongo.errors import DuplicateKeyError

import pytest


@pytest.fixture
def mocked_collection():
    with patch("pymongo.collection.Collection") as MockCollection:
        yield MagicMock(spec=Collection)


def test_add_book_no_error(mocked_collection: MagicMock):
    """Test add_book to ensure it does not raise exceptions and returns a non-None value on success."""
    # Mock the pymongo Collection's insert_one method
    mocked_insert_result = MagicMock()
    mocked_insert_result.inserted_id = "mock_id"
    mocked_collection.insert_one.return_value = mocked_insert_result

    result = add_book(mocked_collection, "Test Book", "Test Author")
    assert result is not None
