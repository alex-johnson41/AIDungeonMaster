from .items.abstract_item import AbstractItem

class Inventory:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []

    def add_item(self, item: AbstractItem) -> None:
        if len(self.items) >= self.capacity:
            raise ValueError('Inventory is full')
        self.items.append(item)

    def remove_item(self, item: AbstractItem) -> None:
        self.items.remove(item)