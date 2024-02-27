from game.player.race.abstract_race import AbstractRace


class Human(AbstractRace):
    def __init__(self):
        self.ability_score_increase = [1, 1, 1, 1, 1, 1]
        self.speed = 30