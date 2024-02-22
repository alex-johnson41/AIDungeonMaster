from .stats import Stats

class Skills:
    def __init__(self, skills_dict: dict[str, int]):
        self.acrobatics = skills_dict["acrobatics"]
        self.animal_handling = skills_dict["animal_handling"]
        self.arcana = skills_dict["arcana"]
        self.athletics = skills_dict["athletics"]
        self.deception = skills_dict["deception"]
        self.history = skills_dict["history"]
        self.insight = skills_dict["insight"]
        self.intimidation = skills_dict["intimidation"]
        self.investigation = skills_dict["investigation"]
        self.medicine = skills_dict["medicine"]
        self.nature = skills_dict["nature"]
        self.perception = skills_dict["perception"]
        self.performance = skills_dict["performance"]
        self.persuasion = skills_dict["persuasion"]
        self.religion = skills_dict["religion"]
        self.sleight_of_hand = skills_dict["sleight_of_hand"] 
        self.stealth = skills_dict["stealth"]
        self.survival = skills_dict["survival"]
    