from game.player.race.abstract_race import AbstractRace


class Human(AbstractRace):
    def __init__(self):
        self.ability_score_increase = {
            "strength": 1, 
            "dexterity": 1, 
            "constitution": 1, 
            "intelligence": 1, 
            "wisdom": 1, 
            "charisma": 1,
            }
        self.speed = 30