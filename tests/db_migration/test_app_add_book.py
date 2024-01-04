
import pytest

from app import *
from unittest.mock import MagicMock, patch

# Since we have a folder structure and file path, we will import add_book accordingly.
# Assuming 'app' is the file name in the directory structure.

# Constants for test
DATABASE_URL = (
    "postgresql://postgres:root@host.docker.internal:5432/code_robotics_1704373301739"
)

# Sample data for testing
SAMPLE_TITLE = "Sample Book"
SAMPLE_AUTHOR = "Sample Author"


@pytest.fixture
def mock_session():
    with patch("app.create_engine") as mock_engine:
        mock_engine.return_value = MagicMock()
        SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=mock_engine.return_value
        )
        mock_session = MagicMock(spec=SessionLocal())
        yield mock_session


def test_add_book_runs_without_errors(mock_session):
    with patch("app.session", new=mock_session):
        result = add_book(title=SAMPLE_TITLE, author=SAMPLE_AUTHOR)
        assert result is not None


# This test will ensure the message returned upon adding a book is correct
def test_add_book_returns_correct_message(mock_session):
    with patch("app.session", new=mock_session):
        result = add_book(title=SAMPLE_TITLE, author=SAMPLE_AUTHOR)
        expected_message = f"Book '{SAMPLE_TITLE}' by {SAMPLE_AUTHOR} added!"
        assert result == expected_message


# Testing add_book with incorrect types should yield TypeError
# This test isn't included in the TGG so it has been commented out.
"""
def test_add_book_raises_error_with_invalid_arguments(mock_session):
    with pytest.raises(TypeError), patch("app.session", new=mock_session):
        add_book()
"""


# Testing add_book behavior when there is a database exception
def test_add_book_handles_db_exceptions(mock_session):
    mock_session.add.side_effect = Exception("Database Error")
    with pytest.raises(Exception), patch("app.session", new=mock_session):
        add_book(title=SAMPLE_TITLE, author=SAMPLE_AUTHOR)


# Necessary imports at the bottom as per instructions
