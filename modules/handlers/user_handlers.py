from telebot import TeleBot
from modules.handlers.base_handler import BaseHandler
from services.catalog_service import CatalogService
from services.feedback_service import FeedbackService

class UserHandlers(BaseHandler):
    def register_handlers(self):
        @self.bot.message_handler(func=lambda message: message.text == "☕ Переглянути каталог")
        def catalog(message):
            try:
                catalog_service = CatalogService(self.db)
                products = catalog_service.get_catalog()
                if not products:
                    self.bot.send_message(message.chat.id, "☹️ Каталог поки порожній!")
                else:
                    self.bot.send_message(message.chat.id, "☕ Ось наша кавова колекція:", 
                                         reply_markup=self.keyboard.catalog_menu(products))
            except Exception as e:
                self.bot.send_message(message.chat.id, f"☹️ Щось пішло не так: {str(e)}. Спробуй ще раз!")

        @self.bot.message_handler(func=lambda message: message.text == "ℹ️ Про нас")
        def info(message):
            self.bot.reply_to(message, "👋 Ми — Vadyms Coffee Bot! Твій помічник у світі ароматної кави. "
                                      "Замовляй улюблений напій через каталог і насолоджуйся! ☕")

        @self.bot.message_handler(func=lambda message: message.text == "❓ Допомога")
        def help(message):
            self.bot.reply_to(message, "✨ Ось що я вмію:\n"
                                     "☕ Переглянути каталог — наш асортимент\n"
                                     "ℹ️ Про нас — хто ми такі\n"
                                     "❓ Допомога — список дій\n"
                                     "💬 /feedback — поділитися враженнями\n"
                                     "🔒 Для адмінів: /admin")

        @self.bot.message_handler(commands=['start'])
        def start(message):
            self.bot.reply_to(message, "☕ Вітаємо в Vadyms Coffee Bot! Готуємо найкращу каву для тебе! ☕\nОбери, що хочеш:", 
                              reply_markup=self.keyboard.main_menu())

        @self.bot.message_handler(commands=['feedback'])
        def feedback(message):
            msg = self.bot.reply_to(message, "💬 Розкажи, що думаєш про нашу каву чи сервіс!")
            self.bot.register_next_step_handler(msg, self.process_feedback)

    def process_feedback(self, message):
        try:
            feedback_service = FeedbackService(self.db)
            feedback_service.save_feedback(message.from_user.id, message.text)
            self.bot.reply_to(message, "🌟 Дякуємо за твій відгук! Він робить нас кращими!")
        except Exception as e:
            self.bot.reply_to(message, f"☹️ Не вдалося зберегти відгук: {str(e)}. Спробуй ще раз!")