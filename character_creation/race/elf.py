from character_creation.race.abstract_race import AbstractRace


class Elf(AbstractRace):
    def __init__(self):
        self.name = "Elf"
        self.ability_score_increase = { 
            "strength": 0, 
            "dexterity": 2, 
            "constitution": 0, 
            "intelligence": 0, 
            "wisdom": 0, 
            "charisma": 0,
            }
        self.speed = 30