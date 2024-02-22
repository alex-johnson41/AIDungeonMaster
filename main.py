from ai_model.gemini_model import GeminiModel
from ai_model.model_settings import SKILL_CHECK_PROMPT, STORY_PROMPT
from character_creation.character_creator import CharacterCreator
from game.game import Game


def basic_communication():
    model = GeminiModel(SKILL_CHECK_PROMPT)
    while True:
        prompt = input("Enter a prompt:")
        if prompt == "/reset":
            model.reset()
        else:
            while (True):
                response = model.communicate(prompt)
                try: 
                    skill_checks = eval(response)
                    break
                except:
                    model.reset()
            print(skill_checks)

def play():
    story_model = GeminiModel(STORY_PROMPT)
    skill_model = GeminiModel(SKILL_CHECK_PROMPT)
    player = CharacterCreator.create_character()
    game = Game(player, story_model, skill_model)
    game.play()

basic_communication()