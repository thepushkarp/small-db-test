import pytest

from app import *

# Assuming the declarative_base and other necessary imports are already available from the project context since we should not add imports that are not 100% confirmed.


@pytest.fixture(scope="module")
def setup_database():
    """
    Fixture to set up the database connection and create all tables.
    """
    engine = create_engine(
        "postgresql://postgres:root@host.docker.internal:5432/code_robotics_1703920790234"
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()


@pytest.fixture(autouse=True)
def session(setup_database):
    """
    Fixture to provide a transactional scope around each test function.
    """
    session = setup_database
    session.begin_nested()  # open a nested transaction
    yield session  # this is where the testing happens
    session.rollback()  # rollback the nested transaction after the test runs


def test_add_book_does_not_raise(session):
    """
    Test to ensure calling add_book does not raise any exceptions.
    """
    assert add_book("The Great Gatsby", "F. Scott Fitzgerald") is not None


def test_add_book_invalid_args(session):
    """
    Test to ensure that passing invalid arguments to add_book raises a TypeError.
    """
    with pytest.raises(TypeError):
        add_book("A single argument")


def test_add_book_return_value(session):
    """
    Test to ensure add_book returns correct success message after adding a book.
    """
    title = "1984"
    author = "George Orwell"
    expected = f"Book '{title}' by {author} added!"
    assert add_book(title, author) == expected


def test_get_books_after_adding_book(session):
    """
    Test to ensure that get_books contains the newly added book.
    """
    title = "To Kill a Mockingbird"
    author = "Harper Lee"
    add_book(title, author)
    books = get_books()
    assert any(book.title == title and book.author == author for book in books)
