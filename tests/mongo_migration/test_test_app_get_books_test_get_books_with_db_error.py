#import pytest
#from pymongo.errors import PyMongoError
#
#from pymongo.errors import PyMongoError
#
#from tests.mongo_migration.test_test_app_get_books_test_get_books_with_db_error import *
#
#
#from unittest.mock import MagicMock
#
#
#def test_get_books_with_db_error(mocker: MagicMock):
#    """
#    Test the get_books function to ensure it handles PyMongoError properly and returns an empty list.
#    """
#    mock_collection = mocker.MagicMock()
#    mock_collection.find.side_effect = PyMongoError
#
#    result = get_books(mock_collection)
#    assert result == []
#