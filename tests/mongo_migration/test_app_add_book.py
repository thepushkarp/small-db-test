from app import *
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from unittest.mock import Mock

import pytest


from sqlalchemy import create_engine
from pymongo import MongoClient
from app import add_book

# Replace the following URI with your MongoDB connection URI
MONGO_URI = "mongodb://your_mongo_user:your_mongo_password@host:port/your_database"


# Define the function with the same name as requested
def test_add_book_no_error(db_collection, mock_book_class):
    """Test if the function doesn't throw errors when it's executed."""
    # Mock the PyMongo insert_one method instead
    original_insert_one = db_collection.insert_one
    
    # Set the insert_one method to a Mock object
    db_collection.insert_one = Mock()

    try:
        # Call the add_book function which should interact with the mocked insert_one method
        response = add_book("Sample Title", "Sample Author")
        # Assert that a response (acknowledgment from the mock insert) was received
        assert response is not None
    finally:
        # Reset the insert_one method back to its original state
        db_collection.insert_one = original_insert_one


def test_add_book_return_value(db_collection, mock_book_class):
    """Test if the return value is the correct success message."""
    original_insert_one = db_collection.insert_one

    db_collection.insert_one = Mock()

    expected_message = "Book 'Sample Title' by Sample Author added!"

    try:
        result = add_book("Sample Title", "Sample Author")
        assert result == expected_message
    finally:
        db_collection.insert_one = original_insert_one


@pytest.fixture(scope="module")
def db_session():
    client = MongoClient(MONGO_URI)
    return client['your_database']  # Replace with your database name


@pytest.fixture(scope="module")
def mock_book_class():
    return Mock(spec=Book)
