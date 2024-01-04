import pytest


import pytest

from app import *
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
import pymongo
from pymongo import MongoClient
from app import add_book, get_books

# Assuming that other functions aren't required to be changed, they are not included in this conversion.
# However, they must be adapted to work with MongoDB instead of a relational database.

# Setup MongoDB connection
client = MongoClient('mongodb://root:example@host.docker.internal:27018/code_robotics_1704369504122')
# Access database
db = client['code_robotics_1704369504122']
# This should reflect the actual collection name you are using for the books
books_collection = db.books

# Setup the MongoDB connection
MONGO_URI = 'mongodb://root:example@host.docker.internal:27018/code_robotics_1704369504122'
client = MongoClient(MONGO_URI)

# Setup the MongoDB connection
MONGO_DB_URI = 'mongodb://root:example@host.docker.internal:27018/code_robotics_1704369504122'


# Define the teardown_module function that closes the MongoDB connection.
def teardown_module(module):
    client.close()
client = MongoClient(MONGO_DB_URI)


# Ensure that the database connection is passed to the app module functions (if necessary)
# This might involve updating add_book and get_books functions in the app module to accept a database/client parameter


def test_add_book_in_get_books(sample_book):
    # Assuming the add_book function now takes a db and a sample_book dictionary
    add_book(db, sample_book["title"], sample_book["author"])
    
    # Assuming get_books now takes a db and returns a list of dictionaries representing books
    books = get_books(db)

    # MongoDB documents are dictionaries, we check for book attributes in the dictionaries.
    # Note that the 'title' and 'author' should be the keys as stored and retrieved from MongoDB
    found_book = any(
        book['title'] == sample_book["title"] and book['author'] == sample_book["author"]
        for book in books
    )

    assert found_book, "The book added should be in the list retrieved by get_books"
db = client['code_robotics_1704369504122']


# Convert the setup_module function to use pymongo to interact with MongoDB
def setup_module(module):
    # Connect to the MongoDB database using the provided connection string
    client = MongoClient('mongodb://root:example@host.docker.internal:27018/code_robotics_1704369504122')
    
    # Get the database object
    db = client['code_robotics_1704369504122']
    
    # Get the 'books' collection from the MongoDB database
    books_collection = db['books']
    
    # Remove all existing documents from the 'books' collection to clean it up before running tests
    books_collection.delete_many({})


# Make sure to define sample_book data and add_book function accordingly before using them.

def test_add_book_no_error(sample_book):
    books_collection = db.books  # 'books' is a placeholder, modify as needed
    try:
        result = books_collection.insert_one({
            "title": sample_book["title"],
            "author": sample_book["author"]
        })

        assert result.inserted_id is not None
    except Exception as e:
        pytest.fail(f"An exception occurred: {e}", pytrace=True)


# Pytest fixture to provide a sample book dictionary
@pytest.fixture()
def sample_book():
    return {"title": "Sample Title", "author": "Sample Author"}

# Setup and teardown functions will provide access to the MongoDB database and cleanup after tests
@pytest.fixture(scope="module")
def mongo_client():
    client = MongoClient('mongodb://root:example@host.docker.internal:27018/code_robotics_1704369504122')
    yield client
    client.close()

@pytest.fixture(scope="module")
def book_collection(mongo_client):
    # Setup code for module
    db = mongo_client.get_database('test_db')
    collection = db.get_collection('books')
    yield collection
    # Teardown code for module
    collection.delete_many({})  # Cleans up the collection after tests


def test_add_book_return_string(sample_book):
    result = add_book(sample_book["title"], sample_book["author"])
    expected_string = f"Book '{sample_book['title']}' by {sample_book['author']} added!"
    assert (
        result == expected_string
    ), "The return string is not matching the expected string"
