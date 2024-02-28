from ai_model.gemini_model import GeminiModel
from ai_model.model_settings import SKILL_CHECK_PROMPT, STORY_PROMPT
from character_creation.character_creator import CharacterCreator
from character_creation.klass.fighter import Fighter
from character_creation.race.human import Human
from game.game import Game
from game.inventory import Inventory
from game.player.player import Player
from game.player.skills import Skills
from game.player.stats import Stats


def skill_check_testing():
    model = GeminiModel(SKILL_CHECK_PROMPT)
    while True:
        prompt = input("Enter a prompt: ")
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

def dummy_character() -> Player:
    stats = Stats(10, 10, 10, 10, 10, 10)
    skills = Skills({"acrobatics": 0, "animal_handling": 0, "arcana": 0, "athletics": 0, "deception": 0, "history": 0, "insight": 0, "intimidation": 0, "investigation": 0, "medicine": 0, "nature": 0, "perception": 0, "performance": 0, "persuasion": 0, "religion": 0, "sleight_of_hand": 0, "stealth": 0, "survival": 0})

    return Player("Test", stats, skills, [], 10, Fighter(), Human(), Inventory(10), 0)

def play():
    story_model = GeminiModel(STORY_PROMPT)
    skill_model = GeminiModel(SKILL_CHECK_PROMPT)
    # player = CharacterCreator.create_character()
    player = dummy_character()
    game = Game(player, story_model, skill_model)
    game.play()

play()