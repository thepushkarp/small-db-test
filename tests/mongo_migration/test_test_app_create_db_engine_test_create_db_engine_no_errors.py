#import pytest
#
#
#from pymongo import MongoClient
#from pymongo.errors import PyMongoError
#
#from tests.mongo_migration.test_test_app_create_db_engine_test_create_db_engine_no_errors import *
#
#
#def test_create_db_engine_no_errors():
#    """
#    Test for making sure `create_db_engine()` doesn't throw any exceptions and returns an instance of `MongoClient` class.
#    This test is designed to fail if the function throws an exception or the returned object is not an instance of `MongoClient`.
#    """
#    try:
#        client = create_db_engine()
#        assert client is not None
#        assert isinstance(client, MongoClient)
#    except PyMongoError:
#        pytest.fail("create_db_engine() raised PyMongoError unexpectedly!")
#