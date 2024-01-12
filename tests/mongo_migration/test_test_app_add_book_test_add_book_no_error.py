#
#
#from unittest.mock import patch
#from bson import ObjectId
#
#from tests.mongo_migration.test_test_app_add_book_test_add_book_no_error import *
#
#import pytest
#from unittest.mock import patch
#
#
#from unittest.mock import Mock
#from pymongo.collection import Collection
#
#
#def test_add_book_no_error(mongo_collection: Collection, book: dict):
#    with patch.object(mongo_collection, "insert_one") as insert_one_mock:
#        insert_one_mock.return_value = {"_id": ObjectId()}
#        result = add_book(mongo_collection, book["title"], book["author"])
#        assert result is not None
#
#
#@pytest.fixture
#def book():
#    return {"title": "Title", "author": "Author"}
#
#
#@pytest.fixture
#def mongo_collection():
#    return Mock(spec=Collection)
#