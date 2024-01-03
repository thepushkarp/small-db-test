from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Assuming MongoDB connection details and database are set accordingly
client = MongoClient('localhost', 27017)
db = client['your_database_name']
books_collection = db['books']

# Assuming 'mydatabase' is the name of your database and 'books' is your collection
db_name = 'mylibrary'  # Use appropriate database name
collection_name = 'books'  # Use appropriate collection name

# Connect to MongoDB
# Assuming MongoDB is running on the default host and port
client = MongoClient('localhost', 27017)

# Get the database
db = client[db_name]

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()


# Function: Get all Books
def get_books():
    books = list(books_collection.find())
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
    books_collection = db[collection_name]
    new_book = {
        'title': title,
        'author': author
    }
    result = books_collection.insert_one(new_book)
    if result.inserted_id:
        return f"Book '{title}' by {author} added!"
    else:
        return "Error adding the book."

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
