from core.abstractions import PaymentProvider

class MockPayment(PaymentProvider):
    def generate_invoice(self, user_id: int, product_name: str, price: float) -> str:
        return f"Рахунок для {user_id}: {product_name} - {price} грн. Сплатіть за посиланням: [example.com/pay]"

    def confirm_payment(self) -> str:
        return "Оплата підтверджена! Ваш товар буде відправлено скоро."