#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, String, create_engine
#from sqlalchemy.orm import Session, sessionmaker
#
#import pytest
#from typing import Generator
#from app import *
#
## setup session
#engine = create_engine(
#    "postgresql://postgres:root@localhost:5432/code_robotics_1703753379631"
#)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
## make a pytest fixture that provides SessionLocal
#@pytest.fixture(scope="function")
#def db_session() -> Generator:
#    session = SessionLocal()
#    try:
#        yield session
#    finally:
#        session.close()
#
#
#@pytest.mark.usefixtures("db_session")
#def test_get_books_no_exception(db_session: Session):
#    try:
#        get_books(db_session)
#    except Exception as e:
#        pytest.fail(f"test_get_books_no_exception failed with error {str(e)}")
#
#
#def test_get_books_return_value(db_session: Session):
#    books = get_books(db_session)
#    assert books is not None
#
#
#def test_get_books_return_type(db_session: Session):
#    books = get_books(db_session)
#    assert isinstance(books, list)
#