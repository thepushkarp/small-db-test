import pytest

from app import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker




import pytest
from pymongo import MongoClient


@pytest.fixture(scope="module")
def db_session():
    # Connect to the MongoDB server
    client = MongoClient('mongodb://localhost:27017/')

    # Select the database and collection we will use
    db = client['test_database']
    collection = db['books']

    # Yields the collection to the test function
    yield collection

    # Cleanup: you can add any cleanup operation you want to perform after each test-module
    # For example, dropping the collection or the test database
    db.drop_collection('books')
    client.close()


def test_add_book_no_errors(db_session):
    global session  # Make sure to use the global session
    session = db_session
    assert add_book("Sample Title", "Sample Author") is not None
