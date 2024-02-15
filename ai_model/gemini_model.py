import google.generativeai as genai
import config
from ai_model.abstract_ai_model import AbstractAIModel


class GeminiModel(AbstractAIModel):
    def __init__(self):
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

    def communicate(self, prompt: str) -> str:
        response = self.chat.send_message(prompt)
        return response.text