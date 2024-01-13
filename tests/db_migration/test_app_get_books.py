

from unittest.mock import MagicMock, patch
from sqlalchemy.orm.exc import NoResultFound

import pytest
from sqlalchemy.orm import Session
from unittest.mock import MagicMock, patch
from app import *
from sqlalchemy.exc import SQLAlchemyError


@pytest.fixture
def mock_session() -> MagicMock:
    return MagicMock(spec=Session)


@pytest.fixture
def mock_book() -> MagicMock:
    mock = MagicMock()
    mock.all.return_value = []
    return mock


def test_get_books_no_error(mock_session, mock_book):
    """
    Test get_books function to ensure no error is thrown and list is returned
    when the function is executed.
    """
    # Mock session query
    mock_session.query.return_value = mock_book
    result = get_books(mock_session)
    assert result is not None
    assert isinstance(result, list)


def test_get_books_with_db_error(mock_session, mock_book):
    """
    Test get_books function to ensure it handles SQLAlchemyError properly and returns an empty list.
    """
    # Trigger a SQLAlchemyError
    mock_session.query.side_effect = SQLAlchemyError
    result = get_books(mock_session)
    assert result == []


def test_get_books_with_no_result_found(mock_session, mock_book):
    """
    Test get_books function to ensure it handles NoResultFound properly and returns an empty list.
    """
    # Trigger a NoResultFound
    mock_session.query.side_effect = NoResultFound
    result = get_books(mock_session)
    assert result == []
