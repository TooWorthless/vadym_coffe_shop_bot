from telebot import TeleBot
from core.abstractions import DatabaseAdapter, PaymentProvider, KeyboardBuilder

class BaseHandler:
    def __init__(self, bot: TeleBot, db: DatabaseAdapter, payment: PaymentProvider, 
                 keyboard: KeyboardBuilder):
        self.bot = bot
        self.db = db
        self.payment = payment
        self.keyboard = keyboard

    def register_handlers(self):
        pass