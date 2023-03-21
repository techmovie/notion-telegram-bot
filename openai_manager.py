import openai
from config import OPENAI_API_KEY,OPENAI_PROMPT


class OpenAiManager:
    def __init__(self, message) -> None:
        openai.api_key = OPENAI_API_KEY
        self.message = message

    def get_prompt_result(self):
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "system","content": OPENAI_PROMPT}, {"role": "user", "content": self.message.strip()}],
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