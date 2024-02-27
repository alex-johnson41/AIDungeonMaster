from abc import ABC, abstractmethod

class AbstractKlass(ABC):

    @abstractmethod
    def __init__(self):
        self.proficiency_bonus = None
        self.base_hp = None