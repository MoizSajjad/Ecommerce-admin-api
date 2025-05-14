E-commerce Admin API

A comprehensive FastAPI backend for managing an e-commerce storefront's administrative tasks, including product management, sales tracking, revenue analytics, and inventory control. Backed by MySQL and SQLAlchemy ORM with clear endpoints and demonstration data.

Table of Contents

Project Overview

Features

Tech Stack

Prerequisites

Getting Started

Clone Repository

Set Up Virtual Environment

Install Dependencies

Configure Environment Variables

Database Setup

Seed Demo Data

Run the Application

API Reference

Products

Sales

Revenue

Inventory

Database Schema

Examples

Project Structure

Contributing

License

Contact

Project Overview

This backend API is designed to support administrative operations for an e-commerce platform. It provides endpoints for:

Creating and listing products

Recording and querying sales data

Calculating revenue metrics

Viewing and updating inventory levels

Demo data scripts generate sample records to quickly test API functionality.

Features

CRUD operations for products

Filtered sales retrieval (by date range, product, category)

Sales summary reporting (daily aggregates)

Revenue calculation and period comparison

Inventory monitoring (low-stock filtering, stock updates)

Automatic table creation on startup via SQLAlchemy

Demo-data seeding script for rapid testing

Tech Stack

Python 3.10+

FastAPI for HTTP API

Uvicorn as ASGI server

SQLAlchemy ORM for database interactions

PyMySQL driver connecting to MySQL

python-dotenv for environment configuration

Prerequisites

MySQL Server 8.0+ installed and running

Python 3.10+

Git client

Getting Started

Clone Repository

git clone https://github.com/MoizSajjad/Ecommerce-admin-api.git
cd Ecommerce-admin-api

Set Up Virtual Environment

# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

Install Dependencies

pip install -r requirements.txt

Configure Environment Variables

Copy .env.example to .env:

copy .env.example .env

Edit .env and fill in real values:

DB_HOST=localhost
DB_PORT=3306
DB_USER=moiz
DB_PASS=admin1234
DB_NAME=ecommerce

Database Setup

Access MySQL (via Workbench or CLI).

Create the database and user:

CREATE DATABASE ecommerce;
CREATE USER 'moiz'@'localhost' IDENTIFIED BY 'admin1234';
GRANT ALL PRIVILEGES ON ecommerce.* TO 'moiz'@'localhost';
FLUSH PRIVILEGES;

Seed Demo Data

Populate your tables with sample products, sales, and inventory:

python scripts/seed_demo_data.py

Expected output: ✅ Demo data seeded successfully!

Run the Application

uvicorn app.main:app --reload

Visit interactive docs at http://127.0.0.1:8000/docs.

API Reference

Products

Method

Endpoint

Description

Request Body

Response Model

GET

/products/

List products (with skip, limit)

n/a

List of ProductRead

POST

/products/

Create a new product

ProductCreate JSON

ProductRead

Sales

Method

Endpoint

Description

Query Params

Response Model

GET

/sales/

Retrieve sales, with filters

start, end, product_id, category

List of SaleRead

GET

/sales/summary

Get daily sales summaries (quantity & revenue)

start, end

List of SalesSummaryItem

Revenue

Method

Endpoint

Description

Query Params

Response Model

GET

/revenue/

Total revenue over an optional date range

start, end

RevenueTotal

GET

/revenue/compare

Compare revenue between two date ranges

start1,end1,start2,end2

RevenueCompare

Inventory

Method

Endpoint

Description

Query Params

Request Body

Response Model

GET

/inventory/

View inventory; optional low-stock filtering

low_stock_only (bool), threshold

n/a

List of InventoryRead

PATCH

/inventory/{product_id}

Update stock level for a specific product

n/a

InventoryUpdate JSON

InventoryRead

Database Schema

+-------------+      +-------+      +-----------+
|   products  |<-----| sales |      | inventory |
|-------------|      |-------|      |-----------|
| id PK       | 1   *| id PK | 1   1| id PK     |
| name        |      | product_id FK --->product_id FK|
| category    |      | quantity|     | stock_level|
| price       |      | sale_date|    | last_updated|
| created_at  |      | revenue |     +-----------+
+-------------+      +-------+      

Examples

List Products

curl "http://127.0.0.1:8000/products/?limit=5"

Create Product

curl -X POST "http://127.0.0.1:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{"name":"Widget","category":"Gadgets","price":29.99}'

Sales Summary

curl "http://127.0.0.1:8000/sales/summary?start=2025-01-01T00:00:00&end=2025-05-01T00:00:00"

Revenue Comparison

curl "http://127.0.0.1:8000/revenue/compare?start1=2025-04-01T00:00:00&end1=2025-04-15T00:00:00&start2=2025-03-01T00:00:00&end2=2025-03-15T00:00:00"

Project Structure

Ecommerce-admin-api/
├── app/
│   ├── main.py          # FastAPI app and router inclusion
│   ├── db.py            # SQLAlchemy engine & session
│   ├── models.py        # ORM models definitions
│   ├── schemas.py       # Pydantic request/response models
│   ├── crud.py          # Database operations
│   └── routers/         # Individual route modules
├── scripts/             # Utility scripts (e.g., data seeder)
│   └── seed_demo_data.py
├── .env.example         # Env var template
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

Contributing

Fork the repository

Create a feature branch

Commit changes with clear messages

Open a Pull Request

License

This project is licensed under the MIT License. See the LICENSE file for details.