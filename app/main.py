from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from fast_api_db.crud.item import ItemCRUD
from fast_api_db.database.connection import SessionLocal
from fast_api_db.model.model import ItemParams

# from fast_api_db.model.model import Base, Item

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Startup route
@app.get("/")
def greet():
    return {"Hello": "World"}


# Create
@app.post("/items")
def create_item(item: ItemParams, db: Session = Depends(get_db)):
    item = ItemCRUD.create_item(
        item_id=item.item_id, item_name=item.item_name, db=db
    )
    return item


# Read
@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = ItemCRUD.get_item(db=db, item_id=item_id)
    return item


# Update
@app.put("/items/{item_id}")
def update_item(item: ItemParams, db: Session = Depends(get_db)):
    item = ItemCRUD.update_item(
        db=db, item_id=item.item_id, item_name=item.item_name
    )
    return item


# # Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = ItemCRUD.delete_item(db=db, item_id=item_id)
    return item
