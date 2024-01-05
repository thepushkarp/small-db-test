from typing import Optional

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from typing import Optional, List
from typing import Optional, Dict

# Assuming DATABASE_URI is a MongoDB connection string, e.g. mongodb://localhost:27017
DATABASE_URI = "your_mongodb_connection_string"


# Function: Get all Books
def get_books(db: Database) -> List[Dict]:
    try:
        books_collection: Collection = db.books  # Assuming the collection is named 'books'
        books_cursor = books_collection.find()
        books = list(books_cursor)
        return books
    except Exception as e:
        print(f"Error: {e}")
        return []


# Assuming that 'Book' in MongoDB corresponds to a dictionary-like object.

def add_book(db: Database, title: str, author: str) -> Optional[Dict]:
    try:
        books_collection = db['books']  # The name of the collection in MongoDB
        new_book_data = {'title': title, 'author': author}
        result = books_collection.insert_one(new_book_data)
        # The inserted_id is the ID of the new document inserted into the collection
        new_book_data['_id'] = result.inserted_id
        return new_book_data
    except Exception as e:
        print(f"Error: {e}")
        return None
DATABASE_NAME = "your_database_name"
COLLECTION_NAME = "books"

DATABASE_URI = "postgresql://username:password@host/dbname"

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # Assuming max length 255
    author = Column(String(255), nullable=False)  # Assuming max length 255


def create_db_engine() -> MongoClient:
    """
    Create a connection to the MongoDB instance.
    """
    client = MongoClient(DATABASE_URI)
    return client


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
