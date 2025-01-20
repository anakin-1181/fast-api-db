from fastapi import HTTPException
from sqlalchemy.orm import Session

from fast_api_db.model.model import Item


class ItemCRUD:
    # Create
    @staticmethod
    def create_item(db: Session, item_id: int, item_name: str):
        try:
            item = Item(item_id=item_id, item_name=item_name)
            db.add(item)
            db.commit()
            db.refresh(item)
            return item
        except ValueError:
            db.rollback()
            raise HTTPException(
                status_code="404", detail="Item cannot be created."
            )

    # Read
    @staticmethod
    def get_item(db: Session, item_id: int):
        try:
            item = (
                db.query(Item).filter(Item.item_id == item_id).first()
            )
            return item
        except ValueError:
            raise HTTPException(
                status_code="404",
                detail=f"Item with id:{item_id} cannot be found.",
            )

    # Update
    # potential: two error messages (cannot find item_id) (parameters error)
    @staticmethod
    def update_item(db: Session, item_id: int, item_name: str):
        try:
            db.query(Item).filter(Item.item_id == item_id).update(
                {"item_name": item_name}
            )
            db.commit()
            return (
                db.query(Item).filter(Item.item_id == item_id).first()
            )
        except ValueError:
            raise HTTPException(
                status_code="404",
                detail=f"Item with id:{item_id} cannot be updated.",
            )

    # Delete
    @staticmethod
    def delete_item(db: Session, item_id: int):
        try:
            item = (
                db.query(Item).filter(Item.item_id == item_id).first()
            )
            db.delete(item)
            db.commit()
            return item
        except ValueError:
            raise HTTPException(
                status_code="404",
                detail=f"Item with id:{item_id} cannot be deleted.",
            )
