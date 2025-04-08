
from telebot import TeleBot
from config.settings import ADMIN_IDS
from modules.handlers.base_handler import BaseHandler
from core.exceptions import AdminAccessError
from services.catalog_service import CatalogService
from services.order_service import OrderService
from utils.validators import validate_product_data

class AdminHandlers(BaseHandler):
    def register_handlers(self):
        @self.bot.message_handler(commands=['admin'])
        def admin(message):
            try:
                self._check_admin(message.from_user.id)
                self.bot.reply_to(message, "🔧 Вітаємо в адмін-панелі, бариста!", reply_markup=self.keyboard.admin_menu())
            except AdminAccessError as e:
                self.bot.reply_to(message, str(e))

        @self.bot.message_handler(func=lambda message: message.text == "➕ Додати каву")
        def add_item(message):
            try:
                self._check_admin(message.from_user.id)
                msg = self.bot.reply_to(message, "➕ Додай нову каву: ключ, назва, опис, ціна (через кому, наприклад: latte, Лате, Ніжна кава, 45.0)")
                self.bot.register_next_step_handler(msg, self.process_add_item)
            except AdminAccessError as e:
                self.bot.reply_to(message, str(e))

        @self.bot.message_handler(func=lambda message: message.text == "➖ Видалити каву")
        def remove_item(message):
            try:
                self._check_admin(message.from_user.id)
                msg = self.bot.reply_to(message, "➖ Вкажи ключ кави, яку хочеш прибрати:")
                self.bot.register_next_step_handler(msg, self.process_remove_item)
            except AdminAccessError as e:
                self.bot.reply_to(message, str(e))

        @self.bot.message_handler(func=lambda message: message.text == "📦 Замовлення")
        def orders(message):
            try:
                self._check_admin(message.from_user.id)
                order_service = OrderService(self.db)
                orders_list = order_service.get_all_orders()
                response = "\n".join([f"👤 {o['user_id']}: {o['product_name']} — {o['price']} грн ({o['status']})" for o in orders_list])
                self.bot.reply_to(message, f"📦 Ось усі замовлення:\n{response}" if response else "📭 Замовлень поки немає.")
            except AdminAccessError as e:
                self.bot.reply_to(message, str(e))
            except Exception as e:
                self.bot.reply_to(message, f"☹️ Щось пішло не так: {str(e)}. Спробуй ще раз!")

    def _check_admin(self, user_id: int):
        if user_id not in ADMIN_IDS:
            raise AdminAccessError("🔒 Ти не бариста! Доступ заборонено.")

    def process_add_item(self, message):
        try:
            key, name, description, price = validate_product_data(message.text)
            catalog_service = CatalogService(self.db)
            catalog_service.add_product(key, name, description, price)
            self.bot.reply_to(message, f"✅ {name} доданий до меню! Час заварювати!")
        except Exception as e:
            self.bot.reply_to(message, f"☹️ Помилка: {str(e)}. Спробуй ще раз!")

    def process_remove_item(self, message):
        try:
            key = message.text.strip()
            catalog_service = CatalogService(self.db)
            catalog_service.remove_product(key)
            self.bot.reply_to(message, f"🗑️ Каву з ключем {key} прибрано з меню!")
        except Exception as e:
            self.bot.reply_to(message, f"☹️ Помилка: {str(e)}. Спробуй ще раз!")