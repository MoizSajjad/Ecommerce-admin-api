
from typing import List, Optional, Tuple
from datetime import datetime
from sqlalchemy import func

from app.models import Sale, Product
from app.schemas import SaleBase
from sqlalchemy.orm import Session
from typing import List

from app.models import Product, Sale, Inventory
from app.schemas import ProductCreate, SaleBase, InventoryUpdate

def get_products(db: Session, skip: int = 0, limit: int = 100) -> List[Product]:
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product_in: ProductCreate) -> Product:
    db_obj = Product(
        name=product_in.name,
        category=product_in.category,
        price=product_in.price
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
def get_sales(
    db,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    product_id: Optional[int] = None,
    category: Optional[str] = None
) -> List[Sale]:
    q = db.query(Sale)
    if start_date:
        q = q.filter(Sale.sale_date >= start_date)
    if end_date:
        q = q.filter(Sale.sale_date <= end_date)
    if product_id:
        q = q.filter(Sale.product_id == product_id)
    if category:
        q = q.join(Product).filter(Product.category == category)
    return q.order_by(Sale.sale_date).all()

def get_sales_summary(
    db,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> List:
    q = (
        db.query(
            func.date(Sale.sale_date).label("date"),
            func.sum(Sale.quantity).label("total_quantity"),
            func.sum(Sale.revenue).label("total_revenue"),
        )
    )
    if start_date:
        q = q.filter(Sale.sale_date >= start_date)
    if end_date:
        q = q.filter(Sale.sale_date <= end_date)
    q = q.group_by(func.date(Sale.sale_date)).order_by(func.date(Sale.sale_date))
    return q.all()
def get_total_revenue(
    db,
    start_date: Optional[datetime] = None,
    end_date:   Optional[datetime] = None
) -> float:
    q = db.query(func.sum(Sale.revenue))
    if start_date:
        q = q.filter(Sale.sale_date >= start_date)
    if end_date:
        q = q.filter(Sale.sale_date <= end_date)
    total = q.scalar() or 0.0
    return float(total)

def get_revenue_compare(
    db,
    start1: datetime, end1: datetime,
    start2: datetime, end2: datetime
) -> Tuple[float, float]:
    rev1 = get_total_revenue(db, start1, end1)
    rev2 = get_total_revenue(db, start2, end2)
    return rev1, rev2

def get_inventory(
    db: Session,
    low_stock_only: bool = False,
    threshold: int = 10
) -> List[Inventory]:
    q = db.query(Inventory)
    if low_stock_only:
        q = q.filter(Inventory.stock_level < threshold)
    return q.all()

def update_inventory(
    db: Session,
    product_id: int,
    new_stock: int
) -> Optional[Inventory]:
    inv = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if not inv:
        return None
    inv.stock_level = new_stock
    db.commit()
    db.refresh(inv)
    return inv