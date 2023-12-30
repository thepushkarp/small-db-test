from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

client = MongoClient()  # Add your connection string if not connecting to default localhost
db = client['books_database']  # Replace 'books_database' with your actual database name
books_collection = db['books']  # Replace 'books' with your actual collection name

engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)


# Assuming the MongoDB collection is named 'books'
# and there's a MongoClient connection already established

def get_books():
    mongo_client = MongoClient()  # connect to the MongoDB server
    db = mongo_client.some_database_name  # replace with your database name
    books_collection = db.books  # 'books' is the collection name
    books = list(books_collection.find())  # retrieve all documents from the collection
    return books

Session = sessionmaker(bind=engine)
session = Session()


# Function: Add a Book
def add_book(title, author):
    new_book = {'title': title, 'author': author}
    result = books_collection.insert_one(new_book)
    return f"Book '{title}' by {author} added!"

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
