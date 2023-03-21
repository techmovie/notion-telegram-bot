import telebot
from config import TELEGRAM_API_KEY
from message_handler import process_message, send_help
from logger import logger

class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_API_KEY)

    def start(self):
        @self.bot.message_handler(commands=['start', 'help'])
        def handle_help(message):
            response = send_help()
            self.bot.reply_to(message, response)

        @self.bot.message_handler(commands=['update'])
        def handle_update(message):
            message_text = message.text
            message_text = message_text.replace('/update', '', 1).strip()

            if not message_text:
                self.bot.reply_to(message, "The message is empty. Please provide the required information.")

            try:
                process_message(message_text)
                self.bot.reply_to(message, "The Notion database has been updated successfully.")
            except Exception as e:
                logger.exception(f"Failed to update the Notion database,{e}")
                self.bot.reply_to(message, f"An error occurred while updating the Notion database: {e}")
            
        self.bot.polling()