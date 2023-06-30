import openai
from config import OPENAI_API_KEY,OPENAI_PROMPT
import datetime


class OpenAiManager:
    def __init__(self, message) -> None:
        openai.api_key = OPENAI_API_KEY
        self.message = message

    def get_prompt_result(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        prompt = OPENAI_PROMPT.replace("YYYY-MM-DD",now)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "system","content": prompt}, {"role": "user", "content": self.message.strip()}],
            max_tokens= 1024,
            n= 1,
            stop= None,
            temperature= 0,
        )
        result = response.choices[0].message.content.strip()
        print(result)
        if not result or ":" not in result:
            raise Exception("Failed to get response from openAI.Please check the prompt config and try again")
        return result
    def create_article_with_word(self):
        prompt = 'Create an engaging article incorporating ten of the words I provide to you. Ensure the words are used in diverse contexts to enhance my comprehension and retention of their meaning and usage. The article should fall within a word count range of 100 to 300 words. The main objective is to help me better understand and remember the usage of these words.'
        print(self.message.strip())
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "system","content": prompt}, {"role": "user", "content": self.message.strip()}],
            max_tokens= 1024,
            n= 1,
            stop= None,
            temperature= 0,
        )
        result = response.choices[0].message.content.strip()
        if not result:
            raise Exception("Failed to get response from openAI.Please check the prompt config and try again")
        return result