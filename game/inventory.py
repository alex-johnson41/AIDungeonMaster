from __future__ import annotations
from game.items.currency import Currency
from game.items.item import Item
from game.items.weapon import Weapon
from .items.abstract_item import AbstractItem

class Inventory:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: list[AbstractItem] = []

    def add_item(self, item_data: dict) -> None:
        if len(self.items) >= self.capacity:
            raise ValueError('Inventory is full')
        new_item = self.create_item(item_data)
        self.items.append(new_item)

    def remove_item(self, item_name: str) -> None:
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return

    def create_item(self, item_data: dict) -> AbstractItem:
        if item_data["type"] == 'weapon':
            return Weapon(item_data["name"], item_data["range"])
        elif item_data["type"] == 'currency':
            return Currency(item_data["value"])
        else:
            return Item(item_data["name"])

    def to_json(self) -> dict:
        return {
            "capacity": self.capacity,
            "items": [item.to_json() for item in self.items]
        }
    
    @staticmethod
    def from_json(json: dict) -> Inventory:
        inventory = Inventory(json["capacity"])
        for item_data in json["items"]:
            inventory.add_item(item_data)
        return inventory