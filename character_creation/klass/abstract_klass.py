from abc import ABC, abstractmethod

class AbstractKlass(ABC):

    @abstractmethod
    def __init__(self):
        self.name = str
        self.proficiency_bonus = None
        self.base_hp = None
        self.skill_List = list
        self.skills_to_choose = None

    def to_json(self) -> dict:
        return {
            "name": self.name
        }