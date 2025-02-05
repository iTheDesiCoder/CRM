# app/common/Logger.py
import json
import logging
import getpass
from injector import inject, singleton
from app.common.Logging.RequestContext import RequestContext
from app.config import level

@singleton
class AppLogger:
    def __init__(self, name='app', file='app.log'):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler = logging.FileHandler(file)
        handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        #self.logger.addHandler(handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(self.get_log_message(message))

    def info(self, message):
        self.logger.info(self.get_log_message(message))

    def warning(self, message):
        self.logger.warning(self.get_log_message(message))

    def error(self, message):
        self.logger.error(self.get_log_message(message))

    def critical(self, message):
        self.logger.critical(message, exc_info=True)

    def get_log_message(self, message):
        headers = RequestContext.headers.get()
        combined = {
            "headers": headers,
            "app_proid": getpass.getuser(),
            "message": message

        }
        return json.dumps(combined)
