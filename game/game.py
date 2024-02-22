from typing import List
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

    def find_skill_checks(self, prompt: str) -> List[str]:
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