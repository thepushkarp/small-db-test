
from tests.mongo_migration.test_test_app_create_db_engine_test_create_db_engine_no_errors import *
import pytest
from pymongo import MongoClient


from pymongo import MongoClient


def create_db_engine():
    """Creates a database engine using pymongo.

    Returns:
        MongoClient: A client instance connected to a MongoDB service.
    """
    client = MongoClient("localhost", 27017)
    return client


def test_create_db_engine_no_errors():
    client = create_db_engine()
    assert isinstance(
        client, MongoClient
    ), "create_db_engine should return a MongoClient instance"


def test_create_db_engine_default_host_port():
    client = create_db_engine()
    default_host = "localhost"
    default_port = 27017
    assert (
        client.HOST == default_host and client.PORT == default_port
    ), "create_db_engine should connect to the default host and port"


def test_create_db_engine_return_value():
    client = create_db_engine()
    assert client is not None, "create_db_engine should return a not None value"
