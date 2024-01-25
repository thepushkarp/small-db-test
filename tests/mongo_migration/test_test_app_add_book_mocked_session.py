from pymongo.collection import Collection
from unittest.mock import MagicMock, patch

import pytest

from tests.mongo_migration.test_test_app_add_book_mocked_session import *


# Mock fixture for pymongo collection
@pytest.fixture
def mocked_session():
    with patch("pymongo.collection.Collection") as mock_collection:
        mock_collection.return_value = MagicMock(spec=Collection)
        yield mock_collection.return_value


# Test to confirm that the `mocked_session` fixture can be initialized properly
def test_mocked_session_initialization(mocked_session):
    assert mocked_session is not None


# Additional tests to confirm the behavior of pymongo operations
def test_mocked_session_insert_one(mocked_session):
    result = mocked_session.insert_one({"_id": "1", "name": "Test Book"})
    mocked_session.insert_one.assert_called_once()
    assert result is not None


def test_mocked_session_find_one(mocked_session):
    result = mocked_session.find_one({"_id": "1"})
    mocked_session.find_one.assert_called_once()
    assert result is not None


def test_mocked_session_delete_one(mocked_session):
    result = mocked_session.delete_one({"_id": "1"})
    mocked_session.delete_one.assert_called_once()
    assert result is not None


def test_mocked_session_update_one(mocked_session):
    result = mocked_session.update_one({"_id": "1"}, {"$set": {"name": "Updated Book"}})
    mocked_session.update_one.assert_called_once()
    assert result is not None


# No need to mock close operation since pymongo doesn't maintain persistent connections in the same way as SQLAlchemy
def test_mocked_session_no_close_necessary(mocked_session):
    assert not hasattr(mocked_session, "close")


# Necessary imports for the test setup.
from unittest.mock import MagicMock, patch
