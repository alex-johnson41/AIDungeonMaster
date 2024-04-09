from character_creation.klass.abstract_klass import AbstractKlass

class Fighter(AbstractKlass):
    def __init__(self):
        self.name = "Fighter"
        self.proficiency_bonus = 2
        self.base_hp = 10
        self.skill_List = ["Acrobatics", "Animal Handling", "Athletics", "History",
                      "Insight", "Intimidation", "Perception", "Survival"]
        self.skills_to_choose = 2