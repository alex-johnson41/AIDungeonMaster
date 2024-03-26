from character_creation.klass.fighter import Fighter
from character_creation.race.human import Human
from game.inventory import Inventory
from game.player.player import Player
from game.player.skills import Skills
from game.player.stats import Stats
from logger import Logger

class CharacterCreator:
    def __init__(self, logger: Logger):
        self.logger = logger

    def create_character(self) -> Player:
        name = input("Enter a name for your character: ")
        race = self.chooseRace()
        stats = Stats(10, 10, 10, 10, 10, 10)
        skills = Skills({"acrobatics": 0, "animal_handling": 0, "arcana": 0, "athletics": 0, "deception": 0, 
                     "history": 0, "insight": 0, "intimidation": 0, "investigation": 0, "medicine": 0, 
                     "nature": 0, "perception": 0, "performance": 0, "persuasion": 0, "religion": 0, 
                     "sleight_of_hand": 0, "stealth": 0, "survival": 0
                     })
        return Player(name, stats, skills, [], 10, Fighter(), Human(), Inventory(10), 0)

        
    def chooseRace(self):
        self.logger.log("Choose a Race for your Character:\n\n1.Human\n2.Elf (Not Available)\n3.Dwarf (Not Available)\n")
        while True:
            choice = int(input("Enter number: "))
            if choice == 1:
                #Human race Selected
                return Human()
            elif choice == 2:
                #Elf race Selected
                pass
            elif choice == 3:
                #Dwarf race Selected
                pass
            else:
                #choice is incorrect
                self.logger.log("Please enter the number of your choice.")
