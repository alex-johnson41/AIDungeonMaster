class Stats:
    def __init__(self, strength: int, dexterity: int, constitution: int, intelligence: int, wisdom: int, charisma: int):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def get_modifier(self, ability: str) -> int:
        return (self.__getattribute__(ability) - 10) // 2
    
    def to_json(self) -> dict:
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
        }