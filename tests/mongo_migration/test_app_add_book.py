import pytest

from app import *
import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection

# Assuming 'mydatabase' is the database and 'mycollection' is the collection we want to use
DATABASE_NAME = 'mydatabase'


# Import the pymongo MongoClient or the add_book function if it is a separate module
# Since no imports are visible for the add_book function, it is assumed to be in the same file scope.

# Import for the add_book if needed (not shown due to knowledge cutoff restriction)

def test_add_book_invalid_args(session):
    """
    Test to ensure that passing invalid arguments to add_book raises a TypeError.
    """
    with pytest.raises(TypeError):
        add_book("A single argument")
COLLECTION_NAME = 'mycollection'


# Fixture to set up the MongoDB database and clean it up after the test
@pytest.fixture(autouse=True)
def session():
    """
    Fixture to provide a clean MongoDB collection around each test function.
    """
    client = MongoClient('localhost', 27017)  # Connect to MongoDB
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    yield collection  # this is where the testing happens
    collection.delete_many({})  # Clean up the collection after each test


# Assuming you have a database called 'code_robotics' and a collection called 'books'

@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up the database connection.
    """
    # Connect to MongoDB using pymongo
    client = MongoClient(host='host.docker.internal', port=27017, username='root', password='root')
    db = client.code_robotics
    yield db

    # Cleanup code: Drop the 'books' collection after tests to start with a fresh state (Optional)
    db.drop_collection('books')
    client.close()


def test_add_book_does_not_raise(session):
    """
    Test to ensure calling add_book does not raise any exceptions.
    """
    assert add_book("The Great Gatsby", "F. Scott Fitzgerald") is not None


def test_add_book_return_value(session):
    """
    Test to ensure add_book returns correct success message after adding a book.
    """
    title = "1984"
    author = "George Orwell"
    expected = f"Book '{title}' by {author} added!"
    assert add_book(title, author) == expected


def test_get_books_after_adding_book(session):
    """
    Test to ensure that get_books contains the newly added book.
    """
    title = "To Kill a Mockingbird"
    author = "Harper Lee"
    add_book(title, author)
    books = get_books()
    assert any(book.title == title and book.author == author for book in books)
