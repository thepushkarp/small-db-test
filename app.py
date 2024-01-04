from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Create a MongoClient object and connect to the MongoDB instance
mongo_client = MongoClient('mongodb://localhost:27017/')  # Replace with the correct connection URI

client = MongoClient('localhost', 27017)  # Connect to the MongoDB server, replace with your own connection details if needed
db = client['mydatabase']  # Replace 'mydatabase' with the actual name of your database
books_collection = db.books  # Replace 'books' with the actual name of your collection where books are stored

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)


def get_books():
    book_collection = mongo_client['database_name']['Book']  # Replace 'database_name' with your actual database name
    books = list(book_collection.find())
    return books

Session = sessionmaker(bind=engine)
session = Session()


# Function: Add a Book
def add_book(title, author):
    new_book = {"title": title, "author": author}
    result = books_collection.insert_one(new_book)
    if result.inserted_id:
        return f"Book '{title}' by {author} added!"
    else:
        return "An error occurred while trying to add the book."

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
