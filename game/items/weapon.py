from .abstract_item import AbstractItem

class Weapon(AbstractItem):
    def __init__(self, name: str, range: int):
        self.name = name
        self.range = range

    def to_json(self) -> dict:
        return {
            "type": "weapon",
            "name": self.name,
            "range": self.range
        }