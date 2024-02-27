from game.inventory import Inventory
from .attack import Attack
from character_creation.klass.abstract_klass import AbstractKlass
from character_creation.race.abstract_race import AbstractRace
from .stats import Stats
from .skills import Skills

class Player:
    def __init__(self, name: str, stats: Stats, skills: Skills, attacks: list[Attack],
                 hp_max: int, klass: AbstractKlass, race: AbstractRace, inventory: Inventory,
                 armor: int
                 ):
        self.name = name
        self.stats = stats
        self.skills = skills
        self.attacks = attacks
        self.level = 1
        self.hp = hp_max
        self.hp_max = hp_max
        self.klass = klass
        self.race = race
        self.inventory = inventory
        self.armor = armor
        self.speed = race.speed

    def level_up(self) -> None:
        self.level += 1
        #TODO: Do anything else that needs to happen when a player levels up

    def attack(self, attack_name: str) -> int:
        for attack in self.attacks:
            if attack.name == attack_name:
                return attack.attack()
        return 0
    
    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        #TODO: Implement death
    
    def heal(self, hp: int) -> None:
        self.hp += hp
        if self.hp > self.hp_max:
            self.hp = self.hp_max

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "stats": self.stats.to_json(),
            "skills": self.skills.to_json(),
            "attacks": [attack.to_json() for attack in self.attacks],
            "level": self.level,
            "hp": self.hp,
            "hp_max": self.hp_max,
            "inventory": self.inventory.to_json(),
            "armor": self.armor,
            "speed": self.speed,
        }