from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Assuming the MongoClient is already connected to the 'books_db' and the collection is 'books'
client = MongoClient()
db = client['books_db']
collection = db['books']

# Assuming that the client and db are set according to your MongoDB server and database settings.
client = MongoClient('localhost', 27017)
db = client['your_database']  # Replace 'your_database' with your actual database name
books_collection = db.books  # Replace 'books' with your actual collection name where books will be stored

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)


# Function: Get all Books using pymongo
def get_books():
    books = list(collection.find({}))
    return books

Session = sessionmaker(bind=engine)
session = Session()


def add_book(title, author):
    new_book = {"title": title, "author": author}
    result = books_collection.insert_one(new_book)
    if result.inserted_id:
        return f"Book '{title}' by {author} added!"
    else:
        return "An error occurred while adding the book."

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
