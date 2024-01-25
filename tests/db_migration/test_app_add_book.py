from unittest.mock import Mock, patch

import pytest
from sqlalchemy.orm import Session

from app import *


# Fixtures for setting up the mocked session and the sqlalchemy error
@pytest.fixture
def mocked_session():
    session = Mock(spec=Session)
    session.commit = Mock()
    session.add = Mock()
    session.rollback = Mock()
    return session


@pytest.fixture
def sqlalchemy_exception():
    return SQLAlchemyError("Dummy error")


# Test cases
def test_add_book_no_error(mocked_session):
    """Test add_book to ensure it does not raise exceptions and returns a non-None value on success."""
    result = add_book(mocked_session, "Test Book", "Test Author")
    assert result is not None


def test_add_book_successful_commit(mocked_session):
    """Test if add_book commits a new book to the session."""
    add_book(mocked_session, "Test Book", "Test Author")
    mocked_session.add.assert_called()
    mocked_session.commit.assert_called()


def test_add_book_handles_sqlalchemy_error(mocked_session, sqlalchemy_exception):
    """Test if add_book handles SQLAlchemyError by rolling back the session and returning None."""
    with patch("builtins.print") as mocked_print:
        mocked_session.commit.side_effect = sqlalchemy_exception
        result = add_book(mocked_session, "Test Book", "Test Author")
        mocked_session.rollback.assert_called()
        mocked_print.assert_called_with(f"Error: {sqlalchemy_exception}")
        assert result is None


# Imports for this test module
from sqlalchemy.exc import SQLAlchemyError
