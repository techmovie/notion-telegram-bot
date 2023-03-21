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


## ChatGPT Usage

In certain scenarios, we may opt to leverage ChatGPT's capabilities to produce and subsequently update content in the Notion database. For instance, by transmitting an English term to ChatGPT, we can obtain its definitions or phonetics. Upon receiving the response, it can be seamlessly integrated into our database.

Follow the steps below to use this feature.

1. Set up your OpenAI API key in `config.py`:

    ```
    OPENAI_API_KEY = "your_openai_api_key"
    ```
2. Set up your prompt in `config.py`:

    ```
    OPENAI_PROMPT = "your_openai_api_prompt"
    ```
    In the aforementioned example, the prompt can be: Please provide the details of the English word I shared with you and follow this format: Word:\nPronunciation:(Phonetic symbol)\nDefinition:\nIn Chinese:\nExample Sentence:\nDate Learned:(Time when I send this prompt formatted as: YYYY-MM-DD)\nDifficulty:Medium\nRemembered:(Fixed to false)
    
3. Run the bot:

    ```
    python main.py
    ```

4. Send a message starting with the `/openai` command to tell the ChatGPT the things you want to do with the prompt. 

    In the above example, the message can be: /openai Inclination.