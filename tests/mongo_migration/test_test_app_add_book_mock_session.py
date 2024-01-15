

from unittest.mock import patch

from tests.mongo_migration.test_test_app_add_book_mock_session import *
from unittest.mock import patch

import pytest
from pymongo import MongoClient


@pytest.fixture
def mock_db():
    with patch("pymongo.MongoClient") as mock_client:
        yield mock_client


# Tests


def test_mock_session_initialization(mock_db):
    assert mock_db is not None


@pytest.mark.parametrize(
    "data",
    [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "1984", "author": "George Orwell"},
    ],
)
def test_mock_session_insertion(mock_db, data):
    db = mock_db()
    db.test.books.insert_one.assert_not_called()
    db.test.books.insert_one(data)
    db.test.books.insert_one.assert_called_once_with(data)


def test_mock_session_find(mock_db):
    db = mock_db()
    db.test.books.find.assert_not_called()
    db.test.books.find({})
    db.test.books.find.assert_called_once_with({})


def test_mock_session_update(mock_db):
    db = mock_db()
    filter_query = {"title": "The Great Gatsby"}
    update_data = {"$set": {"author": "Fitzgerald"}}
    db.test.books.update_one.assert_not_called()
    db.test.books.update_one(filter_query, update_data)
    db.test.books.update_one.assert_called_once_with(filter_query, update_data)


def test_mock_session_deletion(mock_db):
    db = mock_db()
    filter_query = {"title": "The Great Gatsby"}
    db.test.books.delete_one.assert_not_called()
    db.test.books.delete_one(filter_query)
    db.test.books.delete_one.assert_called_once_with(filter_query)


def test_mock_session_exception(mock_db):
    db = mock_db()
    db.test.books.insert_one.side_effect = Exception("Insert failed")
    with pytest.raises(Exception) as excinfo:
        db.test.books.insert_one({"title": "The Great Gatsby"})
    assert "Insert failed" in str(excinfo.value)
