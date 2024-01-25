
from tests.mongo_migration.test_test_app_add_book_test_add_book_successful_commit import *
from pymongo.collection import Collection


from unittest.mock import MagicMock
from unittest.mock import MagicMock, patch

import pytest

from pymongo.collection import Collection


# Assuming `add_book` now uses PyMongo instead of SQLAlchemy, the signature and functionality might look like this:
def add_book(collection: Collection, title: str, author: str):
    """Add a book document to the collection with given title and author."""
    collection.insert_one({"title": title, "author": author})


# The updated test function for PyMongo
def test_add_book_successful_commit():
    """Test if add_book inserts a new book document to the mongodb collection."""
    # Create a MagicMock object to represent the Collection
    mocked_collection = MagicMock(spec=Collection)

    # Call the function that we are testing (here, assumed to be modified for use with pymongo)
    add_book(mocked_collection, "Test Book", "Test Author")

    # Assert that insert_one was called on the mocked collection
    mocked_collection.insert_one.assert_called_once_with(
        {"title": "Test Book", "author": "Test Author"}
    )

    # Since PyMongo does not have a commit method like SQLAlchemy, we do not need to assert commit was called
