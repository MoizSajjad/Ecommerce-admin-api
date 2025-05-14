from fastapi import FastAPI
from app.db import engine, Base
from app.routers import products, sales, revenue, inventory

# Auto-create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce Admin API")

app.include_router(products.router,    prefix="/products", tags=["products"])
app.include_router(sales.router,       prefix="/sales",    tags=["sales"])
app.include_router(revenue.router,     prefix="/revenue",  tags=["revenue"])
app.include_router(inventory.router,   prefix="/inventory",tags=["inventory"])
