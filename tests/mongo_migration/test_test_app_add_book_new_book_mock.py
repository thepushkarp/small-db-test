
from tests.mongo_migration.test_test_app_add_book_new_book_mock import *

import pytest
from app import Book


from unittest.mock import Mock
from unittest.mock import Mock


@pytest.fixture
def mock_new_book():
    return Mock(spec=Book)


def test_new_book_mock(mock_new_book):
    assert mock_new_book is not None
