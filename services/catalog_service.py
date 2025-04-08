from core.abstractions import DatabaseAdapter

class CatalogService:
    def __init__(self, db: DatabaseAdapter):
        self.db = db

    def add_product(self, key: str, name: str, description: str, price: float):
        self.db.add_product(key, name, description, price)

    def remove_product(self, key: str):
        self.db.remove_product(key)

    def get_catalog(self) -> dict:
        return self.db.get_products()