import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.db import engine, SessionLocal, Base
from app.models import Product, Sale, Inventory

def seed_data():
    # 1. Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # 2. Open a session
    session: Session = SessionLocal()

    try:
        # 3. (Optional) Clear existing data
        session.query(Sale).delete()
        session.query(Inventory).delete()
        session.query(Product).delete()
        session.commit()

        # 4. Create sample products
        categories = ["Electronics", "Books", "Clothing", "Home", "Sports"]
        products = []
        for i in range(1, 11):
            p = Product(
                name=f"Product {i}",
                category=random.choice(categories),
                price=round(random.uniform(10, 500), 2)
            )
            session.add(p)
            products.append(p)
        session.commit()

        # 5. Seed inventory for each product
        for p in products:
            inv = Inventory(
                product_id=p.id,
                stock_level=random.randint(20, 100)
            )
            session.add(inv)
        session.commit()

        # 6. Generate random sales over the past year
        today = datetime.utcnow()
        for _ in range(50):  # 50 random sales
            prod = random.choice(products)
            # random date within last 365 days
            days_ago = random.randint(0, 365)
            sale_date = today - timedelta(days=days_ago)
            quantity = random.randint(1, 5)
            sale = Sale(
                product_id=prod.id,
                quantity=quantity,
                sale_date=sale_date,
                revenue=round(prod.price * quantity, 2)
            )
            session.add(sale)
        session.commit()

        print("✅ Demo data seeded successfully!")
    finally:
        session.close()


if __name__ == "__main__":
    seed_data()
