class Stats:
    def __init__(self, strength: int, dexterity: int, constitution: int, intelligence: int, wisdom: int, charisma: int):
        self.stregth = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def get_modifier(self, ability: str) -> int:
        return (self.__getattribute__(ability) - 10) // 2