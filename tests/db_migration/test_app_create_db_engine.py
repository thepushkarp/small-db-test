from sqlalchemy import create_engine
from app import create_db_engine
import pytest
from app import *


def test_create_db_engine_no_errors():
    """
    Test for making sure `create_db_engine()` doesn't throw any exceptions and returns some non-null value.
    This test will fail if the function throws an exception or the return value is None.
    """
    try:
        engine = create_db_engine()
        assert engine is not None
    except Exception:
        pytest.fail("create_db_engine() raised Exception unexpectedly!")
