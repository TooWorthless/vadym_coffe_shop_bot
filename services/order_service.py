from core.abstractions import DatabaseAdapter

class OrderService:
    def __init__(self, db: DatabaseAdapter):
        self.db = db

    def create_order(self, user_id: int, product_name: str, price: float):
        self.db.add_order(user_id, product_name, price)

    def get_all_orders(self) -> list:
        return self.db.get_orders()