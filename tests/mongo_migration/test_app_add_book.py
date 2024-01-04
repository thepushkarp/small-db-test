import pytest

from app import *




from app import add_book
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId


# Typically, db_session would be replaced with a function or fixture that returns a reference to a MongoDB collection
# However, as per instruction, we do not know and should not assume the fixture name, so we'll keep it as db_session

def test_add_book_returns_correct_string(db_session):
    title = "Sample Title"
    author = "Sample Author"
    # The add_book function would interact with MongoDB and return a result message
    # It needs to be adjusted outside this code block to work with MongoDB
    result_message = add_book(title, author)
    assert result_message == f"Book '{title}' by {author} added!"


# Assuming add_book function is already accessible from somewhere,
# and it takes a title and author and adds a book to the MongoDB collection,
# then returns the ObjectId of the inserted document

# Assuming db_session is a PyMongo collection object and is provided to each test

def test_add_book_no_errors(db_session):
    result = add_book(db_session, "Test Title", "Test Author")
    assert result is not None
    assert isinstance(result, ObjectId)


@pytest.fixture(scope="module")
def db_session():
    # Define the MongoDB connection string
    MONGO_URL = "mongodb://root:password@localhost:27017/mydatabase"  # Adjust the URL as needed

    # Create a MongoDB client
    client = MongoClient(MONGO_URL)

    # Get the database to use for testing
    db = client['mydatabase']

    try:
        yield db
    finally:
        # Clean up by dropping the database or collections if necessary
        client.drop_database('mydatabase')  # Or drop specific collections as needed
        client.close()
