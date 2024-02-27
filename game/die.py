from random import randint

class Die:
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self) -> int:
        return randint(1, self.sides)
    
    def to_string(self) -> str:
        return f"1d{self.sides}"