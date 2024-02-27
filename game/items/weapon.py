from .abstract_item import AbstractItem

class Weapon(AbstractItem):
    def to_json(self) -> dict:
        return {}