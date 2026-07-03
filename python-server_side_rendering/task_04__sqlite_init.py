#!/usr/bin/env python3

import sqlite3


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'THE Dark Chocolate', 'Food', 5.99),
        (4, 'Milk Cream', 'Food', 2.99),
        (5, 'Office Chair', 'Home Goods', 234.99),
        (6, 'HR Screen', 'Electronics', 675.52),
        (7, 'Pillow', 'Home Goods', 7.99)
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()
