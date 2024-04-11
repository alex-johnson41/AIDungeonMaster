import json
import os
from ai.communication.ai_communication_manager import AICommunicationManager
from ai.models.gemini_model import GeminiModel
from constants import SKILL_CHECK_PROMPT, STORY_PROMPT
from character_creation.character_creator import CharacterCreator
from game.game import Game
from game.player.player import Player
from logger import Logger


def play():
    logger = Logger(debug=False)
    logger.log("\nWelcome to DungeonMaster AI!\n(/help for commands)")
    player = setup_character(logger)
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
            try:
                return load_character(logger)
            except:
                logger.log("No character files found. Please create a character.")
                return CharacterCreator(logger).create_character()
        else:
            logger.log("Please enter the number of your choice.")

def load_character(logger: Logger) -> Player:
    save_folder = os.path.join(os.getcwd(), "save/character")
    files = os.listdir(save_folder)
    if not files: raise FileNotFoundError
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