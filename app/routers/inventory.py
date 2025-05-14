from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.db import SessionLocal
from app import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.InventoryRead])
def read_inventory(
    low_stock_only: bool = Query(False, description="Show only items below threshold"),
    threshold:    int  = Query(10,    description="Stock level threshold"),
    db: Session = Depends(get_db)
):
    return crud.get_inventory(db, low_stock_only, threshold)

@router.patch("/{product_id}", response_model=schemas.InventoryRead)
def update_inventory_stock(
    product_id: int,
    inv_update: schemas.InventoryUpdate,
    db: Session = Depends(get_db)
):
    inv = crud.update_inventory(db, product_id, inv_update.stock_level)
    if not inv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory record not found"
        )
    return inv
