from game.die import Die


class Attack:
    def __init__(self, name: str, bonus: int, range: int, damage: Die):
        self.name = name
        self.bonus = bonus
        self.range = range
        self.damage = damage

    def attack(self, range: int) -> int:
        if range > self.range:
            return 0
        return self.damage.roll() + self.bonus