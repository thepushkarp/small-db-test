from unittest.mock import Mock, patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from app import Book, add_book, create_db_engine, get_books


@pytest.fixture
def mock_session():
    return Mock()


@pytest.fixture
def mock_engine():
    return Mock()


@patch("app.create_engine")
def test_create_db_engine(mock_create_engine, mock_engine):
    mock_create_engine.return_value = mock_engine
    result = create_db_engine()
    assert result == mock_engine


def test_add_book(mock_session):
    mock_session.add = Mock()
    mock_session.commit = Mock()
    book = add_book(mock_session, "Test Title", "Test Author")
    assert isinstance(book, Book)
    assert book.title == "Test Title"
    assert book.author == "Test Author"


def test_add_book_exception(mock_session):
    mock_session.add = Mock()
    mock_session.commit = Mock(side_effect=SQLAlchemyError)
    book = add_book(mock_session, "Test Title", "Test Author")
    assert book is None


def test_get_books(mock_session):
    mock_book = Mock()
    mock_session.query.return_value.all.return_value = [mock_book]
    books = get_books(mock_session)
    assert books == [mock_book]


def test_get_books_exception(mock_session):
    mock_session.query.return_value.all.side_effect = SQLAlchemyError
    books = get_books(mock_session)
    assert books == []
