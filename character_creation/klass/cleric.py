from character_creation.klass.abstract_klass import AbstractKlass
from game.player.stats import Stats

class Cleric(AbstractKlass):
    def __init__(self):
        self.name = "Cleric"
        self.proficiency_bonus = 2
        self.base_hp = 8
        self.skill_List = ["History","Insight", "Medicine", "Persuation", "Religion"]
        self.skills_to_choose = 2
    