from abc import ABC, abstractmethod

class AbstractItem(ABC):
    @abstractmethod
    def to_json(self) -> dict:
        pass