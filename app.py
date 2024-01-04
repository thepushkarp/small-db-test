from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Set up the MongoDB client and define the database and collection
client = MongoClient('localhost', 27017)  # You can also provide the MongoDB URI
db = client['books_database']  # 'books_database' is an example database name
books_collection = db['books']  # 'books' is an example collection name

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)


def get_books():
    # Assuming the MongoDB database and collection names are 'library' and 'books' respectively.
    # Modify these as necessary for your application.
    db = MongoClient()['library']
    books_collection = db['books']
    
    books = list(books_collection.find())
    return books

Session = sessionmaker(bind=engine)
session = Session()


# Function: Add a Book
def add_book(title, author):
    new_book = {"title": title, "author": author}
    result = books_collection.insert_one(new_book)
    if result.acknowledged:
        return f"Book '{title}' by {author} added!"
    else:
        return "Failed to add book."

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
