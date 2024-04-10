from character_creation.klass.abstract_klass import AbstractKlass
from character_creation.klass.cleric import Cleric
from character_creation.klass.fighter import Fighter
from character_creation.klass.rogue import Rogue
from character_creation.klass.wizard import Wizard


class KlassFactory():
    def create_klass(self, klass_name: str) -> AbstractKlass:
        if klass_name == "Fighter":
            return Fighter()
        elif klass_name == "Wizard":
            return Wizard()
        elif klass_name == "Rogue":
            return Rogue()
        elif klass_name == "Cleric":
            return Cleric()
        else:
            raise ValueError("Invalid class name")