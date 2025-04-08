from telebot import TeleBot
from config.settings import ADMIN_IDS
from modules.handlers.base_handler import BaseHandler
from services.order_service import OrderService

class CallbackHandlers(BaseHandler):
    def register_handlers(self):
        @self.bot.callback_query_handler(func=lambda call: call.data in self.db.get_products())
        def product_details(call):
            try:
                item = self.db.get_products()[call.data]
                response = f"☕ *{item['name']}*\n📝 {item['description']}\n💸 Ціна: {item['price']} грн"
                self.bot.send_message(call.message.chat.id, response, parse_mode='Markdown', 
                                     reply_markup=self.keyboard.product_details(call.data))
            except Exception as e:
                self.bot.send_message(call.message.chat.id, f"☹️ Помилка: {str(e)}. Спробуй ще раз!")

        @self.bot.callback_query_handler(func=lambda call: call.data.startswith("order_"))
        def order(call):
            try:
                key = call.data.split("_")[1]
                item = self.db.get_products()[key]
                order_service = OrderService(self.db)
                order_service.create_order(call.from_user.id, item["name"], item["price"])
                invoice = self.payment.generate_invoice(call.from_user.id, item["name"], item["price"])
                self.bot.send_message(call.message.chat.id, f"🛒 Твоє замовлення:\n{invoice}", 
                                     reply_markup=self.keyboard.order_confirmation())
            except Exception as e:
                self.bot.send_message(call.message.chat.id, f"☹️ Помилка: {str(e)}. Спробуй ще раз!")

        @self.bot.callback_query_handler(func=lambda call: call.data in ["confirm_order", "cancel_order"])
        def confirm_order(call):
            try:
                if call.data == "confirm_order":
                    self.bot.send_message(call.message.chat.id, "🎉 Оплата пройшла! Твоя кава вже готується! ☕")
                    for admin_id in ADMIN_IDS:
                        self.bot.send_message(admin_id, f"📩 Нове замовлення від {call.from_user.id} підтверджено!")
                else:
                    self.bot.send_message(call.message.chat.id, "😔 Замовлення скасовано. Завжди раді бачити тебе знову!")
            except Exception as e:
                self.bot.send_message(call.message.chat.id, f"☹️ Помилка: {str(e)}. Спробуй ще раз!")