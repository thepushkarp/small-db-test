import pytest
from sqlalchemy.orm import sessionmaker
from app import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from pymongo import MongoClient
from app import add_book
import pymongo



@pytest.fixture(scope="module")
def engine():
    client = MongoClient("mongodb://localhost:27017")
    db = client["code_robotics_1703825513833"]
    return db


@pytest.fixture(scope="module")
def session():
    client = MongoClient('localhost', 27017)
    db = client['test_db']
    return db


def test_add_book_empty_author():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test_database']
    result = db.books.insert_one({"title": "The Hobbit", "author": ""})
    assert result.inserted_id is not None


def test_add_book_non_string_input(db):
    result = add_book(db, 1234, "J.R.R. Tolkien")
    assert result is not None
    result = add_book(db, "The Hobbit", 1234)
    assert result is not None


def test_add_book_empty_title(session):
    client = MongoClient(host="mongo-host", port=27017)
    db = client['test-database']
    result = db.books.insert_one({"title": "", "author": "J.R.R. Tolkien"})
    assert result.inserted_id is not None


def test_add_book(client):
    result = add_book(client, "The Hobbit", "J.R.R. Tolkien")
    assert result is not None
