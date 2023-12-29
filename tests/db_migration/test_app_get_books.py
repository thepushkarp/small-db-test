from app import *
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Define a fixture for the engine
@pytest.fixture(scope="module")
def engine():
    return create_engine(
        "postgresql://postgres:root@localhost:5432/code_robotics_1703825513833"
    )


# Define a fixture for the session
@pytest.fixture(scope="module")
def session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


# Define a fixture for the Book model
@pytest.fixture(scope="module")
def Book():
    Base = declarative_base()

    class Book(Base):
        __tablename__ = "books"

        id = Column(Integer, primary_key=True)
        title = Column(String)
        author = Column(String)

    return Book


# Test that the function executes without error and does not return None
def test_get_books(session, Book):
    assert get_books() is not None
