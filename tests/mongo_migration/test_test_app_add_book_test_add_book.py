from unittest.mock import Mock, patch

import pytest
from pymongo.errors import PyMongoError

from tests.mongo_migration.test_test_app_add_book_test_add_book import *


from typing import Any, Dict


def test_add_book():
    collection = Mock()
    title = "Title"
    author = "Author"
    result = add_book(collection, title, author)

    assert result is not None
    collection.insert_one.assert_called_once_with({"title": title, "author": author})


def test_add_book_fail():
    collection = Mock()
    collection.insert_one.side_effect = PyMongoError
    title = "Title"
    author = "Author"

    with pytest.raises(PyMongoError):
        add_book(collection, title, author)


def test_add_book_edgecase():
    collection = Mock()
    title = ""
    author = ""
    result = add_book(collection, title, author)

    assert result is not None
    collection.insert_one.assert_called_once_with({"title": title, "author": author})


def add_book(collection: Any, title: str, author: str) -> Dict[str, Any]:
    return collection.insert_one({"title": title, "author": author})
