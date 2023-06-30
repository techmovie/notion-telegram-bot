import telebot
from config import TELEGRAM_BOT_TOKEN
from message_handler import process_message, send_help
from logger import logger
from openai_manager import OpenAiManager
from notion_manager import NotionManager

notion_manager = NotionManager()

class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

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
                return

            try:
                process_message(message_text)
                self.bot.reply_to(message, "The Notion database has been updated successfully.")
            except Exception as e:
                logger.exception(f"Failed to update the Notion database,{e}")
                self.bot.reply_to(message, f"An error occurred while updating the Notion database: {e}")

        @self.bot.message_handler(commands=['article'])
        def handle_article_creation(message):
            try:
                words = notion_manager.get_database_first_column_name()
                words = '\n'.join(words)
                openai_manager = OpenAiManager(words)
                result = openai_manager.create_article_with_word()
                notion_manager.create_page(
                    properties={
                        'Word': 
                            {
                                'title': [
                                    {
                                        'text': {'content': 'Combine words to articles'}
                                    }
                                ]
                            }
                    },
                    children=[{
                        "object": "block",
                        "paragraph": {
                            "rich_text": [
                                {
                                    "text": {
                                        "content": result
                                    },
                                }
                            ]
                        }
                    }]   
                )
                self.bot.reply_to(message, "The Notion database has been updated successfully.")
            except Exception as e:
                logger.exception(f"Failed to update the Notion database,{e}")
                self.bot.reply_to(message, f"An error occurred while updating the Notion database: {e}")
        
        @self.bot.message_handler(commands=['openai'])
        def handle_update(message):
            message_text = message.text
            message_text = message_text.replace('/openai', '', 1).strip()

            if not message_text:
                self.bot.reply_to(message, "The message is empty. Please provide the required information.")
                return
            try:
                openai_manager = OpenAiManager(message_text)
                result = openai_manager.get_prompt_result()
                process_message(result)
                self.bot.reply_to(message, "The Notion database has been updated successfully.")
            except Exception as e:
                logger.exception(f"Failed to update the Notion database,{e}")
                self.bot.reply_to(message, f"An error occurred while updating the Notion database: {e}")
        try:
            self.bot.infinity_polling()
        except Exception as e:
             logger.exception(f"Failed to start the bot,{e}")