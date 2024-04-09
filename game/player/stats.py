class Stats:
    def __init__(self, strength: int, dexterity: int, constitution: int, intelligence: int, wisdom: int, charisma: int):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def get_modifier(self, ability: str, proficiencies: dict, skill: str) -> int:
        modifier = (self.__getattribute__(ability) - 10) //2
        if skill in proficiencies.keys():
            modifier += proficiencies[skill]
        return modifier
    
    def to_json(self) -> dict:
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
        }
    
    @staticmethod
    def from_json(json: dict) -> dict:
        return Stats(
            json["strength"],
            json["dexterity"],
            json["constitution"],
            json["intelligence"],
            json["wisdom"],
            json["charisma"]
        )