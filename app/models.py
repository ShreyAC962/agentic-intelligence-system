from sqlalchemy import Column, Integer, String, Text
from app.db import engine
# To create a base class for all database models(tables)
from sqlalchemy.orm import declarative_base

Base = declarative_base() # Map python classes to database tables

class Document(Base):
    __tablename__ = "documents"
    # Primary key column
    id = Column(Integer, primary_key=True)
    # Column to stire large text(like documents, articles)
    content = Column(Text)
    doc_metadata = Column(String)