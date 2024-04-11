import json
import time
import os
from ai.communication.ai_communication_manager import AICommunicationManager
from ai.communication.ai_story_output import AIStoryOutput
from ai.communication.ai_skill_check_output import AISkillCheckOutput
from constants import STARTING_PROMPTS
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
        output = self.initialize_story()
        self.logger.log(output.story, story=True)
        player_alive = True
        while (player_alive):
            player_alive = self.take_turn()
        self.logger.log("You have died, game over.")

    def take_turn(self) -> bool:
        player_prompt = self.get_user_action()
        if player_prompt == "/inventory":
            self.logger.log(str(self.player.inventory.to_json()))
        elif player_prompt == "/save":
            self.save_player()
        elif player_prompt == "/hp":
            self.logger.log(f"Current Hit Points: {self.player.hp}")
            self.logger.log(f"Max Hit Points: {self.player.hp_max}")
        elif player_prompt == "/player":
            self.logger.log(json.dumps(self.player.to_json(), indent=4))
        else:
            skill_checks = self.perform_skill_checks(self.find_skill_checks(player_prompt)) 
            self.logger.debug_log(str(skill_checks))
            response = self.get_next_story(player_prompt, skill_checks)
            self.logger.debug_log(str(response.to_json()))
            self.update_player(response) 
            self.logger.log(response.story, story=True)
        return self.player.hp > 0

    def find_skill_checks(self, prompt: str) -> AISkillCheckOutput:
        return self.ai_communication_manager.skill_communicate(prompt)
    
    def initialize_story(self) -> AIStoryOutput:
        starting_sentence= "This is the start of the game, begin the story with "
        prompt = f"{starting_sentence} {random.choice(STARTING_PROMPTS)}"
        return self.ai_communication_manager.story_communicate(self.player, {}, prompt)
    
    def get_next_story(self, player_prompt: str, skill_checks: dict[str, int]) -> AIStoryOutput:
        return self.ai_communication_manager.story_communicate(self.player, player_prompt, skill_checks)

    def update_player(self, data: AIStoryOutput) -> None:
        # TODO: Add support for more data
        self.player.xp += data.xp_earned
        for k, v in data.new_items.items():
            self.player.inventory.add_item(v)
        self.player.take_damage(data.damage_taken)

    def get_user_action(self) -> str:
        return self.logger.input("Input your action ('/help' for directions): ")
    
    def perform_skill_checks(self, skill_output: AISkillCheckOutput) -> dict[str, int]:
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