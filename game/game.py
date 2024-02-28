from ai_model.abstract_ai_model import AbstractAIModel
from game.die import Die
from game.player.player import Player


class Game:
    def __init__(self, player: Player, story_model: AbstractAIModel, skill_model: AbstractAIModel):
        self.player = player
        self.story_model = story_model
        self.skill_model = skill_model

    def play(self) -> None:
        # TODO: Implement game ending conditions (death, victory, etc.)
        response = self.initialize_story()
        print(eval(response)["story"])
        while (True):
            self.take_turn()

    def take_turn(self) -> None:
        # TODO: Fix this, it's a very rough start and definitely not functional
        player_prompt = self.get_user_action()
        skill_checks = self.perform_skill_checks(self.find_skill_checks(player_prompt))
        print(skill_checks)
        story = self.get_next_story(player_prompt, skill_checks)
        response = self.parse_model_response(story)
        print(response)
        print(response["story"])
        self.update_game(response["data"])

    def find_skill_checks(self, prompt: str) -> list[str]:
        # Continue to prompt and reset the model until it 
        # returns a syntactically correct list
        while (True):
            try: 
                response = self.skill_model.communicate(prompt)
                skill_checks = eval(response) # Converts output to a list
                break
            except:
                self.skill_model.reset()
        return skill_checks
    
    def initialize_story(self) -> None:
        game_data = {
            "player": self.player.to_json(),
            "skill_checks": [],
            "player_action": "This is the start of the game, begin the story with the player waking up outside of a bar hungover."}
        while (True):
            response = self.story_model.communicate(f"{game_data}")
            try: 
                eval(response)
                break
            except:
                self.story_model.reset()
        return response
    
    def get_next_story(self, player_prompt: str, skill_checks: list[str]) -> str:
        game_data = {
            "player": self.player.to_json(),
            "skill_checks": skill_checks,
            "player_action": player_prompt
        }
        return self.story_model.communicate(f"{game_data}")
    
    def parse_model_response(self, response: str) -> dict:
        return eval(response)

    def update_game(self, game_data: dict) -> None:
        self.player.xp += game_data["xp_earned"]
        for item in game_data["new_items"]:
            self.player.inventory.add_item(item)
        self.player.hp -= game_data["damage_taken"]

    def get_user_action(self) -> str:
        return input("Input your action: ")
    
    def perform_skill_checks(self, skill_checks: list[str]) -> dict[str, int]:
        # TODO: Double check that skill checks are always done with a d20
        die = Die(20)
        results = {}
        for skill in skill_checks:
            try:
                results[skill] = die.roll() + self.player.skills.__getattribute__(skill.lower())
            except:
                pass
        return results