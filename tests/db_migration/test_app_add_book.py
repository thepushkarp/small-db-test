from unittest.mock import Mock, patch


from unittest.mock import Mock, patch
from app import Book, add_book

import pytest
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

# Assuming that the Book model and add_book function are in a module named "app"
from app import *


@pytest.fixture(scope="module")
def session():
    session = Session()
    yield session
    session.close()


@pytest.fixture(scope="module")
def new_book_mock():
    return Mock(spec=Book)


def test_add_book_no_error(session, new_book_mock):
    with patch.object(session, "add"), patch.object(session, "commit"):
        result = add_book(session, "Title", "Author")
        assert result is not None


def test_add_book_rollback_on_exception(session, new_book_mock):
    with patch.object(session, "add", side_effect=SQLAlchemyError), patch.object(
        session, "rollback"
    ) as mock_rollback:
        result = add_book(session, "Title", "Author")
        assert result is None
        mock_rollback.assert_called_once()
