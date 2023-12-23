from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Assuming the MongoClient is connecting to the local MongoDB instance on the default port
client = MongoClient('localhost', 27017)

# Get a reference to the database and collection
db = client['your_database_name']  # Replace with your actual database name
books_collection = db['books']

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)

# Assuming MongoClient has already been imported and configured elsewhere in your code.

def get_books():
    # Assuming the MongoDB client has already been created and is named 'client'.
    # Also assuming a defined database name 'your_database' and collection name 'books_collection'.
    db = client.your_database
    books_collection = db.books_collection

    # Retrieve all books from the collection
    books_cursor = books_collection.find({})
    
    # Convert the Cursor to a list of dicts (which represent your books)
    books = list(books_cursor)

    return books

Session = sessionmaker(bind=engine)
session = Session()


# Function: Add a Book using pymongo
def add_book(title, author):
    new_book = {"title": title, "author": author}
    books_collection.insert_one(new_book)
    return f"Book '{title}' by {author} added!"

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
