from fastapi import FastAPI
from sqlalchemy.orm import Session

from fast_api_db.crud.item import ItemCRUD
from fast_api_db.database.connection import SessionLocal
from fast_api_db.model.model import create_table

# from fast_api_db.model.model import Base, Item

app = FastAPI()


# Create
@app.post("/items")
def create_item(db: Session, item_id: int, item_name: str):
    item = ItemCRUD.create_item(
        db=db, item_id=item_id, item_name=item_name
    )
    return item


# Read
@app.get("/items/{item_id}")
def get_item(db: Session, item_id: int):
    item = ItemCRUD.get_item(db=db, item_id=item_id)
    return item


# Update
# @app.put("/items/{item_id}")
# def update_item(db: Session, item_id: int, **kwargs):
#     item = ItemCRUD.update_item(db=db, item_id=item_id, kwargs=kwargs)
#     return item


# Delete
@app.delete("/items/{item_id}")
def delete_item(db: Session, item_id: int):
    item = ItemCRUD.delete_item(db=db, item_id=item_id)
    return item


if __name__ == "__main__":
    db = SessionLocal()
    create_table()
