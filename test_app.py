
import unittest
from app import Book, add_book, get_books, engine, Base, Session

class TestBookApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create an in-memory database for testing
        cls.engine = engine
        Base.metadata.create_all(cls.engine)
        cls.session = Session()

    @classmethod
    def tearDownClass(cls):
        # Clean up the database
        Base.metadata.drop_all(cls.engine)

    def test_add_book(self):
        # Test adding a book
        add_book('Test Book', 'Test Author')
        result = self.session.query(Book).filter_by(title='Test Book').first()
        self.assertIsNotNone(result)
        self.assertEqual(result.author, 'Test Author')

    def test_get_books(self):
        # Test retrieving books
        self.session.add(Book(title='Another Test Book', author='Another Author'))
        self.session.commit()
        result = get_books()
        self.assertEqual(len(result), 2)  # Including the book added in test_add_book

if __name__ == '__main__':
    unittest.main()
