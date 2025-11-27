from core.database.database import Database
import sqlite3
import os

# Ensure we are in the right directory or set path correctly
# The test uses 'test_order_management.db' in 'core/database/' but passes 'test_order_management.db' to constructor
# Database class joins base_dir with filename.
# base_dir is core/database/

db = Database('test_order_management.db')
print(f"DB Path: {db.db_path}")

try:
    with sqlite3.connect(db.db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT product FROM commodity WHERE category = '主食'")
        result = cur.fetchall()
        print(f"Direct fetchall result: {result}")
        if result:
            print(f"Row type: {type(result[0])}")
            print(f"Row[0] content: {result[0]}")
            print(f"Row[0][0]: {result[0][0]}")

    names = db.get_product_names_by_category('主食')
    print(f"Method result: {names}")
except Exception as e:
    print(f"Error: {e}")
