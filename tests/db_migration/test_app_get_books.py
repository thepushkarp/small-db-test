
import pytest
from sqlalchemy import create_engine
from app import *
from sqlalchemy.orm import Session, sessionmaker
from unittest.mock import MagicMock, create_autospec, patch


# Define a test fixture for database session
@pytest.fixture
def db_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    return Session()


# Define a test fixture for a mock book object
@pytest.fixture
def mock_book() -> MagicMock:
    return MagicMock(spec=Book)


def test_get_books_no_error(mock_book: MagicMock):
    """
    Test the get_books function to ensure no error is thrown and a list is returned
    when the function is executed.
    """
    # Mock session query
    mock_session = create_autospec(Session)
    mock_session.query.return_value.all.return_value = [mock_book]

    result = get_books(mock_session)
    assert result is not None
    assert isinstance(result, list)


def test_get_books_with_db_error(mock_book: MagicMock):
    """
    Test the get_books function to ensure it handles SQLAlchemyError properly and returns an empty list.
    """
    # Trigger a SQLAlchemyError
    mock_session = create_autospec(Session)
    mock_session.query.return_value.all.side_effect = SQLAlchemyError

    result = get_books(mock_session)
    assert result == []
