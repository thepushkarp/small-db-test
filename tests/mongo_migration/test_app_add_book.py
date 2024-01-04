from app import *
import pytest
from yourapp import add_book
from pymongo.errors import PyMongoError
from pymongo.errors import TypeError
from yourapplication import add_book



@pytest.fixture(scope="module")
def mock_session():
    class MockSession:
        def add(self, book):
            pass

        def commit(self):
            pass

        def rollback(self):
            pass

    return MockSession()


# mock_session in the context of pymongo would likely be a MagicMock object
# representing a collection, which allows you to intercept methods like 'insert_one'. 

def test_add_book_no_error(mock_collection):  # Renamed mock_session to mock_collection
    inserted_book = {
        "title": "1984",
        "author": "George Orwell"
    }

    try:
        # Use the insert_one method to add a new book
        # You have to make sure that the add_book function in your app uses the
        # mocked collection's insert_one method for this to be effective.
        result = add_book("1984", "George Orwell", mock_collection)
        assert result is not None
        assert mock_collection.insert_one.called  # Confirm that insert_one was called    
    
    finally:
        # Rollback in pymongo context: Delete the test data.
        # If you're mocking the methods this step would not actually hit the database.
        try:
            mock_collection.delete_one(inserted_book)
        except PyMongoError as e:
            # Handle the exception if delete operation fails
            print(f"An error occurred while cleaning up test: {e}")


# In a real-world scenario, 'yourapplication' would be the name of your Python file/module where 'add_book' is defined.
# Make sure to replace 'yourapplication' with the appropriate module name.

def test_add_book_invalid_arguments():
    with pytest.raises(TypeError):
        add_book("Fahrenheit 451")


def test_add_book_valid_return_value(mock_session):
    title = "The Hitchhiker's Guide to the Galaxy"
    author = "Douglas Adams"
    expected_response = f"Book '{title}' by {author} added!"

    response = add_book(title, author)

    assert response == expected_response


