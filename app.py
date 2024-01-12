from typing import Optional

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
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

# Function: Get all Books
def get_books(client: MongoClient) -> list[dict]:
    try:
        books = list(client.db.books.find())
        return books
    except PyMongoError as e:
        print(f"Error: {e}")
        return []


# Function: Add a Book
def add_book(client: MongoClient, title: str, author: str) -> Optional[dict]:
    try:
        new_book = {"title": title, "author": author}
        db = client['book_database'] # Replace 'book_database' with your database name
        collection = db['book_collection'] # Replace 'book_collection' with your collection name
        result = collection.insert_one(new_book)
        return new_book if result else None
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
