from character_creation.race.abstract_race import AbstractRace
from character_creation.race.human import Human


class RaceFactory():
    def create_race(self, name: str) -> AbstractRace:
        if name == "Human":
            return Human()
        elif name == "Elf":
            pass
        elif name == "Dwarf":
            pass
        elif name == "Halfling":
            pass
        else:
            raise  