from pymongo import MongoClient

from tests.mongo_migration.test_test_app_get_books_mock_session import *


from unittest.mock import MagicMock, patch
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture()
def mock_mongo_client():
    with patch("pymongo.MongoClient") as mock_client:
        mock_db = MagicMock()
        mock_client().__getitem__.return_value = mock_db
        yield mock_db


# Tests for mock_mongo_client fixture
def test_mock_mongo_client_returns_not_none(mock_mongo_client):
    assert mock_mongo_client is not None


def test_mock_mongo_client_has_collection_accessor(mock_mongo_client):
    assert hasattr(mock_mongo_client, "__getitem__")


def test_mock_mongo_client_collection_accessor_returns_mongodb_collection_object(
    mock_mongo_client,
):
    collection = mock_mongo_client["example_collection"]
    assert isinstance(collection, MagicMock)


def test_mock_mongo_client_collection_methods_are_mocked(mock_mongo_client):
    methods_to_check = ["insert_many", "find", "update_one", "delete_one"]
    for method in methods_to_check:
        assert hasattr(mock_mongo_client["example_collection"], method)
        assert isinstance(
            getattr(mock_mongo_client["example_collection"], method), MagicMock
        )


def test_mock_mongo_client_collection_methods_count(mock_mongo_client):
    mock_mongo_client["example_collection"].find.call_count = 0
    collection = mock_mongo_client["example_collection"]
    collection.find({})
    assert collection.find.call_count == 1
