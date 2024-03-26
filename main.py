from ai.communication.ai_communication_manager import AICommunicationManager
from ai.models.gemini_model import GeminiModel
from ai.models.model_settings import SKILL_CHECK_PROMPT, STORY_PROMPT
from character_creation.character_creator import CharacterCreator
from character_creation.klass.fighter import Fighter
from character_creation.race.human import Human
from game.game import Game
from game.inventory import Inventory
from game.player.player import Player
from game.player.skills import Skills
from game.player.stats import Stats
from logger import Logger

def dummy_character() -> Player:
    stats = Stats(10, 10, 10, 10, 10, 10)
    skills = Skills({"acrobatics": 0, "animal_handling": 0, "arcana": 0, "athletics": 0, "deception": 0, 
                     "history": 0, "insight": 0, "intimidation": 0, "investigation": 0, "medicine": 0, 
                     "nature": 0, "perception": 0, "performance": 0, "persuasion": 0, "religion": 0, 
                     "sleight_of_hand": 0, "stealth": 0, "survival": 0
                     })

    return Player("Test", stats, skills, [], 10, Fighter(), Human(), Inventory(10), 0)

def play():
    story_model = GeminiModel(STORY_PROMPT)
    skill_model = GeminiModel(SKILL_CHECK_PROMPT)
    ai_communication_manager = AICommunicationManager(story_model, skill_model)
    logger = Logger(debug=True)
    player = CharacterCreator(logger).create_character()
    # player = dummy_character()
    game = Game(player, ai_communication_manager, logger)
    game.play()

play()