import unittest
from unittest.mock import Mock, patch

from sqlalchemy.exc import SQLAlchemyError

from app import Book, add_book, create_db_engine, get_books


class TestApp(unittest.TestCase):
    def setUp(self):
        self.mock_session = Mock()
        self.mock_engine = Mock()

    @patch("app.create_engine")
    def test_create_db_engine(self, mock_create_engine):
        mock_create_engine.return_value = self.mock_engine
        result = create_db_engine()
        self.assertEqual(result, self.mock_engine)

    def test_add_book(self):
        self.mock_session.add = Mock()
        self.mock_session.commit = Mock()
        book = add_book(self.mock_session, "Test Title", "Test Author")
        self.assertIsInstance(book, Book)
        self.assertEqual(book.title, "Test Title")
        self.assertEqual(book.author, "Test Author")

    def test_add_book_exception(self):
        self.mock_session.add = Mock()
        self.mock_session.commit = Mock(side_effect=SQLAlchemyError)
        book = add_book(self.mock_session, "Test Title", "Test Author")
        self.assertIsNone(book)

    def test_get_books(self):
        mock_book = Mock()
        self.mock_session.query.return_value.all.return_value = [mock_book]
        books = get_books(self.mock_session)
        self.assertEqual(books, [mock_book])

    def test_get_books_exception(self):
        self.mock_session.query.return_value.all.side_effect = SQLAlchemyError
        books = get_books(self.mock_session)
        self.assertEqual(books, [])


if __name__ == "__main__":
    unittest.main()
