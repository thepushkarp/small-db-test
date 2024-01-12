from app import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
import pytest

DATABASE_URI = "sqlite:///:memory:"


def test_create_db_engine_no_errors():
    """
    Test for making sure `create_db_engine()` doesn't throw any exceptions and creates an instance of `Engine` class.
    This test is designed to fail if the function throws an exception or the returned object is not an instance of `Engine`.
    """
    try:
        engine = create_db_engine()
        assert engine is not None
        assert isinstance(engine, create_engine(DATABASE_URI, echo=True).__class__)
    except SQLAlchemyError:
        pytest.fail("create_db_engine() raised SQLAlchemyError unexpectedly!")
