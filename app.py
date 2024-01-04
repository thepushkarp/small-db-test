from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient

# Create a client
client = MongoClient('localhost', 27017)

#Access the 'library' database and 'books' collection
db = client['library']
books = db['books']

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
    client = MongoClient('localhost', 27017)
    db = client['database_name']  # replace with your database name
    collection = db['collection_name']  # replace with your collection name
    books = list(collection.find())
    return books

Session = sessionmaker(bind=engine)
session = Session()


def add_book(title, author):
    new_book = {'title': title, 'author': author}
    books.insert_one(new_book)
    return f"Book '{title}' by {author} added!"

if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
