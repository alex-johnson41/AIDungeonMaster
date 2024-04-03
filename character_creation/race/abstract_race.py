from abc import ABC, abstractmethod

class AbstractRace(ABC):

    @abstractmethod
    def __init__(self):
        self.name = str
        self.ability_score_increase = dict
        self.speed = None

    def to_json(self) -> dict:
        return {
            "name": self.name
        }