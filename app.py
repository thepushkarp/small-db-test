from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
# Assuming MongoClient has been imported and 'MongoClient' instance is available
client = MongoClient('localhost', 27017)  # Replace with your connection string if needed
db = client.your_database  # Replace 'your_database' with your actual database name
books_collection = db.your_collection  # Replace 'your_collection' with your actual collection name

# Assuming there is an existing MongoClient connection
# The 'client' should be initialized elsewhere in your application
client = MongoClient('mongodb://localhost:27017/')
db = client.your_database_name  # Replace with your actual database name
books_collection = db.books  # Assumed collection name is 'books'

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)


# Function: Get all Books
def get_books():
    books_cursor = books_collection.find()
    books = list(books_cursor)
    return books

Session = sessionmaker(bind=engine)
session = Session()


# Function: Add a Book using pymongo
def add_book(title, author):
    new_book = {"title": title, "author": author}
    result = books_collection.insert_one(new_book)
    return f"Book '{title}' by {author} added!"

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
