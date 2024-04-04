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
        name = self.logger.input("\nEnter a name for your character: ")
        race = self.chooseRace()
        klass = self.chooseKlass()
        stats = self.assignStats(race)
        proficiencies = self.pro_skills(klass)
        skills = self.calculateSkills(stats, proficiencies)
        return Player(name, stats, skills, [], 10, klass, race, Inventory(10), 0)
        
    def chooseRace(self) -> AbstractRace:
        # User chooses a race from the listed options and enters the number as input
        self.logger.log("\nChoose a Race for your Character:\n\n1.Human\n2.Elf (Not Available)\n3.Dwarf (Not Available)\n")
        while True:
            choice = self.logger.input("Enter number: ")
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
        self.logger.log("\nChoose a Class for your Character:\n\n1.Fighter\n2.Wizard (Not Available)\n3.Rogue (Not Available)\n")
        while True:
            choice = self.logger.input("Enter the number of your choice: ")
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
            choice = int(self.logger.input("Enter the number of your choice: "))
            # The input for variable 'choice' needs checks
            # Must be an integer between 1 and len(abilities)
            choiceKey = (abilities[choice-1]).lower()
            assignedValues.update({choiceKey:value+assignedValues[choiceKey]})
            abilities.pop(choice-1)
        return Stats(assignedValues.get("strength"), assignedValues.get("dexterity"),
                     assignedValues.get("constitution"), assignedValues.get("intelligence"),
                     assignedValues.get("wisdom"), assignedValues.get("charisma"))
            
    def calculateSkills(self, stats, proficiencies) -> Skills:
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
        
    def pro_skills(self, klass):
        all_skills = ["Acrobatics","Animal Handling","Arcana","Athletics","Deception","History",
                      "Insight","Intimidation","Investigation","Medicine","Nature","Perception",
                      "Performance","Persuasion","Religion","Sleight of Hand","Stealth", "Survival"]
        chosen_Skills = {}
        skill_List = klass.skill_List
        skills_to_choose = 2
        self.logger.log("\nSelect TWO skills based on the Class you have chosen.")
        while skills_to_choose > 0:
            number = 1
            self.logger.log("Select a skill to be proficient in:")
            for skill in skill_List:
                string = str(number) + ". " + str(skill)
                self.logger.log(string)
                number += 1
            choice = int(self.logger.input("Enter the number of your choice: "))
            self.logger.log("")
            # The input for variable 'choice' needs checks
            # Must be an integer between 1 and len(abilities)
            all_skills.remove(skill_List[choice-1])
            choiceKey = (skill_List[choice-1]).lower()
            #chosen_Skills.update({choiceKey:value+assignedValues[choiceKey]})
            skill_List.pop(choice-1)
            skills_to_choose -= 1
            chosen_Skills[choiceKey] = klass.proficiency_bonus
        skills_to_choose = 2
        self.logger.log("\nSelect TWO additional skills to be proficient in.")
        while skills_to_choose > 0:
            number = 1
            self.logger.log("Select a skill to be proficient in:")
            for skill in all_skills:
                string = str(number) + ". " + str(skill)           
                self.logger.log(string)
                number += 1
            choice = int(self.logger.input("Enter the number of your choice: "))
            self.logger.log("")
            choiceKey = (all_skills[choice-1]).lower()
            all_skills.pop(choice-1)
            skills_to_choose -= 1
            chosen_Skills[choiceKey] = klass.proficiency_bonus
        return chosen_Skills
            