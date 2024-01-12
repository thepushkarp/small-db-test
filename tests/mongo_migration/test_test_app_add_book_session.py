from pymongo import MongoClient
import pytest

from tests.mongo_migration.test_test_app_add_book_session import *


import pytest


@pytest.fixture(scope="module")
def session():
    """Setup mongodb session, and close it after test"""
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test_database"]
    yield db
    client.close()


def test_session_not_none(session):
    """Test if session is correctly setup"""
    assert session is not None


def test_session_db_name(session):
    """Test if the created session has the correct database name"""
    assert session.name == "test_database"


def test_session_is_connected(session):
    """Test if session is connected to the MongoDB server."""
    # assuming 'server_info()' will throw a ServerSelectionTimeoutError
    # if it cannot connect to MongoDB
    assert session.client.server_info() is not None
