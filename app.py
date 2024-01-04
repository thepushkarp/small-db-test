from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymongo
from pymongo import MongoClient

# Database details
client = MongoClient("localhost", 27017)
db = client["bookstore"] # Replace with your database name

# assuming that you have a "myDatabase" MongoDB and a "books" collection on it
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myDatabase"]
mycol = mydb["books"]

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
    books = db['books'].find()  # Replace 'books' with your MongoDB collection name
    return list(books)

Session = sessionmaker(bind=engine)
session = Session()


def add_book(title, author):
    new_book = { "title": title, "author": author }
    mycol.insert_one(new_book)
    return f"Book '{title}' by {author} added!"

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
