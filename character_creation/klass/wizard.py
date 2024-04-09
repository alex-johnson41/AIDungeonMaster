from character_creation.klass.abstract_klass import AbstractKlass

class Wizard(AbstractKlass):
    def __init__(self):
        self.name = "Wizard"
        self.proficiency_bonus = 2
        self.base_hp = 6
        self.skill_List = ["Arcana", "History","Insight", 
                           "Investigation", "Medicine", "Religion"]
        self.skills_to_choose = 2
    