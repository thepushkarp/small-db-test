
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Setup
engine = create_engine('sqlite:///demo.db', echo=True)
Base = declarative_base()

# Simplified Book Model
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Session Setup
Session = sessionmaker(bind=engine)
session = Session()

# Function: Add a Book
def add_book(title, author):
    new_book = Book(title=title, author=author)
    session.add(new_book)
    session.commit()
    return f"Book '{title}' by {author} added!"

# Function: Get all Books
def get_books():
    books = session.query(Book).all()
    return books

# Demo Execution
if __name__ == "__main__":
    print(add_book("1984", "George Orwell"))
    print(add_book("To Kill a Mockingbird", "Harper Lee"))
    
    for book in get_books():
        print(f"{book.id}: {book.title} by {book.author}")
