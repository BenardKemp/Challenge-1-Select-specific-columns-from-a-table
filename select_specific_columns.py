import sqlite3

def select_specific_columns():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #1
    query = "SELECT product_id, name, category, price, stock_qty, created_at FROM products"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    select_specific_columns()
