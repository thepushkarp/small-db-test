from unittest.mock import Mock, patch
from pymongo import MongoClient

import pytest
from pymongo.errors import ConnectionFailure


from unittest.mock import Mock, patch

from tests.mongo_migration.test_test_app_add_book_db import *


@pytest.fixture(scope="module")
def db():
    client = MongoClient("mongodb://localhost:27017/")
    db_test = client["test_db"]
    yield db_test
    client.close()


def test_db_exists(db):
    assert db is not None


def test_db_connection_error():
    with patch("pymongo.MongoClient") as mock:
        mock.side_effect = ConnectionFailure
        with pytest.raises(ConnectionFailure):
            db = mock()
            db.test_db.books.find_one()


def test_db_close():
    with patch("pymongo.MongoClient") as mock:
        db = mock()
        db.close()
        db.close.assert_called_once()
