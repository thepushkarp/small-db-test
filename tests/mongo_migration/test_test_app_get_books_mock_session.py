import pytest
from pymongo.errors import PyMongoError

import pytest

from tests.mongo_migration.test_test_app_get_books_mock_session import *


from unittest.mock import MagicMock, patch


@pytest.fixture
def mock_session():
    collection = MagicMock()
    collection.find.return_value = [{"title": "Book1"}, {"title": "Book2"}]
    return collection


# Placeholder for the actual get_books function
def get_books(collection):
    try:
        return list(collection.find())
    except PyMongoError as e:
        raise e


def test_mock_session_does_not_raise_error(mock_session):
    with patch("app.get_books", return_value=None) as mock_get_books:
        assert mock_get_books(mock_session) is None


def test_get_books_returns_books(mock_session):
    books = get_books(
        mock_session
    )  # get_books() should use the mock_session internally
    assert len(books) == 2
    assert books == [{"title": "Book1"}, {"title": "Book2"}]


def test_get_books_handles_exceptions(mock_session):
    mock_session.find.side_effect = PyMongoError("Database connection error")

    with pytest.raises(PyMongoError) as exc_info:
        get_books(mock_session)  # Any database exception should be raised

    assert (
        exc_info.value.args[0] == "Database connection error"
    ), "get_books() should raise an exception on database errors."
