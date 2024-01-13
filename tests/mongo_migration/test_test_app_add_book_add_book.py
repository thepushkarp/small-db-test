#from pytest_pymongo import Database
#import pytest
#from pymongo.errors import PyMongoError
#
#
#from unittest.mock import patch
#
#from pymongo import Collection
#
#from tests.mongo_migration.test_test_app_add_book_add_book import *
#
#
#def test_add_book(book_collection: Collection):
#    title = "Test Title"
#    author = "Test Author"
#    result = add_book(book_collection, title, author)
#    assert result is not None
#    assert result.title == title
#    assert result.author == author
#
#
#@pytest.fixture(scope="function", autouse=True)
#def book_collection(pymongo_db: Database) -> Collection:
#    collection = pymongo_db["books"]
#    yield collection
#    collection.drop()
#
#
#def test_add_book_exception(book_collection: Collection):
#    with patch("pytest_pymongo.plugin.manager") as mock_manager:
#        mock_manager.side_effect = PyMongoError
#        result = add_book(book_collection, "Test Title", "Test Author")
#        assert result is None
#