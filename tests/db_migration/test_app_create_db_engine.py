#from app import *
#from unittest.mock import MagicMock, patch
#
#import pytest
#
#
#from unittest.mock import MagicMock, patch
#
## Tests for create_db_engine
#
#
#def test_create_db_engine_no_errors():
#    """Test if create_db_engine function executes without any exceptions."""
#    with patch("sqlalchemy.create_engine", return_value=MagicMock()):
#        from app import create_db_engine
#
#        assert create_db_engine() is not None
#
#
#def test_create_db_engine_returns_correct_object_type(mocker):
#    """Test if create_db_engine returns a mock engine instance."""
#    mocked_engine = mocker.MagicMock()
#    mocker.patch("sqlalchemy.create_engine", return_value=mocked_engine)
#    from app import create_db_engine
#
#    engine = create_db_engine()
#    assert engine == mocked_engine
#
#
#def test_create_db_engine_use_database_uri(mocker):
#    """Test if the create_db_engine function is called with correct DATABASE_URI."""
#    mocker.patch("sqlalchemy.create_engine")
#    from app import create_db_engine
#
#    create_db_engine()
#    sqlalchemy.create_engine.assert_called_once()
#
#
#def test_create_db_engine_with_echo_true(mocker):
#    """Test if the create_db_engine function is called with echo set to True."""
#    mocker.patch("sqlalchemy.create_engine")
#    from app import create_db_engine
#
#    create_db_engine()
#    _, kwargs = sqlalchemy.create_engine.call_args
#    assert kwargs.get("echo") == True
#