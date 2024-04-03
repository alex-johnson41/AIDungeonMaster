import json
import os
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


"""
FEATURES TO ADD: 
- Save and load characters
- Save and load games


"""
def dummy_character() -> Player:
    stats = Stats(10, 10, 10, 10, 10, 10)
    skills = Skills({"acrobatics": 0, "animal_handling": 0, "arcana": 0, "athletics": 0, "deception": 0, 
                     "history": 0, "insight": 0, "intimidation": 0, "investigation": 0, "medicine": 0, 
                     "nature": 0, "perception": 0, "performance": 0, "persuasion": 0, "religion": 0, 
                     "sleight_of_hand": 0, "stealth": 0, "survival": 0
                     })

    return Player("Test", stats, skills, [], 10, Fighter(), Human(), Inventory(10), 0)

def play():
    logger = Logger(debug=False)
    logger.log("\nWelcome to DungeonMaster AI!\n(/help for commands)")
    player = setup_character(logger)
    # player = dummy_character()
    logger.log("Initializing game...")
    game = setup_game(logger, player)
    game.play()

def setup_game(logger: Logger, player: Player) -> Game:
        story_model = GeminiModel(STORY_PROMPT)
        skill_model = GeminiModel(SKILL_CHECK_PROMPT)
        ai_communication_manager = AICommunicationManager(story_model, skill_model)
        return Game(player, ai_communication_manager, logger)

def setup_character(logger: Logger) -> Player:
    logger.log("\nWould you like to create a new character or load an existing one?\n1. Create character\n2. Load character")
    while True:
        choice = logger.input("Enter the number of your choice: ")
        if choice == "1":
            return CharacterCreator(logger).create_character()
        elif choice == "2":
            return load_character(logger)
        else:
            logger.log("Please enter the number of your choice.")

def load_character(logger: Logger) -> Player:
    save_folder = os.path.join(os.getcwd(), "save/character")
    files = os.listdir(save_folder)
    for i, file in enumerate(files):
        logger.log(f"{i + 1}. {file}")
    file_num = int(logger.input("Input the number of the character file you would like to load: "))
    try:
        with open(os.path.join(save_folder, files[file_num-1]), "r") as file:
            data = json.loads(file.read())
            return Player.from_json(data)
    except FileNotFoundError:
        logger.log("File not found. Please try again.")
        return load_character(logger)

play()