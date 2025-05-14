E-commerce Admin API

A FastAPI backend for managing an e-commerce storefront's administrative tasks, including product management, sales tracking, revenue analytics, and inventory control. Uses MySQL for data storage and SQLAlchemy ORM.

Table of Contents

Overview

Features

Tech Stack

Prerequisites

Setup

Clone

Virtual Environment

Install

Environment Variables

Database

Seed Data

Run

API Endpoints

Database Schema

Examples

Project Structure

Contributing

License

Contact

Overview

Provides an admin API for:

Products: create, list

Sales: record, filter, summarize

Revenue: total, compare

Inventory: view, low‑stock filter, update

Automatic table creation on startup and a script to seed demo data.

Features

CRUD for products

Filterable sales queries and daily summaries

Revenue calculation and period comparison

Inventory monitoring and updates

Demo-data seeding script

Tech Stack

Python 3.10+

FastAPI

Uvicorn

SQLAlchemy

PyMySQL

python-dotenv

Prerequisites

MySQL Server 8.0+

Python 3.10+

Git

Setup

Clone

git clone https://github.com/MoizSajjad/Ecommerce-admin-api.git
cd Ecommerce-admin-api

Virtual Environment

python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

Install

pip install -r requirements.txt

Environment Variables

Copy the template:

copy .env.example .env      # Windows
cp .env.example .env        # macOS/Linux

Edit .env and set values:

DB_HOST=localhost
DB_PORT=3306
DB_USER=moiz
DB_PASS=admin1234
DB_NAME=ecommerce

Database

Start MySQL client (Workbench or CLI).

Create database and user:

CREATE DATABASE ecommerce;
CREATE USER 'moiz'@'localhost' IDENTIFIED BY 'admin1234';
GRANT ALL PRIVILEGES ON ecommerce.* TO 'moiz'@'localhost';
FLUSH PRIVILEGES;

Seed Data

python scripts/seed_demo_data.py

Expected: ✅ Demo data seeded successfully!

Run

uvicorn app.main:app --reload

Open docs at http://127.0.0.1:8000/docs

API Endpoints

Products

Method

Path

Description

GET

/products/

List products

POST

/products/

Create a product

Sales

Method

Path

Description

GET

/sales/

List/filter sales

GET

/sales/summary

Daily summaries (quantity & revenue)

Revenue

Method

Path

Description

GET

/revenue/

Total revenue over period

GET

/revenue/compare

Compare two date ranges

Inventory

Method

Path

Description

GET

/inventory/

List inventory, filter low stock

PATCH

/inventory/{product_id}

Update stock level for a product

Database Schema

products (1) ──< sales (*)
products (1) ─── inventory (1)

Examples

List first 5 products:

curl "http://127.0.0.1:8000/products/?limit=5"

Create product:

curl -X POST "http://127.0.0.1:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Widget","category":"Gadgets","price":29.99}'

Project Structure

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

Contributing

Fork repo

Create branch: git checkout -b feature/...

Commit changes

Push and open PR
