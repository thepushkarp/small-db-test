
from tests.mongo_migration.test_test_app_add_book_mock_session import *

import pytest
from unittest.mock import MagicMock, patch


# Since we are converting to use pymongo, let's mock pymongo's collection operation
class MockCollection:
    def __init__(self):
        self.insert_one = MagicMock()
        self.update_one = MagicMock()
        self.find_one = MagicMock()
        self.delete_one = MagicMock()


# This is a mock for pymongo's database object
class MockDatabase:
    def __init__(self):
        self.collection = MagicMock(return_value=MockCollection())


# Now we will create a fixture that mocks mongodb session using pymongo's data access patterns
@pytest.fixture
def mock_session():
    with patch("pymongo.MongoClient") as mock_client:
        mock_db = MockDatabase()
        mock_client.return_value.__getitem__ = MagicMock(return_value=mock_db)
        yield mock_client


# Tests for mock_session pytest fixture
def test_mock_session_does_not_throw(mock_session):
    # This test checks the syntax and whether the fixture can be used without throwing an error
    assert mock_session is not None, "mock_session fixture should not return None"


def test_mock_session_has_collection(mock_session):
    client = mock_session()
    db = client["testdb"]
    collection = db.collection("testcollection")
    assert collection is not None, "The mock session should have a collection object"


def test_mock_session_can_insert(mock_session):
    client = mock_session()
    db = client["testdb"]
    collection = db.collection("testcollection")
    collection.insert_one({"test": "data"})
    collection.insert_one.assert_called_once()


def test_mock_session_can_update(mock_session):
    client = mock_session()
    db = client["testdb"]
    collection = db.collection("testcollection")
    collection.update_one({"test": "data"}, {"$set": {"test": "updated_data"}})
    collection.update_one.assert_called_once()


def test_mock_session_can_find(mock_session):
    client = mock_session()
    db = client["testdb"]
    collection = db.collection("testcollection")
    collection.find_one({"test": "data"})
    collection.find_one.assert_called_once()


def test_mock_session_can_delete(mock_session):
    client = mock_session()
    db = client["testdb"]
    collection = db.collection("testcollection")
    collection.delete_one({"test": "data"})
    collection.delete_one.assert_called_once()


# Necessary import from pymongo that would go at the top of the file
from pymongo import MongoClient
