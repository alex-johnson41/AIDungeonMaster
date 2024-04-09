from character_creation.klass.abstract_klass import AbstractKlass
from character_creation.klass.fighter import Fighter
from character_creation.klass.rogue import Rogue
from character_creation.klass.wizard import Wizard
from character_creation.race.abstract_race import AbstractRace
from character_creation.race.dwarf import Dwarf
from character_creation.race.elf import Elf
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
        name = self.logger.input("\nEnter a name for your character: ")
        race = self.chooseRace()
        klass = self.chooseKlass()
        stats = self.assignStats(race)
        proficiencies = self.pro_skills(klass)
        skills = self.calculateSkills(stats, proficiencies)
        return Player(name, stats, skills, [], 10, klass, race, Inventory(10), 0)
        
    def chooseRace(self) -> AbstractRace:
        # User chooses a race from the listed options and enters the number as input
        self.logger.log("\nChoose a Race for your Character:\n\n1.Human\n2.Elf\n3.Dwarf\n")
        while True:
            choice = self.logger.input("Enter number: ")
            if choice == "1":
                #Human race Selected
                return Human()
            elif choice == "2":
                #Elf race Selected
                return Elf()
            elif choice == "3":
                #Dwarf race Selected
                return Dwarf()
            else:
                #choice is incorrect
                self.logger.log("Please enter the number of your choice.")
                
    def chooseKlass(self) -> AbstractKlass:
        # User chooses a class from the listed options and enters the number as input
        self.logger.log("\nChoose a Class for your Character:\n\n1.Fighter\n2.Wizard\n3.Rogue\n")
        while True:
            choice = self.logger.input("Enter the number of your choice: ")
            if choice == "1":
                #Fighter Class Selected
                return Fighter()
            elif choice == "2":
                #Wizard Class Selected
                return Wizard()
            elif choice == "3":
                #Rogue Class Selected
                return Rogue()
            else:
                #choice is incorrect
                self.logger.log("Please enter the number of your choice.")
                
    def assignStats(self, race: AbstractRace) -> Stats:
        # Values are presented to the use with a list of abilities. The user selects one ability to assign each value.
        # Races have increases for different abilities. Those are added in this function as well.
        values = [15,14,13,12,10,8]
        assignedValues = race.ability_score_increase
        abilities = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
        for value in values:
            self.logger.log("\nWhich Ability would you like to assign a value of " + str(value) + " to?")
            number = 1
            for ability in abilities:
                # Prints list of remaining abilities
                string = str(number) + ". " + str(ability)
                self.logger.log(string)
                number += 1
            input_valid = False
            while (not input_valid):
                try:
                    choice = int(self.logger.input("Enter the number of your choice: "))
                except:
                    self.logger.log("Invalid Input: Please enter the number of your choice")
                else:
                    if choice <= 0 or choice > len(abilities):
                        self.logger.log("Invalid Input: Please enter the number of one of the choices.")
                    else:
                        choiceKey = (abilities[choice-1]).lower()
                        assignedValues.update({choiceKey:value+assignedValues[choiceKey]})
                        abilities.pop(choice-1)
                        input_valid = True
                    
        return Stats(assignedValues.get("strength"), assignedValues.get("dexterity"),
                     assignedValues.get("constitution"), assignedValues.get("intelligence"),
                     assignedValues.get("wisdom"), assignedValues.get("charisma"))
            
    def calculateSkills(self, stats: Stats, proficiencies: dict) -> Skills:
        # Calculates the modifier of each skill from the ability scores. Each skill and it's modifier is printed for the user to see.
        all_skills = {"acrobatics": "dexterity","animal handling":"wisdom","arcana":"intelligence","athletics":"strength",
                      "deception": "charisma","history": "intelligence","insight": "wisdom","intimidation": "charisma",
                      "investigation": "intelligence","medicine": "wisdom","nature": "intelligence","perception": "wisdom",
                      "performance": "charisma","persuasion": "charisma","religion": "intelligence","sleight of hand": "dexterity",
                      "stealth": "dexterity","survival": "wisdom"}
        skill_mods = {}
        self.logger.log("\nHere are your character's skill modifiers:")
        for key in all_skills:
            modifier = stats.get_modifier(all_skills[key], proficiencies, key)
            underscore_key = key.replace(" ", "_")
            skill_mods[underscore_key] = modifier
            self.logger.log((key.title()) + " = " + str(modifier))
        self.logger.log("")
        return Skills(skill_mods)
        
    def pro_skills(self, klass: AbstractKlass) -> dict:
        # Returns a dictionary of proficient skills chosen by the user. The value of each skill is the proficiency bonus for 
        # that skill
        all_skills = ["Acrobatics","Animal Handling","Arcana","Athletics","Deception","History",
                      "Insight","Intimidation","Investigation","Medicine","Nature","Perception",
                      "Performance","Persuasion","Religion","Sleight of Hand","Stealth", "Survival"]
        chosen_skills = {}
        skill_list = klass.skill_List
        skills_to_choose = klass.skills_to_choose
        self.logger.log("\nSelect skills based on the Class you have chosen.")
        while skills_to_choose > 0:
            number = 1
            self.logger.log("Select a skill to be proficient in:")
            for skill in skill_list:
                string = str(number) + ". " + str(skill)
                self.logger.log(string)
                number += 1
            input_valid = False
            while (not input_valid):
                # Get user input. Use try to make sure input is an integer. 
                try:
                    choice = int(self.logger.input("Enter the number of your choice: "))
                except:
                    self.logger.log("Invalid Input: Please enter the number of your choice")
                else:
                    # check to make sure choice is between zero and len(skill_list)
                    if choice <= 0 or choice > len(skill_list):
                        self.logger.log("Invalid Input: Please enter the number of one of the choices.")
                    else:
                        self.logger.log("")
                        all_skills.remove(skill_list[choice-1])
                        choice_key = (skill_list[choice-1]).lower()
                        skill_list.pop(choice-1)
                        skills_to_choose -= 1
                        chosen_skills[choice_key] = klass.proficiency_bonus
                        input_valid = True
        skills_to_choose = 4 - klass.skills_to_choose
        self.logger.log("\nSelect additional skills to be proficient in.")
        while skills_to_choose > 0:
            number = 1
            self.logger.log("Select a skill to be proficient in:")
            for skill in all_skills:
                string = str(number) + ". " + str(skill)           
                self.logger.log(string)
                number += 1
            input_valid = False
            while (not input_valid):
                # Get user input. Use try to make sure input is an int.
                try:
                    choice = int(self.logger.input("Enter the number of your choice: "))
                except:
                    self.logger.log("Invalid Input: Please enter the number of your choice")
                else:
                    # check to make sure choice is between zero and len(all_skills)
                    if choice <= 0 or choice > len(all_skills):
                        self.logger.log("Invalid Input: Please enter the number of one of the choices.")
                    else:
                        self.logger.log("")
                        choice_key = (all_skills[choice-1]).lower()
                        all_skills.pop(choice-1)
                        skills_to_choose -= 1
                        chosen_skills[choice_key] = klass.proficiency_bonus
                        input_valid = True
        return chosen_skills
            