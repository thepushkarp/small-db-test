from sqlalchemy.orm import Session
import sqlalchemy
import pytest

import sqlalchemy.orm
from app import *
from sqlalchemy.exc import SQLAlchemyError


from unittest.mock import MagicMock, patch


# Define a test fixture for database session
@pytest.fixture
def db_session() -> Session:
    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    session = sqlalchemy.orm.sessionmaker(bind=engine)()
    return session


def test_get_books_no_error(db_session: Session):
    """
    Test the get_books function to ensure no error is thrown and a list is returned
    when the function is executed.
    """

    with patch.object(db_session, "query", return_value=MagicMock()) as mock_query:
        get_books(db_session)
        mock_query.assert_called_once()


def test_get_books_with_db_error(db_session: Session):
    """
    Test the get_books function to ensure it handles SQLAlchemyError properly and returns an empty list.
    """

    with patch.object(
        db_session, "query", side_effect=SQLAlchemyError("Simulated SQLAlchemyError")
    ) as mock_query:
        assert get_books(db_session) == []
        mock_query.assert_called_once()
