from game.die import Die


class Attack:
    def __init__(self, name: str, bonus: int, range: int, damage: Die):
        self.name = name
        self.bonus = bonus
        self.range = range
        self.damage = damage

    def attack(self, range: int) -> int:
        return 0 if range > self.range else self.damage.roll() + self.bonus 
    
    def to_json(self) -> dict:
        return {
            "name": self.name,
            "bonus": self.bonus,
            "range": self.range,
            "damage": self.damage.to_string()
        }