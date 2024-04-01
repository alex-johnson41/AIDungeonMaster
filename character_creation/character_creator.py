from character_creation.klass.abstract_klass import AbstractKlass
from character_creation.klass.fighter import Fighter
from character_creation.race.abstract_race import AbstractRace
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
        # Calls different functions that help the user build thier character
        name = input("Enter a name for your character: ")
        race = self.chooseRace()
        klass = self.chooseKlass()
        stats = self.assignStats(race)
        skills = self.calculateSkills(stats)
        return Player(name, stats, skills, [], 10, klass, race, Inventory(10), 0)
        
    def chooseRace(self) -> AbstractRace:
        # User chooses a race from the listed options and enters the number as input
        self.logger.log("Choose a Race for your Character:\n\n1.Human\n2.Elf (Not Available)\n3.Dwarf (Not Available)\n")
        while True:
            choice = input("Enter number: ")
            if choice == "1":
                #Human race Selected
                return Human()
            elif choice == "2":
                #Elf race Selected
                self.logger.log("Elf is not available at this time. Please make another choice.")
            elif choice == "3":
                #Dwarf race Selected
                self.logger.log("Dwarf is not available at this time. Please make another choice.")
            else:
                #choice is incorrect
                self.logger.log("Please enter the number of your choice.")
                
    def chooseKlass(self) -> AbstractKlass:
        # User chooses a class from the listed options and enters the number as input
        self.logger.log("Choose a Class for your Character:\n\n1.Fighter\n2.Wizard (Not Available)\n3.Rogue (Not Available)\n")
        while True:
            choice = input("Enter the number of your choice: ")
            if choice == "1":
                #Fighter Class Selected
                return Fighter()
            elif choice == "2":
                #Wizard Class Selected
                self.logger.log("Wizard is not available at this time. Please make another choice.")
            elif choice == "3":
                #Rogue Class Selected
                self.logger.log("Rogue is not available at this time. Please make another choice.")
            else:
                #choice is incorrect
                self.logger.log("Please enter the number of your choice.")
                
    def assignStats(self, race) -> Stats:
        # Values are presented to the use with a list of abilities. The user selects one ability to assign each value.
        # Races have increases for different abilities. Those are added in this function as well.
        values = [15,14,13,12,10,8]
        assignedValues = race.ability_score_increase
        abilities = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
        for value in values:
            self.logger.log("\nWhich Ability would you like to assign a value of " + str(value) + " to?")
            number = 1
            for ability in abilities:
                string = str(number) + ". " + str(ability)
                self.logger.log(string)
                number += 1
            choice = int(input("Enter the number of your choice: "))
            # The input for variable 'choice' needs checks
            # Must be an integer between 1 and len(abilities)
            choiceKey = (abilities[choice-1]).lower()
            assignedValues.update({choiceKey:value+assignedValues[choiceKey]})
            abilities.pop(choice-1)
        return Stats(assignedValues.get("strength"), assignedValues.get("dexterity"),
                     assignedValues.get("constitution"), assignedValues.get("intelligence"),
                     assignedValues.get("wisdom"), assignedValues.get("charisma"))
            
    def calculateSkills(self, stats) -> Skills:
        # Calculates the modifier of each skill from the ability scores. Each skill and it's modifier is printed for the user to see.
        self.logger.log("\nHere are your character's skill modifiers:")
        acrobatics = stats.get_modifier("dexterity")
        self.logger.log("Acrobatics = "+str(acrobatics))
        animal_handling = stats.get_modifier("wisdom")
        self.logger.log("Animal Handling = "+str(animal_handling))
        arcana = stats.get_modifier("intelligence")
        self.logger.log("Arcana = "+str(arcana))
        athletics = stats.get_modifier("strength")
        self.logger.log("Athletics = "+str(athletics))
        deception = stats.get_modifier("charisma")
        self.logger.log("Deception = "+str(deception))
        history = stats.get_modifier("intelligence")
        self.logger.log("History = "+str(history))
        insight = stats.get_modifier("wisdom")
        self.logger.log("Insight = "+str(insight))
        intimidation = stats.get_modifier("charisma")
        self.logger.log("Intimidation = "+str(intimidation))
        investigation = stats.get_modifier("intelligence")
        self.logger.log("Investigation = "+str(investigation))
        medicine = stats.get_modifier("wisdom")
        self.logger.log("Medicine = "+str(medicine))
        nature = stats.get_modifier("intelligence")
        self.logger.log("Nature = "+str(nature))
        perception = stats.get_modifier("wisdom")
        self.logger.log("Perception = "+str(perception))
        performance = stats.get_modifier("charisma")
        self.logger.log("Performance = "+str(performance))
        persuation = stats.get_modifier("charisma")
        self.logger.log("Persuation = "+str(persuation))
        religion = stats.get_modifier("intelligence")
        self.logger.log("Religion = "+str(religion))
        sleight_of_hand = stats.get_modifier("dexterity")
        self.logger.log("Sleight of Hand = "+str(sleight_of_hand))
        stealth = stats.get_modifier("dexterity")
        self.logger.log("Stealth = "+str(stealth))
        survival = stats.get_modifier("wisdom")
        self.logger.log("Survival = "+str(survival))
        
        return Skills({"acrobatics": acrobatics, "animal_handling": animal_handling, "arcana": arcana, "athletics": athletics,
                       "deception": deception, "history": history, "insight": insight, "intimidation": intimidation,
                       "investigation": investigation, "medicine": medicine, "nature": nature, "perception": perception, 
                       "performance": performance, "persuasion": persuation, "religion": religion, "sleight_of_hand": sleight_of_hand,
                       "stealth": stealth, "survival": survival})
                     