from character_creation.klass.abstract_klass import AbstractKlass
from character_creation.klass.fighter import Fighter


class KlassFactory():
    def create_klass(self, klass_name: str) -> AbstractKlass:
        if klass_name == "Fighter":
            return Fighter()
        else:
            raise ValueError("Invalid class name")