from unittest.mock import Mock, patch

import pytest

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from app import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author = Column(String(50))


@pytest.fixture(scope="module")
def db():
    engine = create_engine("sqlite:///test.db")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


def test_add_book():
    session = Mock()
    title = "Title"
    author = "Author"
    result = add_book(session, title, author)
    assert result is not None
    session.add.assert_called_once_with(result)
    session.commit.assert_called_once()


def test_add_book_exception():
    session = Mock()
    session.add.side_effect = SQLAlchemyError
    title = "Title"
    author = "Author"
    result = add_book(session, title, author)
    assert result is None
    session.add.assert_called_once()
    session.rollback.assert_called_once()


# Necessary imports for the test
from typing import Optional
