from notion_manager import NotionManager
from logger import logger

notion_manager = NotionManager()
def send_help():
    help_message = (
        "To update the Notion database, send a message starting with the /update command and the following format:\n\n"
        "/update\n"
        "database_id:your_custom_database_id (optional)\n"
        "property_name1:value1\n"
        "property_name2:value2\n"
        "...\n\n"
        "If you don't specify a database_id, the bot will use the default one from the configuration file.\n\n"
        "Supported property types: title, rich_text, number, select, multi_select, "
        "date, people, files, checkbox, url, email, phone_number"
    )
    return help_message

def process_message(message):
    try:
        # Add data to the Notion database
        notion_manager.add_to_database(message)
        return "Data added to Notion database"
    except Exception as e:
        raise e
