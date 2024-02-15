import google.generativeai as genai
import config
from ai_model.abstract_base_model import AbstractBaseModel


class GeminiModel(AbstractBaseModel):
    def __init__(self):
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

    def communicate(self, prompt: str) -> str:
        response = self.chat.send_message(prompt)
        return response.text