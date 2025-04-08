from telebot import types
from core.abstractions import KeyboardBuilder

class TelegramKeyboard(KeyboardBuilder):
    def main_menu(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('☕ Переглянути каталог'),
                   types.KeyboardButton('ℹ️ Про нас'),
                   types.KeyboardButton('❓ Допомога'))
        return markup

    def admin_menu(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('➕ Додати каву'),
                   types.KeyboardButton('➖ Видалити каву'),
                   types.KeyboardButton('📦 Замовлення'))
        return markup

    def catalog_menu(self, products: dict):
        markup = types.InlineKeyboardMarkup()
        for key, item in products.items():
            btn = types.InlineKeyboardButton(f"☕ {item['name']} — {item['price']} грн", callback_data=key)
            markup.add(btn)
        return markup

    def product_details(self, key: str):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🛒 Замовити зараз", callback_data=f"order_{key}"))
        return markup

    def order_confirmation(self):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✅ Підтвердити замовлення", callback_data="confirm_order"),
                   types.InlineKeyboardButton("❌ Скасувати", callback_data="cancel_order"))
        return markup