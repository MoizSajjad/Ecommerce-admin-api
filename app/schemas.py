from datetime import datetime 
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class ProductBase(BaseModel):
    name: str
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    product_id: int
    quantity: int
    sale_date: datetime

class SaleRead(SaleBase):
    id: int
    revenue: float

    class Config:
        orm_mode = True

class SalesSummaryItem(BaseModel):
    date: date
    total_quantity: int
    total_revenue: float

class RevenueTotal(BaseModel):
    total_revenue: float

class RevenueCompare(BaseModel):
    period1_revenue: float
    period2_revenue: float

class InventoryBase(BaseModel):
    product_id: int
    stock_level: int

class InventoryRead(InventoryBase):
    id: int
    last_updated: datetime

    class Config:
        orm_mode = True

class InventoryUpdate(BaseModel):
    stock_level: int
