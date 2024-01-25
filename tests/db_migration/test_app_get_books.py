from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


from unittest.mock import Mock, create_autospec

import pytest
from app import *
from unittest.mock import Mock, create_autospec


# Mocking the Book class which is assumed to already be in scope.
class Book:
    # assuming the Book class has an id, title, and author properties for the purpose of this test
    id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    author = Column(String(length=50))


@pytest.fixture
def session_mock():
    session = create_autospec(Session, instance=True)
    Mock(spec=sessionmaker)
    return session


def test_get_books_should_not_return_none(session_mock):
    books = get_books(session_mock)
    assert books is not None, "Function get_books returned None"


def test_get_books_success(session_mock):
    # Mock successful query
    mock_book_instance = Book()
    mock_book_instance.id = 1
    mock_book_instance.title = "Test title"
    mock_book_instance.author = "Test author"

    session_mock.query.return_value.all.return_value = [mock_book_instance]

    books = get_books(session_mock)
    assert len(books) > 0, "Function get_books should return list with elements."
    assert isinstance(
        books[0], Book
    ), "Elements returned by get_books should be instances of Book."


def test_get_books_empty_list_on_exception(session_mock):
    # Mock an exception during querying
    session_mock.query.side_effect = SQLAlchemyError

    books = get_books(session_mock)
    assert books == [], "Function get_books should return an empty list on exception."
    session_mock.query.assert_called_once(), "Session query should be called once."


def test_get_books_empty_list_when_no_books(session_mock):
    # Mock no books in database
    session_mock.query.return_value.all.return_value = []

    books = get_books(session_mock)
    assert (
        books == []
    ), "Function get_books should return an empty list when no books found."
