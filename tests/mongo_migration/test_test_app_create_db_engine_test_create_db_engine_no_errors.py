#
#
#import pytest
#import pytest
#
#from tests.mongo_migration.test_test_app_create_db_engine_test_create_db_engine_no_errors import *
#from app import create_db_client
#
#
#def test_create_db_client_no_errors(mongodb_uri: str):
#    """
#    Test for making sure `create_db_client()` doesn't throw any exceptions and returns some non-null value.
#    This test will fail if the function throws an exception or the return value is None.
#    """
#    try:
#        client = create_db_client(mongodb_uri)
#        assert client is not None
#    except Exception:
#        pytest.fail("create_db_client() raised Exception unexpectedly!")
#
#
## Mock mongodb uri
#@pytest.fixture
#def mongodb_uri():
#    return "mongodb://localhost:27017/testdb"
#