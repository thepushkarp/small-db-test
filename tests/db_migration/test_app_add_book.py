import pytest
from sqlalchemy.orm import sessionmaker
from app import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# Define fixture for DB Engine
@pytest.fixture(scope="module")
def engine():
    engine = create_engine(
        "postgresql://postgres:root@localhost:5432/code_robotics_1703825513833",
        echo=True,
    )
    return engine


# Define fixture for DB Session
@pytest.fixture(scope="module")
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def test_add_book(session):
    result = add_book("The Hobbit", "J.R.R. Tolkien")
    assert result is not None


def test_add_book_empty_title(session):
    result = add_book("", "J.R.R. Tolkien")
    assert result is not None


def test_add_book_empty_author(session):
    result = add_book("The Hobbit", "")
    assert result is not None


def test_add_book_non_string_input(session):
    result = add_book(1234, "J.R.R. Tolkien")
    assert result is not None
    result = add_book("The Hobbit", 1234)
    assert result is not None
