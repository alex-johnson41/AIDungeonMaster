from .abstract_item import AbstractItem

class Currency(AbstractItem):
    def __init__(self, value: int):
        self.value = value
    
    def to_json(self) -> dict:
        return {
            "value": self.value
        }

    def add(self, amount: int) -> None:
        self.value += amount
    
    def remove(self, amount: int) -> None:
        self.value = amount if amount < self.value else 0