class AISkillCheckOutput:
    def __init__(self, output: str):
        self.output = output
        self.skill_checks: list[str] = eval(output)

    def to_json(self) -> dict:
        return self.skill_checks