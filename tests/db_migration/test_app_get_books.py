from sqlalchemy.orm import Session
from unittest.mock import Mock, patch
from sqlalchemy.exc import SQLAlchemyError

import pytest

from app import *


from unittest.mock import Mock, patch


# Test if `get_books` can be called without raising an exception
def test_get_books_no_exception():
    session_mock = Mock(spec=Session)
    with patch("builtins.print") as mock_print:
        books = get_books(session_mock)
        assert books is not None
        mock_print.assert_not_called()


# Test if `get_books` returns an empty list when there are no books
def test_get_books_empty_db():
    session_mock = Mock(spec=Session)
    session_mock.query.return_value.all.return_value = []
    books = get_books(session_mock)
    assert books == []


# Test if `get_books` returns a non-empty list when books are present
def test_get_books_with_books():
    mock_book = Mock(spec=Book)
    session_mock = Mock(spec=Session)
    session_mock.query.return_value.all.return_value = [mock_book]
    books = get_books(session_mock)
    assert len(books) == 1
    assert books[0] == mock_book


# Test if `get_books` returns an empty list and prints an error when there is a SQLAlchemyError
def test_get_books_sqlalchemy_error():
    session_mock = Mock(spec=Session)
    session_mock.query.side_effect = SQLAlchemyError("Mocked error")
    with patch("builtins.print") as mock_print:
        books = get_books(session_mock)
        assert books == []
        mock_print.assert_called_once_with("Error: Mocked error")

# Necessary imports for the unit tests
import pytest
