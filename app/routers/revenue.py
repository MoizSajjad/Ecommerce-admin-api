
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime


from app.db import SessionLocal
from app import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=schemas.RevenueTotal)
def read_total_revenue(
    start: Optional[datetime] = Query(None, description="Start datetime"),
    end:   Optional[datetime] = Query(None, description="End datetime"),
    db: Session = Depends(get_db)
):
    total = crud.get_total_revenue(db, start, end)
    return {"total_revenue": total}

@router.get("/compare", response_model=schemas.RevenueCompare)
def read_revenue_compare(
    start1: datetime = Query(..., description="Start of first period"),
    end1:   datetime = Query(..., description="End of first period"),
    start2: datetime = Query(..., description="Start of second period"),
    end2:   datetime = Query(..., description="End of second period"),
    db: Session = Depends(get_db)
):
    if start1 > end1 or start2 > end2:
        raise HTTPException(400, "Each start must be before its end")
    rev1, rev2 = crud.get_revenue_compare(db, start1, end1, start2, end2)
    return {"period1_revenue": rev1, "period2_revenue": rev2}
