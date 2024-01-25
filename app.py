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
    # Since a specific URI name was not provided, assuming DATABASE_URI is in scope.
    client = MongoClient(DATABASE_URI)  # DATABASE_URI should be defined in scope
    return client.get_database()  # Assuming the DATABASE_URI includes the db name

def add_book(mongo_client, title: str, author: str) -> Optional[dict]:
    try:
        db = mongo_client["book_database"]
        books_collection = db["books"]
        new_book_data = {"title": title, "author": author}
        result = books_collection.insert_one(new_book_data)
        # Since MongoDB does not return the complete book object on insertion
        # we recreate the data with the generated _id to return to the caller.
        new_book_data['_id'] = result.inserted_id
        return new_book_data
    except Exception as e:
        print(f"Error: {e}")
        return None


# Function: Get all Books
def get_books(mongo_client) -> list:
    try:
        book_collection = mongo_client['library']['books']
        books = list(book_collection.find({}, {'_id': False}))
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
