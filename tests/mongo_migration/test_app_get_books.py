from app import *
import pytest
from sqlalchemy.orm import sessionmaker
from app import Book  # correction here, proper import from the file path
from sqlalchemy import create_engine



from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from pymongo.collection import Collection


# Add the necessary imports for your actual tests

@pytest.fixture(scope="module")
def db_session():  # Don't change the method name
    # Connect to the MongoDB server (replace with your actual credentials and database name)
    client = MongoClient("mongodb://username:password@hostname:port/dbname")
    db = client['dbname']  # Access the database
    
    # Setup code before yielding (if necessary, such as adding dummy data to the database)
    
    yield db  # This will be used by the tests to access the database

    # Teardown code after yielding (if necessary, such as removing dummy data from the database)
    client.close()  # Close the database connection



def test_get_books_correct_type(mongo_session):
    """
    Assumes that mongo_session is a PyMongo database session fixture provided to the test.
    """
    result = get_books()
    assert isinstance(result, list)
    # In MongoDB, documents are represented as dictionaries by PyMongo
    assert all(isinstance(book, dict) for book in result)
    # If there's a specific field or structure to the books you'd like to check, you can add further assertions


def test_get_books_no_errors(db_session):
    result = get_books()  # Make use of the session in scope
    assert result is not None
