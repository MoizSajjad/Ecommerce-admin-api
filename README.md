# E-commerce Admin API

A FastAPI backend for managing an e-commerce storefront's administrative tasks, including product management, sales tracking, revenue analytics, and inventory control. Uses MySQL for data storage and SQLAlchemy ORM.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Prerequisites](#prerequisites)
5. [Setup](#setup)
   - [Clone](#clone)
   - [Virtual Environment](#virtual-environment)
   - [Install Dependencies](#install-dependencies)
   - [Configure Environment Variables](#configure-environment-variables)
   - [Database Setup](#database-setup)
   - [Seed Demo Data](#seed-demo-data)
   - [Run the Application](#run-the-application)
6. [API Endpoints](#api-endpoints)
7. [Database Schema](#database-schema)
8. [Examples](#examples)
9. [Project Structure](#project-structure)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)

---

## Overview
Provides an admin API for:
- **Products**: create and list products
- **Sales**: record sales, filter, summarize
- **Revenue**: calculate total revenue and compare periods
- **Inventory**: view stock levels, filter low stock, update stock

Automatic table creation on startup and a script to seed demo data.

## Features
- CRUD for products
- Filterable sales queries and daily summaries
- Revenue calculation and period comparison
- Inventory monitoring and updates
- Demo-data seeding script

## Tech Stack
- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- PyMySQL
- python-dotenv

## Prerequisites
- MySQL Server 8.0+
- Python 3.10+
- Git client

## Setup

### Clone
```bash
git clone https://github.com/MoizSajjad/Ecommerce-admin-api.git
cd Ecommerce-admin-api
```

### Virtual Environment
```bash
python -m venv venv
# Windows
.env\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
1. Copy the template:
   ```bash
   cp .env.example .env   # macOS/Linux
   copy .env.example .env # Windows
   ```
2. Edit `.env` and set:
   ```env
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=moiz
   DB_PASS=admin1234
   DB_NAME=ecommerce
   ```

### Database Setup
Run the following in MySQL client:
```sql
CREATE DATABASE ecommerce;
CREATE USER 'moiz'@'localhost' IDENTIFIED BY 'admin1234';
GRANT ALL PRIVILEGES ON ecommerce.* TO 'moiz'@'localhost';
FLUSH PRIVILEGES;
```

### Seed Demo Data
```bash
python scripts/seed_demo_data.py
```
Expected: `✅ Demo data seeded successfully!`

### Run the Application
```bash
uvicorn app.main:app --reload
```
Access docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API Endpoints

### Products
| Method | Path        | Description      |
| ------ | ----------- | ---------------- |
| GET    | `/products/`| List products    |
| POST   | `/products/`| Create product   |

### Sales
| Method | Path             | Description                  |
| ------ | ---------------- | ---------------------------- |
| GET    | `/sales/`        | List/filter sales            |
| GET    | `/sales/summary` | Daily sales quantity/revenue |

### Revenue
| Method | Path                 | Description                     |
| ------ | -------------------- | ------------------------------- |
| GET    | `/revenue/`          | Total revenue over a period     |
| GET    | `/revenue/compare`   | Compare two periods' revenues   |

### Inventory
| Method | Path                         | Description                     |
| ------ | ---------------------------- | ------------------------------- |
| GET    | `/inventory/`                | List inventory, low-stock filter|
| PATCH  | `/inventory/{product_id}`    | Update stock level              |

## Database Schema
```
products (1) ──< sales (*)
products (1) ─── inventory (1)
```

## Examples
```bash
curl "http://127.0.0.1:8000/products/?limit=5"
curl -X POST "http://127.0.0.1:8000/products/" -H "Content-Type: application/json" -d '{"name":"Widget","category":"Gadgets","price":29.99}'
curl "http://127.0.0.1:8000/sales/summary?start=2025-01-01T00:00:00&end=2025-05-01T00:00:00"
```

## Project Structure
```
Ecommerce-admin-api/
├── app/
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
├── scripts/
│   └── seed_demo_data.py
├── .env.example
├── requirements.txt
└── README.md
```

## Contributing
1. Fork the repo  
2. Create a branch (`git checkout -b feature/YourFeature`)  
3. Commit changes  
4. Push and open PR  


