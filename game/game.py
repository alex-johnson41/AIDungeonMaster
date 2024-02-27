from ai_model.abstract_ai_model import AbstractAIModel
from game.player.player import Player


class Game:
    def __init__(self, player: Player, story_model: AbstractAIModel, skill_model: AbstractAIModel):
        self.player = player
        self.story_model = story_model
        self.skill_model = skill_model

    def play(self) -> None:
        pass

    def take_turn(self) -> None:
        pass

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
    
    def prompt_model(self, player_prompt: str, skill_checks: list[str]) -> str:
        game_data = {
            "player": self.player.to_json(),
            "skill_checks": skill_checks
        }
        return self.story_model.communicate(f"{game_data}\n{player_prompt}")