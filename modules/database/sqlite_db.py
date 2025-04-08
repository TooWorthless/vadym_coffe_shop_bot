import sqlite3
from config.settings import DB_NAME
from core.abstractions import DatabaseAdapter

class SQLiteDatabase(DatabaseAdapter):
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                name TEXT,
                description TEXT,
                price REAL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_name TEXT,
                price REAL,
                status TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                text TEXT
            )
        ''')
        self.conn.commit()

    def add_product(self, key: str, name: str, description: str, price: float):
        self.cursor.execute('INSERT OR REPLACE INTO products (key, name, description, price) VALUES (?, ?, ?, ?)',
                           (key, name, description, price))
        self.conn.commit()

    def remove_product(self, key: str):
        self.cursor.execute('DELETE FROM products WHERE key = ?', (key,))
        self.conn.commit()

    def get_products(self) -> dict:
        try:
            self.cursor.execute('SELECT key, name, description, price FROM products')
            return {row[0]: {"name": row[1], "description": row[2], "price": row[3]} for row in self.cursor.fetchall()}
        except Exception:
            return {}

    def add_order(self, user_id: int, product_name: str, price: float):
        self.cursor.execute('INSERT INTO orders (user_id, product_name, price, status) VALUES (?, ?, ?, ?)',
                           (user_id, product_name, price, 'pending'))
        self.conn.commit()

    def get_orders(self) -> list:
        self.cursor.execute('SELECT user_id, product_name, price, status FROM orders')
        return [{"user_id": row[0], "product_name": row[1], "price": row[2], "status": row[3]} for row in self.cursor.fetchall()]

    def add_feedback(self, user_id: int, text: str):
        self.cursor.execute('INSERT INTO feedback (user_id, text) VALUES (?, ?)', (user_id, text))
        self.conn.commit()