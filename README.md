# Notion Telegram Bot

A simple Telegram Bot that updates a Notion database based on user input. This bot supports various property types and allows users to specify a custom database_id to update. It can also use ChatGPT's features to generate and update content in the Notion database automatically.


## Setup

1. Install the required Python packages:
   

    ```
    pip install -r requirements.txt
    ```

2. Copy the `config_sample.py` file and rename it to `config.py`.

3. Set up your Notion API key and database ID in `config.py`:

    ```
    NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "your_notion_api_key")
    NOTION_DATABASE_ID = os.environ.get("NOTION_DATABASE_ID", "your_notion_database_id")
    ```

4. Set up your Telegram API key in `config.py`:

    ```
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "your_telegram_bot_token")
    ```

5. Run the bot:

    ```
    python main.py
    ```

## Usage

1. Start a conversation with the bot in Telegram.
2. Use the `/start` or `/help` command to get instructions on how to format your message.
3. To use the bot, send a message to it on Telegram in the following format: 
   ```
   /update 
    database_id:your_custom_database_id (optional)
    property_name1:value1
    property_name2:value2

   ```
    The bot will extract the property names and values from the message and update the specified Notion database accordingly.

    If you don't specify a database_id, the bot will use the default one from the configuration file.

    Please note that you need to replace `PropertyName1`, `PropertyValue1`, `PropertyName2`, `PropertyValue2`, etc., with the actual property names and values you want to update in the Notion database.

    Supported property types: title, rich_text, number, select, multi_select, date, people, files, checkbox, url, email, phone_number

## ChatGPT Usage

In certain scenarios, we may opt to leverage ChatGPT's capabilities to produce and subsequently update content in the Notion database. For instance, by transmitting an English term to ChatGPT, we can obtain its definitions or phonetics. Upon receiving the response, it can be seamlessly integrated into our database.

Follow the steps below to use this feature.

1. Set up your OpenAI API key in `config.py`:

    ```
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "your_openai_api_key")
    ```
2. Set up your prompt in `config.py`:

    ```
    OPENAI_PROMPT = os.environ.get("OPENAI_PROMPT", "your_openai_api_prompt")
    ```
    In the aforementioned example, the prompt can be:
    > Please provide the details of the English word I shared with you and follow this format: Word:\nPronunciation:(Phonetic symbol)\nDefinition:\nIn Chinese:\nExample Sentence:\nDate Learned:(Time when I send this prompt formatted as: YYYY-MM-DD)\nDifficulty:Medium\nRemembered:(Fixed to false)
    
3. Run the bot:

    ```
    python main.py
    ```

4. Send a message starting with the `/openai` command to tell the ChatGPT the things you want to do with the prompt. 

    In the above example, the message can be: `/openai Inclination`.

## Commands

* `/start`: Starts the bot and displays a welcome message.
* `/help`: Shows the help message, which contains instructions on how to use the bot and the correct message format.
* `/update`: Triggers the bot to update the Notion database with the properties provided in the message.
* `/openai`: Triggers the bot to update the Notion database with the content generated by ChatGPT.

## Docker

You can also run this project in a Docker container.

```
docker run -e TELEGRAM_API_KEY=your_telegram_api_key -e NOTION_API_KEY=your_notion_api_key -e DATABASE_ID=your_database_id -e OPENAI_API_KEY=your_openai_api_key -e OPENAI_PROMPT=your_openai_prompt birdplane/notion-telegram-bot:latest
```

## Contributing
Feel free to fork this repository and make any changes or improvements you'd like. If you believe your changes could be beneficial to others, please create a pull request, and we'll review your contribution.

## License
This project is licensed under the MIT License.