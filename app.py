from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Assuming 'books' is the MongoDB collection we'll be working with
# You would have set your MongoDB URI and client somewhere in the code
# For example:
# client = MongoClient("mongodb_uri")
# db = client['database_name']
# books_collection = db['books']

def add_book(title, author):
    new_book = {'title': title, 'author': author}
    result = books_collection.insert_one(new_book)
    if result.inserted_id:
        return f"Book '{title}' by {author} added!"
    else:
        return "There was an error adding the book."

# Function: Get all Books using pymongo
def get_books():
    books_cursor = books_collection.find({})
    return list(books_cursor)

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
