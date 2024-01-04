from app import *
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['bookDB']


@pytest.fixture(scope="module")
def engine():
    client = MongoClient("mongodb://localhost:27017/")
    return client['code_robotics_1703825513833']


@pytest.fixture(scope="module")
def session():
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    return db



def test_get_books():
    assert db.books.find() is not None


@pytest.fixture(scope="module")
def Book():
    Base = declarative_base()

    class Book(Base):
        __tablename__ = "books"

        id = Column(Integer, primary_key=True)
        title = Column(String)
        author = Column(String)

    return Book
