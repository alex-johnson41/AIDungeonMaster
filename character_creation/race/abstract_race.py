from abc import ABC, abstractmethod

class AbstractRace(ABC):

    @abstractmethod
    def __init__(self):
        self.ability_score_increase = dict
        self.speed = None