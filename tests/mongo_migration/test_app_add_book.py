from app import session

from app import *
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session




import pytest
from pymongo import MongoClient


@pytest.fixture(scope="function")
def db_session():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test_database']
    
    # Create a new dictionary to hold collections so we can delete them after testing
    collections = {}
    for collection_name in db.list_collection_names():
        collections[collection_name] = list(db[collection_name].find())

    yield db
    
    # Cleanup: Drop the collections to ensure isolation after tests
    for collection_name in collections.keys():
        db.drop_collection(collection_name)

    # Revert any changes made to other collections by inserting the old documents
    for collection_name, documents in collections.items():
        if len(documents) > 0:
            db[collection_name].insert_many(documents)

    client.close()


def test_add_book_no_errors(db_session):
    title = "Test Book"
    author = "Test Author"
    assert add_book(title, author) is not None
