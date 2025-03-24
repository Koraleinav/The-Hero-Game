from colors import RED, YELLOW, RESET
import random

# Monster Constants
MONSTER_HP_MULTIPLIER = 5
MONSTER_DAMAGE_MULTIPLIER = 2

class Monster:
    def __init__(self, monster_name: str, current_hero_level: int) -> None:
        self.monster_name = monster_name
        self.level = random.choice([current_hero_level - 1, current_hero_level, current_hero_level + 1])
        self.hp = self.level * MONSTER_HP_MULTIPLIER
        self.damage = self.level * MONSTER_DAMAGE_MULTIPLIER

    def attack(self, hero) -> None:
        hero.reduce_health(self)
        print(f"{RED}{self.monster_name}{RESET} attacked {YELLOW}{hero.hero_name}{RESET}")

    def reduce_health(self, damage: int) -> None:
        self.hp = max(0, self.hp - damage)