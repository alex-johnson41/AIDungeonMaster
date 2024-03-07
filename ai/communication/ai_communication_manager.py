from ai.communication.ai_skill_check_output import AISkillCheckOutput
from ai.models.abstract_ai_model import AbstractAIModel
from ai.communication.ai_story_output import AIStoryOutput
from game.player.player import Player


class AICommunicationManager():
    def __init__(self, story_model: AbstractAIModel, skill_model: AbstractAIModel):
        self.story_model = story_model
        self.skill_model = skill_model

    def story_communicate(self, player: Player, user_prompt: str, skill_checks_dict: dict[str, int]) -> AIStoryOutput:
        prompt = f"{self.format_story_prompt(player, user_prompt, skill_checks_dict)}" 
        output = self.repeat_prompt(prompt, True)
        return AIStoryOutput(output)
    
    def skill_communicate(self, prompt: str) -> AISkillCheckOutput:
        output = self.repeat_prompt(prompt, False)
        return AISkillCheckOutput(output)

    def format_story_prompt(self, player: Player, prompt: str, skill_checks: dict[str, int]) -> str:
        return {
            "player": player.to_json(),
            "skill_checks": skill_checks,
            "player_action": prompt
            }
    
    def repeat_prompt(self, prompt: str, is_story: bool) -> str:
        # Repeat the prompt until the model returns a syntactically correct response
        while True:
            output = self.story_model.communicate(prompt) if is_story else self.skill_model.communicate(prompt)
            try:
                eval(output)
                break
            except:
                if is_story:
                    self.story_model.reset()
                else:
                    self.skill_model.reset()
        return output