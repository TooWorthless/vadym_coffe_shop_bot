
import logging
from config.settings import LOG_FILE
from core.abstractions import Logger

class FileLogger(Logger):
    def __init__(self):
        logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                            format='%(asctime)s - %(message)s')

    def log(self, message: str):
        logging.info(message)
