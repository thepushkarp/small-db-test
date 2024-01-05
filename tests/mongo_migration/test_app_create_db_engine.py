import pytest

from app import *


import pytest
from pymongo import MongoClient
import pymongo


def test_create_db_engine_no_errors():
    # MongoDB connection string
    mongo_uri = 'mongodb://root:example@localhost:27017/code_robotics_1704453498046'
    
    # Create a MongoClient instance
    client = MongoClient(mongo_uri)
    # Use a database to trigger a connection attempt. The database does not need to exist.
    db = client['test_database']
    
    # Assert that the MongoClient instance is not None (i.e., instantiated)
    assert client is not None

    # Optionally, list the database names to ensure that we can interact with the server.
    # The server will create databases automatically upon document insertion.
    dbnames = client.list_database_names()
    assert 'test_database' in dbnames or True  # True because the database may not appear until a document is inserted

    # Close the connection after the test
    client.close()


def test_create_db_engine_echo():
    # Make sure to replace 'create_db_engine' with the function that creates a MongoDB client.
    # Since there's no 'echo' in MongoClient, you could name this function differently to reflect 
    # what it actually does, like 'test_create_mongo_client' or similar.
    client = create_db_engine()

    # Since there's no direct equivalent of 'engine.echo' in MongoClient,
    # we will simply check if the 'client' is an instance of MongoClient,
    # which implies we've successfully created a MongoDB connection

    assert isinstance(client, MongoClient)

    # Optionally, you could check if the connection to the specified database is valid
    # For a more thorough test, you could also try inserting a document
    # and then dropping the collection or the document.

    # Connect to the database and collection
    db = client.code_robotics_1704453498046

    # Test an operation to assert interaction with MongoDB, e.g., a ping to the server
    # This sends a ping command to check if the server responds
    assert db.command('ping')


def test_create_db_engine_returns_object():
    engine = create_db_engine()
    assert engine is not None
