#
#import pytest
#from pymongo.errors import PyMongoError
#
#from tests.mongo_migration.test_test_app_add_book_test_add_book_exception import *
#from unittest.mock import Mock
#
#
#import pytest
#
#
#def test_add_book_exception_no_error():
#    collection = Mock()
#    title = "Title"
#    author = "Author"
#    result = add_book(collection, title, author)
#    assert result is not None
#    collection.insert_one.assert_called_once()
#
#
#def test_add_book_exception():
#    collection = Mock()
#    collection.insert_one.side_effect = PyMongoError
#    title = "Title"
#    author = "Author"
#    with pytest.raises(PyMongoError):
#        result = add_book(collection, title, author)
#    assert result is None
#
#
#def test_add_book_exception_with_error():
#    collection = Mock()
#    collection.insert_one.side_effect = PyMongoError("Custom error")
#    title = "Title"
#    author = "Author"
#    with pytest.raises(PyMongoError) as ex:
#        result = add_book(collection, title, author)
#    assert "Custom error" in str(ex.value)
#    assert result is None
#