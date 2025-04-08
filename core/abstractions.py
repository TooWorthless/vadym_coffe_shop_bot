from abc import ABC, abstractmethod

class DatabaseAdapter(ABC):
    @abstractmethod
    def add_product(self, key: str, name: str, description: str, price: float): pass
    @abstractmethod
    def remove_product(self, key: str): pass
    @abstractmethod
    def get_products(self) -> dict: pass
    @abstractmethod
    def add_order(self, user_id: int, product_name: str, price: float): pass
    @abstractmethod
    def get_orders(self) -> list: pass
    @abstractmethod
    def add_feedback(self, user_id: int, text: str): pass

class PaymentProvider(ABC):
    @abstractmethod
    def generate_invoice(self, user_id: int, product_name: str, price: float) -> str: pass
    @abstractmethod
    def confirm_payment(self) -> str: pass

class KeyboardBuilder(ABC):
    @abstractmethod
    def main_menu(self): pass
    @abstractmethod
    def admin_menu(self): pass
    @abstractmethod
    def catalog_menu(self, products: dict): pass
    @abstractmethod
    def product_details(self, key: str): pass
    @abstractmethod
    def order_confirmation(self): pass