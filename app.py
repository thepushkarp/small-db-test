from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Set up the connection to the database (replace with your actual connection URI)
client = MongoClient("mongodb://localhost:27017/")
# Access the specific database
db = client["books_database"]
# Access the specific collection within the database (equivalent to a table)
books_collection = db["books"]

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)

# Since we cannot import MongoClient, we assume it has been imported previously
# and a MongoDB client has been set up similar to how the SQLAlchemy session was set up.

# Function: Get all Books
def get_books():
    # Assuming 'db' is the database and 'books_collection' is the collection name
    books_cursor = db.books_collection.find({})
    books = list(books_cursor)
    return books

Session = sessionmaker(bind=engine)
session = Session()


# Function: Add a Book
def add_book(title, author):
    new_book = {"title": title, "author": author}
    result = books_collection.insert_one(new_book)
    # You can capture the result to do additional logic or error handling
    if result.acknowledged:
        return f"Book '{title}' by {author} added!"
    else:
        return "An error occurred while adding the book."

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
