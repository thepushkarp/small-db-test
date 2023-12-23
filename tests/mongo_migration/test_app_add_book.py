import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app import *
from pymongo import MongoClient

engine = create_engine(
    "postgresql://postgres:root@host.docker.internal:5432/code_robotics_1703325463224"
)

Session = sessionmaker(bind=engine)
session = Session()


@pytest.fixture
def book_data():
    return {"title": "Test Book", "author": "Test Author"}


#assuming mongodb connection credentials and database are already set globally

def test_add_book(book_data):
    client = MongoClient() #replace with actual credentials if required
  
    #replace 'test_db' and 'books' with actual db name and collection
    db = client['test_db']
    collection = db['books']

    response = add_book(collection, **book_data)
    assert response.inserted_id is not None

@pytest.fixture
def mongo_client():
    return MongoClient("mongodb://localhost:27017")

@pytest.fixture
def test_db(mongo_client):
    return mongo_client["book_test_db"]

@pytest.fixture
def test_books_collection(test_db):
    return test_db["books"]
