from typing import Optional

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from typing import Optional, List
from bson.objectid import ObjectId
from pymongo.collection import Collection

# Replace this with your actual MongoDB connection string
DATABASE_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "library"  # Replace with your database name


# Function: Get all Books
def get_books(collection: Collection) -> List[dict]:
    try:
        # Find all documents in the collection without any filter (empty query)
        books_cursor = collection.find({})
        
        # Convert the cursor to a list of dictionaries (representing books)
        books = list(books_cursor)
        
        # Return the list of books
        return books
    except Exception as e:  # Catch a more general exception since we're not using SQLAlchemy
        print(f"Error: {e}")
        return []


def add_book(collection: Collection, title: str, author: str) -> Optional[dict]:
    try:
        new_book_id = collection.insert_one({'title': title, 'author': author}).inserted_id
        new_book = collection.find_one({'_id': new_book_id})
        return new_book
    except Exception as e:
        print(f"Error: {e}")
        return None
COLLECTION_NAME = "books"  # Replace with your collection name

DATABASE_URI = "postgresql://username:password@host/dbname"

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # Assuming max length 255
    author = Column(String(255), nullable=False)  # Assuming max length 255


def create_db_engine():
    client = MongoClient(DATABASE_URI)
    db = client[DATABASE_NAME]
    return db


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
