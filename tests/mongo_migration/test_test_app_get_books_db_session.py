
from tests.mongo_migration.test_test_app_get_books_db_session import *
from pymongo import MongoClient

import pytest
from unittest.mock import patch
from unittest.mock import MagicMock, patch


from typing import Generator
from typing import Generator


@pytest.fixture
def mock_db_session() -> Generator:
    with patch.object(MongoClient, "__init__", return_value=None):
        mock_client = MongoClient()
        mock_client.mydatabase = MagicMock()

        yield mock_client


def test_db_session(mock_db_session: MongoClient) -> None:
    assert mock_db_session is not None
