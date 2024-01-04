from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Assuming there's an existing MongoClient connection named 'client',
# Replace 'your_db_name' with the actual name of your database
db = client['your_db_name']
books_collection = db.books

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def get_books():
    client = MongoClient('localhost', 27017)  # Connect to the MongoDB server; adjust the host and port as necessary
    db = client['your_database_name']         # Replace with your actual database name
    books_collection = db.books               # Replace with your actual collection name

    books = list(books_collection.find({}))  # Using find({}) to get all documents in the collection as a list
    return books
session = Session()


def add_book(title, author):
    new_book = {"title": title, "author": author}
    result = books_collection.insert_one(new_book)
    if result.acknowledged:
        return f"Book '{title}' by {author} added!"
    else:
        return "There was an error adding the book."

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
