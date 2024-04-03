from abc import ABC, abstractmethod

class AbstractKlass(ABC):

    @abstractmethod
    def __init__(self):
        self.name = str
        self.proficiency_bonus = None
        self.base_hp = None

    def to_json(self) -> dict:
        return {
            "name": self.name
        }