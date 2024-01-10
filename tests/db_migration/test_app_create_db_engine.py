from sqlalchemy import create_engine
import pytest
from app import *
from app import create_db_engine


import pytest
from sqlalchemy.engine import Engine


# Test to ensure that the create_db_engine function does not throw errors and return a valid engine object.
def test_create_db_engine_no_errors():
    engine = create_db_engine()
    assert isinstance(
        engine, Engine
    ), "create_db_engine should return an engine instance"


# Edge case test: Ensure the function returns an Engine even if echo parameter changes
def test_create_db_engine_echo_parameter(monkeypatch):
    # Set up a valid DATABASE_URI for testing
    database_uri = "sqlite:///test.db"
    monkeypatch.setenv("DATABASE_URI", database_uri)

    # Call function with monkeypatched environment
    engine = create_db_engine()
    assert isinstance(
        engine, Engine
    ), "Even with echo=True, should return an Engine instance"
