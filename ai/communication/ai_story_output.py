class AIStoryOutput:
    def __init__(self, output: str):
        self.output = output
        self.process_output()

    def process_output(self) -> None:
        # TODO: Add support for more data
        eval_output = eval(self.output)
        data = eval_output["data"]
        self.story = eval_output["story"]
        self.xp_earned = data["xp_earned"]
        self.new_items = data["new_items"]
        self.damage_taken = data["damage_taken"]

    def to_json(self) -> dict:
        return {
            "story": self.story,
            "xp_earned": self.xp_earned,
            "new_items": self.new_items,
            "damage_taken": self.damage_taken
        }