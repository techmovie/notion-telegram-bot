# Notion Telegram Bot

A simple Telegram Bot that updates a Notion database based on user input. This bot supports various property types and allows users to specify a custom database_id to update.

## Setup

1. Install the required Python packages:
   

    ```
    pip install -r requirements.txt
    ```

2. Copy the `config_sample.py` file and rename it to `config.py`.

3. Set up your Notion API key and database ID in `config.py`:

    ```
    NOTION_API_KEY = "your_notion_api_key"
    NOTION_DATABASE_ID = "your_notion_database_id"
    ```

4. Set up your Telegram API key in `config.py`:

    ```
    TELEGRAM_API_KEY = "your_telegram_api_key"
    ```

5. Run the bot:

    ```
    python main.py
    ```

## Usage

1. Start a conversation with the bot in Telegram.
2. Use the `/start` or `/help` command to get instructions on how to format your message.
3. Send a message with the specified format to update the Notion database.
