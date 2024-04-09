import json
import time
import os
from ai.communication.ai_communication_manager import AICommunicationManager
from ai.communication.ai_story_output import AIStoryOutput
from ai.communication.ai_skill_check_output import AISkillCheckOutput
from game.die import Die
from game.player.player import Player
from logger import Logger
import random


class Game:
    def __init__(self, player: Player, ai_communication_manager: AICommunicationManager, logger: Logger):
        self.player = player
        self.logger = logger
        self.ai_communication_manager = ai_communication_manager

    def play(self) -> None:
        # TODO: Implement game ending conditions (death, victory, etc.)
        output = self.initialize_story()
        self.logger.log(output.story)
        while (True):
            self.take_turn()

    def take_turn(self) -> None:
        player_prompt = self.get_user_action()
        if player_prompt == "/inventory":
            self.logger.log(str(self.player.inventory.to_json()))
        elif player_prompt == "/save":
            self.save_player()
        else:
            skill_checks = self.perform_skill_checks(self.find_skill_checks(player_prompt)) 
            response = self.get_next_story(player_prompt, skill_checks)
            self.update_player(response)
            self.logger.debug_log(skill_checks)
            self.logger.debug_log(response.to_json()) 
            self.logger.log(response.story)

    def find_skill_checks(self, prompt: str) -> AISkillCheckOutput:
        return self.ai_communication_manager.skill_communicate(prompt)
    
    def initialize_story(self) -> AIStoryOutput:
        starting_sentence= "This is the start of the game, begin the story with "
        with open("game/prompts.txt", "r") as f: #Pulling from prompts.txt file. One line per prompt added
            prompts = f.readlines()
        prompt = starting_sentence.join(random.choice(prompts))
        return self.ai_communication_manager.story_communicate(self.player, {}, prompt)
    
    def get_next_story(self, player_prompt: str, skill_checks: dict[str, int]) -> AIStoryOutput:
        return self.ai_communication_manager.story_communicate(self.player, player_prompt, skill_checks)

    def update_player(self, data: AIStoryOutput) -> None:
        # TODO: Add support for more data
        self.player.xp += data.xp_earned
        for item in data.new_items:
            self.player.inventory.add_item(item)
        self.player.hp -= data.damage_taken

    def get_user_action(self) -> str:
        return self.logger.input("Input your action ('/help' for directions): ")
    
    def perform_skill_checks(self, skill_output: AISkillCheckOutput) -> dict[str, int]:
        # TODO: Double check that skill checks are always done with a d20
        die = Die(20)
        results = {}
        for skill in skill_output.skill_checks:
            # Sometimes the model returns a skill check that isn't valid
            try:
                results[skill] = die.roll() + self.player.skills.__getattribute__(skill.lower())
            except:
                pass
        return results

    def save_player(self) -> None:
        dir_path = os.path.join(os.getcwd(), "save", "character")
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f"{self.player.name}{time.time()}.json")
        with open(file_path, "w") as file:
            file.write(json.dumps(self.player.to_json(), indent=4))
        self.logger.log("Character saved.")