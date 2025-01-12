from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_table():
    Base.metadata.create_all()


class Item(Base):
    __tablename__ = "item"
    item_id = Column(
        Integer, primary_key=True, nullable=False, unique=True
    )
    item_name = Column(String)
