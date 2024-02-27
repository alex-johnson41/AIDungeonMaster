from ai_model.abstract_ai_model import AbstractAIModel
from game.player.player import Player


class Game:
    def __init__(self, player: Player, story_model: AbstractAIModel, skill_model: AbstractAIModel):
        self.player = player
        self.story_model = story_model
        self.skill_model = skill_model

    def play(self) -> None:
        # TODO: Implement game ending conditions (death, victory, etc.)
        while (True):
            self.take_turn()

    def take_turn(self) -> None:
        # TODO: Fix this, it's a very rough start and definitely not functional
        player_prompt = self.get_user_action()
        skill_checks = self.find_skill_checks(player_prompt)
        story = self.get_next_story(player_prompt, skill_checks)
        game_data = self.parse_model_response(story)
        self.update_game(game_data)

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
    
    def get_next_story(self, player_prompt: str, skill_checks: list[str]) -> str:
        game_data = {
            "player": self.player.to_json(),
            "skill_checks": skill_checks
        }
        return self.story_model.communicate(f"{game_data}\n{player_prompt}")
    
    def parse_model_response(self, response: str) -> dict:
        # TODO: We need to come up with some way to parse the model's response and 
        # update the game state accordingly. Maybe have the model return json?
        pass

    def update_game(self, game_data: dict) -> None:
        # TODO: Update the game/player data based on the model's response
        # Not sure what the input will look like yet
        pass

    def get_user_action(self) -> str:
        return input("Input your action")