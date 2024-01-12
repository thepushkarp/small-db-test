from pymongo import MongoClient


import pytest

from tests.mongo_migration.test_test_app_add_book_db import *
import pytest


def db():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["test_db"]
    yield db

    client.close()


def test_db_execution():
    db_conn = db()
    assert db_conn is not None


def test_db_closing():
    db_conn = db()
    db_conn.close()
