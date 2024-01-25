#
#from app import get_books
#from tests.mongo_migration.test_test_app_get_books_test_get_books_sqlalchemy_error_handled import *
#from pymongo.errors import PyMongoError
#from unittest.mock import Mock, patch
#
#
#from unittest.mock import Mock, patch
#
#from pymongo.errors import PyMongoError
#
#import pytest
#
#
#def test_get_books_pymongo_error_handled():
#    mock_mongo_collection = Mock()
#    mock_mongo_collection.find.side_effect = PyMongoError
#
#    with patch("builtins.print") as mock_print:
#        books = get_books(mock_mongo_collection)
#        assert mock_print.call_count == 1
#        mock_mongo_collection.find.assert_called_once()
#        assert books == []
#