from sqlalchemy import Column, Integer, String, create_engine
from typing import Optional
from sqlalchemy.orm import Session, declarative_base, sessionmaker


from typing import Optional

from sqlalchemy import Column, Integer, String, create_engine

import pytest
from app import *
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from unittest.mock import Mock, patch

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


def test_add_book_happy_path(db):
    result = add_book(db, "Title", "Author")
    assert isinstance(result, object)
    assert result is not None


def test_add_book_failure(db):
    with patch.object(
        db, "add", side_effect=SQLAlchemyError("Random error")
    ), patch.object(db, "rollback"), patch("builtins.print") as mock_print:
        result = add_book(db, "Title", "Author")
        assert result is None
        mock_print.assert_called_with("Error: Random error")

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author = Column(String(50))


# Function: Add a Book
def add_book(session, title: str, author: str) -> Optional[Book]:
    try:
        new_book = Book(title=title, author=author)
        session.add(new_book)
        session.commit()
        return new_book
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error: {e}")
        return None
