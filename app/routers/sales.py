from typing import List, Optional
from datetime import datetime
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.SaleRead])
def read_sales(
    start: Optional[datetime] = Query(None, description="start datetime"),
    end:   Optional[datetime] = Query(None, description="end datetime"),
    product_id: Optional[int]   = Query(None),
    category:   Optional[str]   = Query(None),
    db: Session = Depends(get_db)
):
    return crud.get_sales(db, start, end, product_id, category)

@router.get("/summary", response_model=List[schemas.SalesSummaryItem])
def sales_summary(
    start: Optional[datetime] = Query(None, description="start datetime"),
    end:   Optional[datetime] = Query(None, description="end datetime"),
    db: Session = Depends(get_db)
):
    return crud.get_sales_summary(db, start, end)
