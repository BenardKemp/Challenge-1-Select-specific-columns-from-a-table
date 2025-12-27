# SQL Beginner Challenge #1: Select Specific Columns

**Difficulty:** Beginner  
**Estimated time:** 5–10 minutes  
**Concepts:** `SELECT`, column selection, query clarity  

This challenge teaches a foundational SQL habit: **selecting only the columns you actually need**—instead of using `SELECT *`.
This challenge is part of series of SQL challenges [SolveWithSQL](https://solvewithsql.com)

---

## 🧠 The Problem

You’re working with an e-commerce database. A product manager asks for a simple list of products showing:

- Product name
- Price
- Category

They do **not** want internal columns like IDs, stock levels, or timestamps.

Your task is to write a SQL query that returns **only** the requested columns.

---

## 📊 Table Schema

### `products`

| Column Name | Type      | Description |
|------------|-----------|-------------|
| product_id | INTEGER   | Unique product ID |
| name       | TEXT      | Product name |
| category   | TEXT      | Product category |
| price      | DECIMAL   | Product price |
| stock_qty | INTEGER   | Units in stock |
| created_at | TIMESTAMP | Creation timestamp |

---

## 🧪 Sample Data

| product_id | name                 | category     | price  | stock_qty | created_at |
|-----------:|----------------------|--------------|-------:|----------:|------------|
| 101 | Wireless Mouse      | Accessories | 24.99 | 120 | 2025-01-10 |
| 102 | Mechanical Keyboard | Accessories | 89.00 | 45  | 2025-01-12 |
| 103 | 27-inch Monitor     | Displays    | 229.99| 18  | 2025-01-15 |
| 104 | USB-C Hub           | Accessories | 34.50 | 70  | 2025-01-18 |
| 105 | Laptop Stand        | Workspace   | 39.99 | 32  | 2025-01-21 |

---

## ✅ Requirements

Your query must:

- Return **only** the following columns:
  - `name`
  - `price`
  - `category`
- Use the column order shown above
- **Not** use `SELECT *`

---

## ✍️ Your Task

Write a SQL query that fulfills the requirements.

```sql
-- Write your query here

