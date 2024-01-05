from typing import Optional

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'username', 'password', 'host', and 'dbname' with your PostgreSQL credentials
DATABASE_URI = "postgresql://username:password@host/dbname"

Base = declarative_base()


# Simplified Book Model
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # Assuming max length 255
    author = Column(String(255), nullable=False)  # Assuming max length 255


def create_db_engine():
    return create_engine(DATABASE_URI, echo=True)

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


# Function: Get all Books
def get_books(session) -> list[Book]:
    try:
        books = session.query(Book).all()
        return books
    except SQLAlchemyError as e:
        print(f"Error: {e}")
        return []


# Demo Execution
if __name__ == "__main__":
    engine = create_db_engine()

    # Create tables
    Base.metadata.create_all(engine)

    # Session Setup
    Session = sessionmaker(bind=engine)
    session = Session()

    print(add_book(session, "The Hobbit", "J.R.R. Tolkien"))
    print(add_book(session, "The Fellowship of the Ring", "J.R.R. Tolkien"))
    print(add_book(session, "The Two Towers", "J.R.R. Tolkien"))

    for book in get_books(session):
        print(f"{book.id}: {book.title} by {book.author}")
