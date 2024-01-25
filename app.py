from typing import Optional

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import PyMongoError

DATABASE_URI = "postgresql://username:password@host/dbname"

Base = declarative_base()

def get_books(collection: Collection) -> list:
    try:
        books_cursor = collection.find({})
        return list(books_cursor)
    except PyMongoError as e:
        print(f"Error: {e}")
        return []


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # Assuming max length 255
    author = Column(String(255), nullable=False)  # Assuming max length 255


def create_db_engine():
    client = MongoClient(DATABASE_URI)
    return client.get_database()


# Function: Add a Book
def add_book(collection: Collection, title: str, author: str) -> Optional[dict]:
    try:
        new_book = {"title": title, "author": author}
        result = collection.insert_one(new_book)
        new_book["_id"] = result.inserted_id  # Include the new id in the returned document
        return new_book
    except PyMongoError as e:
        print(f"Error: {e}")
        return None


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
