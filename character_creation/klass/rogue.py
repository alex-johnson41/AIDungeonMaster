from character_creation.klass.abstract_klass import AbstractKlass

class Rogue(AbstractKlass):
    def __init__(self):
        self.name = "Rogue"
        self.proficiency_bonus = 2
        self.base_hp = 8
        self.skill_List = ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", 
                           "Perception", "Performance", "Persuation", "Sleight of Hand", "Stealth"]
        self.skills_to_choose = 4