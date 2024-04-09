from character_creation.race.abstract_race import AbstractRace


class Dwarf(AbstractRace):
    def __init__(self):
        self.name = "Dwarf"
        self.ability_score_increase = { 
            "strength": 0, 
            "dexterity": 0, 
            "constitution": 2, 
            "intelligence": 0, 
            "wisdom": 0, 
            "charisma": 0, 
            }
        self.speed = 25