from core.exceptions import ValidationError

def validate_product_data(data: str) -> tuple:
    try:
        key, name, description, price = data.split(", ")
        price = float(price)
        if price <= 0:
            raise ValidationError("Ціна має бути додатньою!")
        return key, name, description, price
    except ValueError:
        raise ValidationError("Неправильний формат: ключ, назва, опис, ціна")