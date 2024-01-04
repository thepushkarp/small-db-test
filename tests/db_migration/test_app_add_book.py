import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app import *

# Engine creation using the provided database string
engine = create_engine(
    "postgresql://postgres:root@host.docker.internal:5432/code_robotics_1703325463224"
)

Session = sessionmaker(bind=engine)
session = Session()


@pytest.fixture
def book_data():
    return {"title": "Test Book", "author": "Test Author"}


def test_add_book(book_data):
    response = add_book(**book_data)
    assert response is not None
