from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Assuming that 'mydatabase' is the database and 'books' is the collection we're using
db_name = 'mydatabase'
collection_name = 'books'

# Connect to MongoDB
client = MongoClient('localhost', 27017)  # You may need to change this to your MongoDB URI
db = client[db_name]
collection = db[collection_name]

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()


# Assuming 'books' is the name of the collection where books are stored.
# You should replace 'your_database' with the actual name of your database.

# Function: Get all Books
def get_books():
    client = MongoClient()  # Connects to the MongoDB server running on localhost:27017 by default
    db = client.your_database  # Replace 'your_database' with your actual database name
    books_collection = db.books
    books = list(books_collection.find())  # Retrieves all documents from the 'books' collection
    return books

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Function: Add a Book
def add_book(title, author):
    new_book = {
        'title': title,
        'author': author
    }
    collection.insert_one(new_book)
    return f"Book '{title}' by {author} added!"

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
