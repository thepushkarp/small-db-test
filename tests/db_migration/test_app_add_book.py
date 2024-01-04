#from sqlalchemy.orm import sessionmaker
#from typing import List
#from sqlalchemy import Session, create_engine, sessionmaker
#
#import pytest
#from app import *
#
#
#def test_add_book_does_not_throw_exception(session: Session):
#    try:
#        assert add_book("book1", "author1", session)
#    except Exception as e:
#        assert False, f"An Exception {str(e)} occurred"
#
#
#def test_add_book_returns_correct_message(session: Session):
#    assert add_book("book1", "author1", session) == "Book 'book1' by author1 added!"
#
#
#def test_add_book_raises_exception_for_none_as_title(session: Session):
#    with pytest.raises(Exception):
#        add_book(None, "author1", session)
#
#
#def test_add_book_raises_exception_for_empty_string_as_title(session: Session):
#    with pytest.raises(Exception):
#        add_book("", "author1", session)
#
#
#@pytest.fixture(scope="module")
#def session():
#    DATABASE_URI = (
#        "postgresql://postgres:root@localhost:5432/code_robotics_1703753379631"
#    )
#    engine = create_engine(DATABASE_URI)
#    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#    session = SessionLocal()
#    return session
#
#
### Import these libraries at top
#import pytest
#