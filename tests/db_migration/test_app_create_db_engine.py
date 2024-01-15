
import pytest

from app import *
from unittest.mock import MagicMock, patch

# Since `create_db_engine` function is already in scope, we don't need to import it again


@pytest.fixture
def mock_create_engine():
    with patch("app.create_engine") as mock:
        yield mock


def test_create_db_engine_does_not_return_none(mock_create_engine):
    # Mock return value for `create_engine`
    mock_create_engine.return_value = MagicMock()
    engine = create_db_engine()
    assert engine is not None


def test_create_db_engine_with_mock_db_uri(mock_create_engine):
    # Mock return value for `create_engine`
    mock_create_engine.return_value = MagicMock()
    test_uri = "sqlite:///:memory:"

    with patch("app.DATABASE_URI", new=test_uri):
        engine = create_db_engine()
        # Test if `create_engine` was called with the provided mock URI and echo=True
        mock_create_engine.assert_called_once_with(test_uri, echo=True)
        assert engine is not None


# Other tests can go here


from unittest.mock import MagicMock, patch
