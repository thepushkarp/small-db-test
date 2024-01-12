#from pymongo import MongoClient
#
#from tests.mongo_migration.test_test_app_get_books_mock_session import *
#from unittest.mock import MagicMock
#
#import pytest
#
#
#@pytest.fixture
#def mock_session() -> MagicMock:
#    return MagicMock(spec=MongoClient)
#
#
#def test_mock_session_creation(mock_session):
#    assert isinstance(mock_session, MagicMock)
#
#
#def test_mock_session_return_value(mock_session):
#    assert mock_session.some_function() is not None
#