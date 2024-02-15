from random import randint

class Die:
    def __init__(self, sides: int):
        self.sides = sides

    def roll(self) -> int:
        return randint(1, self.sides)