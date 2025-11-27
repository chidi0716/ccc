import datetime
import os
import random
import sqlite3

class Database():
    def __init__(self, db_filename="order_management.db"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(base_dir, db_filename)

    @staticmethod
    def generate_order_id() -> str:
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        random_num = random.randint(1000, 9999)
        return f"OD{timestamp}{random_num}"

    def get_product_names_by_category(self, category):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            sql = "SELECT product FROM commodity WHERE category = ?"
            cur.execute(sql, (category,))
            return cur.fetchall()

    def get_product_price(self, product):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            sql = "SELECT price FROM commodity WHERE product = ?"
            cur.execute(sql, (product,))
            result = cur.fetchone()
            return result[0] if result else None

    def add_order(self, order_data):
        order_id = self.generate_order_id()
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            sql = """
                INSERT INTO order_list (
                    order_id, date, customer_name, product, 
                    amount, total, status, note
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cur.execute(sql, (
                order_id,
                order_data['product_date'],
                order_data['customer_name'],
                order_data['product_name'],
                order_data['product_amount'],
                order_data['product_total'],
                order_data['product_status'],
                order_data['product_note']
            ))
            conn.commit()

    def get_all_orders(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            sql = """
                SELECT 
                    o.order_id, o.date, o.customer_name, o.product, 
                    c.price, o.amount, o.total, o.status, o.note
                FROM order_list o
                LEFT JOIN commodity c ON o.product = c.product
            """
            cur.execute(sql)
            return cur.fetchall()

    def delete_order(self, order_id):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            sql = "DELETE FROM order_list WHERE order_id = ?"
            cur.execute(sql, (order_id,))
            conn.commit()
            return True
