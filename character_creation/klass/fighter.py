from character_creation.klass.abstract_klass import AbstractKlass


class Fighter(AbstractKlass):
    def __init__(self):
        self.name = "Fighter"
        self.proficiency_bonus = 2
        self.base_hp = 10