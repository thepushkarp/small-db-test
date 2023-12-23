#from sqlalchemy.orm import Session, sessionmaker
#from sqlalchemy import Column, Integer, String, create_engine
#from typing import Generator
#
#from app import *
#
#import pytest
#from sqlalchemy.ext.declarative import declarative_base
#
#Base = declarative_base()
#
#
#class Book(Base):
#    __tablename__ = "books"
#
#    id = Column(Integer, primary_key=True)
#    title = Column(String)
#    author = Column(String)
#
#
#DATABASE_URL = (
#    "postgresql://postgres:root@host.docker.internal:5432/code_robotics_1703325463224"
#)
#engine = create_engine(DATABASE_URL)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#Base.metadata.create_all(bind=engine)
#
#
#@pytest.fixture(scope="module")
#def db_session() -> Generator:
#    session = SessionLocal()
#    try:
#        yield session
#    finally:
#        session.close()
#
#
#def test_get_books(db_session):
#    books = get_books(db_session)
#    assert books is not None
#