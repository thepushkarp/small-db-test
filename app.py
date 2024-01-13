from typing import Optional

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from typing import List, Optional
from pymongo.errors import PyMongoError

DATABASE_URI = "postgresql://username:password@host/dbname"

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # Assuming max length 255
    author = Column(String(255), nullable=False)  # Assuming max length 255


def create_db_engine():
    return MongoClient(DATABASE_URI)

# Function: Add a Book
def add_book(collection, title: str, author: str) -> Optional[dict]:
    try:
        new_book = {'title': title, 'author': author}
        collection.insert_one(new_book)
        return new_book
    except Exception as e:
        print(f"Error: {e}")
        return None



def get_books(collection) -> List[Optional[dict]]:
    try:
        books = list(collection.find())
        return books
    except PyMongoError as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    engine = create_db_engine()

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    print(add_book(session, "The Hobbit", "J.R.R. Tolkien"))
    print(add_book(session, "The Fellowship of the Ring", "J.R.R. Tolkien"))
    print(add_book(session, "The Two Towers", "J.R.R. Tolkien"))

    for book in get_books(session):
        print(f"{book.id}: {book.title} by {book.author}")
