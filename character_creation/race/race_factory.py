from character_creation.race.abstract_race import AbstractRace
from character_creation.race.dwarf import Dwarf
from character_creation.race.elf import Elf
from character_creation.race.halfling import Halfling
from character_creation.race.human import Human


class RaceFactory():
    def create_race(self, name: str) -> AbstractRace:
        if name == "Human":
            return Human()
        elif name == "Elf":
            return Elf()
        elif name == "Dwarf":
            return Dwarf()
        elif name == "Halfling":
            return Halfling()
        else:
            raise  