import telebot
from config.settings import API_TOKEN

class Bot:
    def __init__(self):
        self.instance = telebot.TeleBot(API_TOKEN)

    def get_instance(self):
        return self.instance

    def start(self):
        self.instance.polling(none_stop=True)