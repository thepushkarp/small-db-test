#
#import pytest
#
#from tests.mongo_migration.test_test_app_get_books_test_get_books_empty_db import *
#import pytest
#
#
#from unittest.mock import patch
#
#
#def test_get_books_empty_db(mocker):
#    # Mock the pymongo collection and its find method
#    mock_collection = mocker.patch("pymongo.collection.Collection")
#    mock_collection.find.return_value = []
#
#    # Call get_books with a mocked pymongo Collection
#    books = get_books(mock_collection)
#    assert books == []
#