#from sqlalchemy.exc import SQLAlchemyError
#
#import pytest
#
#from app import *
#from pytest import raises as pytest_raises
#from sqlalchemy.engine.base import Engine
#from unittest.mock import MagicMock, patch
#
#from pytest import monkeypatch
#
#
## Test if function `create_db_engine` does not raise any errors when called
#def test_create_db_engine_no_errors():
#    with patch("sqlalchemy.create_engine") as mock_create_engine:
#        mock_create_engine.return_value = MagicMock(spec=Engine)
#        engine = create_db_engine()
#        assert engine is not None
#
#
## Test to ensure that `create_db_engine` creates an instance of SQLAlchemy Engine
#def test_create_db_engine_instance():
#    with patch("sqlalchemy.create_engine") as mock_create_engine:
#        mock_create_engine.return_value = MagicMock(spec=Engine)
#        engine = create_db_engine()
#        assert isinstance(engine, Engine)
#
#
## Test if `create_db_engine` uses the correct DATABASE_URI
#def test_create_db_engine_uses_correct_uri(monkeypatch):
#    expected_uri = "sqlite:///:memory:"
#    monkeypatch.setattr("app.DATABASE_URI", expected_uri)
#    with patch("sqlalchemy.create_engine") as mock_create_engine:
#        mock_create_engine.return_value = MagicMock(spec=Engine)
#        create_db_engine()
#        mock_create_engine.assert_called_with(expected_uri, echo=True)
#
#
## Test on failure when `create_db_engine` encounters a SQLAlchemyError
#def test_create_db_engine_handles_sqlalchemyerror():
#    with patch("sqlalchemy.create_engine") as mock_create_engine:
#        mock_create_engine.side_effect = SQLAlchemyError("Error in creating engine")
#        with pytest.raises(SQLAlchemyError):
#            create_db_engine()
#
#
## Necessary imports for mock and monkeypatch to work inside pytest
#from unittest.mock import patch
#