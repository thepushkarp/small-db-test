from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymongo
from pymongo import MongoClient

# Assuming that you have a running MongoDB instance on the default host and port
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["library"]  # 'library' is the name of the database
books_collection = db["books"]  # 'books' is the name of the collection

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)


def get_books():
    client = MongoClient()  # You might need to specify host and port
    db = client['your_database_name']  # Replace with your database name
    books_collection = db['books']  # Replace with your collection name
    books = list(books_collection.find({}))
    return books

Session = sessionmaker(bind=engine)
session = Session()


# Function: Add a Book in MongoDB
def add_book(title, author):
    new_book = {"title": title, "author": author}
    result = books_collection.insert_one(new_book)
    return f"Book '{title}' by {author} added! ID: {result.inserted_id}"

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
