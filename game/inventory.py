from .items.abstract_item import AbstractItem

class Inventory:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: list[AbstractItem] = []

    def add_item(self, item: AbstractItem) -> None:
        if len(self.items) >= self.capacity:
            raise ValueError('Inventory is full')
        self.items.append(item)

    def remove_item(self, item: AbstractItem) -> None:
        self.items.remove(item)

    def to_json(self) -> dict:
        return {
            "capacity": self.capacity,
            "items": [item.to_json() for item in self.items]
        }