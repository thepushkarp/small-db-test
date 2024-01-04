from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# You should configure these settings accordingly
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
books_collection = db['books']

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)

# Since the pymongo part is not provided, we will assume that there is a MongoDB
# database and collection already set up for use. The code below assumes that
# the MongoDB client, database, and collection are already initialized and made
# accessible within the same scope as this function.

def get_books():
    # Assuming 'books_collection' is the MongoDB collection where books are stored
    books_cursor = books_collection.find({})
    
    # Convert the cursor to a list of dictionaries (if needed in that format)
    books = list(books_cursor)
    
    return books

Session = sessionmaker(bind=engine)
session = Session()


def add_book(title, author):
    new_book = {"title": title, "author": author}
    result = books_collection.insert_one(new_book)
    return f"Book '{title}' by {author} added!"

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
