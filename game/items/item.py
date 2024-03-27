from game.items.abstract_item import AbstractItem


class Item(AbstractItem):
    def __init__(self, name: str):
        self.name = name

    def to_json(self) -> dict:
        return {
            "name": self.name
        }