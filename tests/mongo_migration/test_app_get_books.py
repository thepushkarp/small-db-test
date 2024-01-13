import pytest

from app import *
from sqlalchemy.orm import Session, sessionmaker


from sqlalchemy import create_engine

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
import pymongo

# Adjust this as per your database and collection requirements
myclient = pymongo.MongoClient('mongodb://root:example@localhost:27017/')
mydb = myclient["code_robotics_1704453498046"]  # The database
books_col = mydb["books"]  # The books collection



@pytest.fixture(scope="module")
def db_engine():
    engine = create_engine(
        "postgresql://refactorybot:22r)pGKLcaeP@refactory.cluster-cw4q9y97boua.us-east-1.rds.amazonaws.com:5432/code_robotics_1704453498046"
    )
    return engine


@pytest.fixture(scope="module")
def db_session():
    yield books_col
    # Optional: Cleanup after tests, if necessary
    # books_col.delete_many({})




def test_get_books_without_errors(db_session: Session):
    """
    Test that the get_books function does not throw any errors when called.
    """
    assert (
        get_books(db_session) is not None
    ), "get_books() should return a result, not None."


def test_get_books_returns_list(db_session: Session):
    """
    Test that get_books returns a list.
    """
    books = get_books(db_session)
    assert isinstance(books, list), "get_books() should return a list."


def test_get_books_empty_session(db_session: Session):
    """
    Test get_books on an empty session.
    """
    books = get_books(db_session)
    assert (
        books == []
    ), "get_books() should return an empty list when there are no books."
