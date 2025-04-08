from core.bot import Bot
from modules.database.sqlite_db import SQLiteDatabase
from modules.payments.mock_payment import MockPayment
from modules.keyboards.telegram_kb import TelegramKeyboard
from modules.handlers.user_handlers import UserHandlers
from modules.handlers.admin_handlers import AdminHandlers
from modules.handlers.callback_handlers import CallbackHandlers

def main():
    bot = Bot()
    db = SQLiteDatabase()
    payment = MockPayment()
    keyboard = TelegramKeyboard()

    db.add_product("espresso", "Еспресо", "Міцна класика для справжніх поціновувачів", 35.0)
    db.add_product("latte", "Лате", "Ніжна кава з пишною молочною пінкою", 45.0)
    db.add_product("cappuccino", "Капучино", "Ідеальний баланс кави та молока", 40.0)
    db.add_product("americano", "Американо", "Легка кава для довгих розмов", 30.0)
    db.add_product("mocha", "Мокко", "Шоколадна насолода з кавовим присмаком", 50.0)
    db.add_product("flatwhite", "Флет Вайт", "Гладка текстура та насичений смак", 48.0)

    user_handlers = UserHandlers(bot.get_instance(), db, payment, keyboard)
    admin_handlers = AdminHandlers(bot.get_instance(), db, payment, keyboard)
    callback_handlers = CallbackHandlers(bot.get_instance(), db, payment, keyboard)

    user_handlers.register_handlers()
    admin_handlers.register_handlers()
    callback_handlers.register_handlers()

    bot.start()

if __name__ == "__main__":
    main()