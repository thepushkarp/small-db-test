from typing import Optional

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

DATABASE_URI = "postgresql://username:password@host/dbname"

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # Assuming max length 255
    author = Column(String(255), nullable=False)  # Assuming max length 255


def create_db_engine():
    client = MongoClient(DATABASE_URI)
    return client.get_database()

def add_book(client: MongoClient, title: str, author: str) -> Optional[dict]:
    try:
        books_collection = client['library']['books']
        result = books_collection.insert_one({
            "title": title,
            "author": author
        })
        new_book = {
            "_id": result.inserted_id,
            "title": title,
            "author": author
        }
        return new_book
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_books(client: MongoClient) -> list[Book]:
    try:
        books_collection = client.db.books  # Assume 'db' is the database name and 'books' is the collection name
        books_cursor = books_collection.find({})
        books = [Book(**book) for book in books_cursor]
        return books
    except Exception as e:
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
