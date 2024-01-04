from sqlalchemy import create_engine
import pytest

from app import *
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


@pytest.fixture(scope="function")
def session():
    # The MongoDB connection URI
    mongo_uri = "mongodb://root:example@host.docker.internal:27018/code_robotics_1704373301739"
    client = MongoClient(mongo_uri)

    # Attempt to connect to MongoDB server
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("Server not available")
        raise

    # Create or get a test database
    db = client['test_database']
    
    # Create or get the designated collection for tests
    collection = db['test_collection']
    
    # Clear collection before running the test
    collection.delete_many({})

    yield collection  # this is where the testing happens

    # Cleanup after tests
    collection.delete_many({})
    client.close()


def test_get_books_no_errors(session):
    books = get_books()
    assert books is not None


def test_get_books_empty_table(session):
    assert get_books() == []
