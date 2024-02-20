import google.generativeai as genai
import config
from ai_model.abstract_ai_model import AbstractAIModel
from .model_settings import SAFETY_SETTINGS


class GeminiModel(AbstractAIModel):
    def __init__(self, initialization_prompt: str = None):
        genai.configure(api_key=config.GEMINI_API_KEY)
        self.reset(initialization_prompt)

    def communicate(self, prompt: str) -> str:
        response = self.chat.send_message(prompt, safety_settings=SAFETY_SETTINGS)
        return response.text
    
    def reset(self, initialization_prompt: str = None):
        self.model = genai.GenerativeModel('gemini-pro', safety_settings=SAFETY_SETTINGS)
        self.chat = self.model.start_chat(history=[])
        if initialization_prompt:
            self.communicate(initialization_prompt)