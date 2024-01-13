from unittest.mock import patch
import os

import pytest
from pymongo import MongoClient


import os

from tests.mongo_migration.test_test_app_create_db_engine_test_create_db_engine_echo_parameter import *


from unittest.mock import patch


def create_db_engine():
    """Create a MongoDB client instance based on the environment variable DATABASE_URI."""

    database_uri = os.getenv("DATABASE_URI")
    if database_uri is None:
        raise ValueError("DATABASE_URI environment variable not set")

    client = MongoClient(database_uri)

    return client


def test_create_db_engine():
    with patch.dict("os.environ", {"DATABASE_URI": "mongodb://localhost:27017/"}):
        client = create_db_engine()
        assert (
            client is not None
        ), "The create_db_engine function should return a MongoClient instance"


def test_create_db_engine_without_env_var():
    with patch.dict("os.environ", {}, clear=True):
        with pytest.raises(ValueError) as e:
            create_db_engine()
        assert (
            str(e.value) == "DATABASE_URI environment variable not set"
        ), "Should raise a ValueError if DATABASE_URI is not set"


@pytest.fixture
def mongo_client():
    with patch.dict("os.environ", {"DATABASE_URI": "mongodb://localhost:27017/"}):
        return create_db_engine()


def test_create_db_engine_correct_host(mongo_client):
    assert (
        mongo_client.HOST == "localhost"
    ), "The MongoClient should be connected to the correct host"


def test_create_db_engine_correct_port(mongo_client):
    assert (
        mongo_client.PORT == 27017
    ), "The MongoClient should be connected to the correct port"
