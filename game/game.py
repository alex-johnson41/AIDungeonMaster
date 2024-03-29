from ai.communication.ai_communication_manager import AICommunicationManager
from ai.communication.ai_story_output import AIStoryOutput
from ai.communication.ai_skill_check_output import AISkillCheckOutput
from game.die import Die
from game.player.player import Player
from logger import Logger


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
        # TODO: Fix this, it's a very rough start and can be cleaned up
        # It's farily cleaned up now but it could be better/easier to follow
        player_prompt = self.get_user_action()
        skill_checks = self.perform_skill_checks(self.find_skill_checks(player_prompt)) 
        response = self.get_next_story(player_prompt, skill_checks)
        self.update_player(response)

        self.logger.debug_log(skill_checks)
        self.logger.debug_log(response.to_json()) 
        self.logger.log(response.story)

    def find_skill_checks(self, prompt: str) -> AISkillCheckOutput:
        return self.ai_communication_manager.skill_communicate(prompt)
    
    def initialize_story(self) -> AIStoryOutput:
        # TODO: Add a file with a list of prompts to start the game with and pick one at random
        # Maybe add support for the user to input their own starting prompt
        prompt = "This is the start of the game, begin the story with the player waking up outside of a bar hungover."
        return self.ai_communication_manager.story_communicate(self.player, {}, prompt)
    
    def get_next_story(self, player_prompt: str, skill_checks: dict[str, int]) -> AIStoryOutput:
        return self.ai_communication_manager.story_communicate(self.player, player_prompt, skill_checks)

    def update_player(self, data: AIStoryOutput) -> None:
        # TODO: Add support for more data
        # Also maybe we move this function to a different class, idk where tho
        self.player.xp += data.xp_earned
        for item in data.new_items:
            self.player.inventory.add_item(item)
        self.player.hp -= data.damage_taken

    def get_user_action(self) -> str:
        return input("Input your action: ")
    
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