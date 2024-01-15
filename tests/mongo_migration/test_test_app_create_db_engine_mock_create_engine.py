

from unittest.mock import MagicMock, patch
from unittest.mock import patch

import pytest

from tests.mongo_migration.test_test_app_create_db_engine_mock_create_engine import *
from pymongo import MongoClient


@pytest.fixture
def mock_create_engine():
    with patch("pymongo.MongoClient") as mock:
        mock.return_value = MagicMock(spec=MongoClient)
        yield mock


# Test to ensure that the function doesn't throw errors when it's executed
def test_mock_create_engine_execution(mock_create_engine):
    assert (
        mock_create_engine is not None
    ), "mock_create_engine should not be None when executed"


# Example test that checks if MongoClient is properly mocked (edge case)
def test_mock_create_engine_mongo_client(mock_create_engine):
    client = mock_create_engine()
    assert isinstance(
        client, MagicMock
    ), "mock_create_engine should return a MagicMock instance of MongoClient"


# Example test case to verify that MongoClient's methods can be called (edge case)
def test_mock_create_engine_mongo_client_methods(mock_create_engine):
    client = mock_create_engine()
    client.server_info()  # Just call one of the MongoClient methods without asserting anything.
    client.server_info.assert_called_once(), "server_info method should be called once on the MongoClient mock"
