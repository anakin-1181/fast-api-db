from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "item"
    item_id = Column(
        Integer, primary_key=True, nullable=False, unique=True
    )
    item_name = Column(String)


class ItemParams(BaseModel):
    item_id: int
    item_name: str
