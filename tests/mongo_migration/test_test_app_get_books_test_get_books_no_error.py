

from unittest.mock import MagicMock, patch

from tests.mongo_migration.test_test_app_get_books_test_get_books_no_error import *
import pytest
from pymongo.database import Database

import pytest


def get_books(db: Database):
    """
    Fetches all books from MongoDB collection.
    """
    books_collection = db["books"]
    return list(books_collection.find())


def test_get_books_no_error(mock_db, mock_books):
    """
    Test get_books function to ensure no error is thrown and list is returned
    when the function is executed.
    """
    mock_db.__getitem__.return_value.find.return_value = mock_books
    result = get_books(mock_db)
    assert result is not None
    assert isinstance(result, list)


@pytest.fixture
def mock_db():
    return MagicMock(spec=Database)


@pytest.fixture
def mock_books():
    return [
        {
            "_id": 1,
            "title": "The Old Man and the Sea",
            "author": "Ernest Hemingway",
            "year_published": 1952,
        },
        {
            "_id": 2,
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "year_published": 1960,
        },
    ]
