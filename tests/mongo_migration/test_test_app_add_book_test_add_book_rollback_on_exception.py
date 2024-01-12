
from tests.mongo_migration.test_test_app_add_book_test_add_book_rollback_on_exception import *
from pymongo.errors import OperationFailure
import pytest

import pytest
from app import add_book


from unittest.mock import Mock


def test_add_book_rollback_on_exception(book_collection_mock, new_book_mock):
    book_collection_mock.insert_one.side_effect = OperationFailure
    result = add_book(book_collection_mock, "Title", "Author")
    assert result is None


@pytest.fixture
def book_collection_mock():
    collection = Mock()
    return collection


@pytest.fixture
def new_book_mock():
    return {"title": "Title", "author": "Author"}


def test_add_book_rollback_on_exception(book_collection_mock, new_book_mock):
    book_collection_mock.insert_one.side_effect = OperationFailure
    result = add_book(book_collection_mock, "Title", "Author")
    assert result is None
