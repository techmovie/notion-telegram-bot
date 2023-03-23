FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
COPY config_sample.py ./config.py
RUN pip install --no-cache-dir -r requirements.txt

ENV NOTION_API_KEY = 'your_notion_api_key'
ENV NOTION_DATABASE_ID = 'your_databse_id'
ENV TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
ENV OPENAI_API_KEY = 'your_openai_api_key'
ENV OPENAI_PROMPT = 'your_openai_prompt'

COPY . .

CMD ["python", "main.py"]