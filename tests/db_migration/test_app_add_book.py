
from app import *
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from unittest.mock import Mock

import pytest

# Assuming that the session and Book are available in scope as we cannot import these directly
# (e.g., from mypackage.models import session, Book)


@pytest.fixture(scope="module")
def db_session():
    # Setting up a test database session
    engine = create_engine(
        "postgresql://pupa:postgres@host.docker.internal:5432/code_robotics_1704262983446"
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


@pytest.fixture(scope="module")
def mock_book_class():
    # Assuming Book class is in scope, we create a Mock for the Book class
    return Mock(spec=Book)


def test_add_book_no_error(db_session, mock_book_class):
    """Test if the function doesn't throw errors when it's executed."""
    original_add = db_session.add
    original_commit = db_session.commit

    # Mocking the session's add and commit methods
    db_session.add = Mock()
    db_session.commit = Mock()

    try:
        response = add_book("Sample Title", "Sample Author")
        assert response is not None
        # Restore the original session methods after test
    finally:
        db_session.add = original_add
        db_session.commit = original_commit


def test_add_book_return_value(db_session, mock_book_class):
    """Test if the return value is the correct success message."""
    original_add = db_session.add
    original_commit = db_session.commit

    db_session.add = Mock()
    db_session.commit = Mock()

    expected_message = "Book 'Sample Title' by Sample Author added!"

    try:
        result = add_book("Sample Title", "Sample Author")
        assert result == expected_message
    finally:
        db_session.add = original_add
        db_session.commit = original_commit


# Necessary imports for the tests above
from sqlalchemy import create_engine
