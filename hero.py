from colors import RED, GREEN, YELLOW, BLUE, MAGENTA, RESET

# Hero Constants
HERO_HEAL_PERCENT = 20
HERO_LEVEL_UP_STAT_INCREASE = 10
HERO_LEVEL_UP_COST_MULTIPLIER = 5

class Hero:
    def __init__(self, hero_name: str) -> None:
        self.hero_name = hero_name
        self.hp = 10
        self.damage = 2
        self.level = 1
        self.coins = 0
        self.defending = False

    def heal(self) -> None:
        original_hp = self.hp
        self.hp += self.hp * HERO_HEAL_PERCENT / 100
        print(f"{GREEN}{self.hero_name} healed for {self.hp - original_hp:.2f} HP!{RESET}")

    def level_up(self) -> bool:
        cost = self.level * HERO_LEVEL_UP_COST_MULTIPLIER
        if self.coins >= cost:
            self.coins -= cost
            self.level += 1
            self.damage += self.damage * HERO_LEVEL_UP_STAT_INCREASE / 100
            self.hp = 10 + self.level * HERO_LEVEL_UP_STAT_INCREASE / 100
            print(f"{BLUE}{self.hero_name} leveled up to level {self.level}!{RESET}")
            return True
        else:
            return False

    def attack(self, monster) -> None:
        monster.reduce_health(self.damage)
        if monster.hp <= 0:
            self.coins += self.level
            print(f"{GREEN}{self.hero_name} defeated {monster.monster_name} and earned {self.level} coins!{RESET}")
        else:
            print(f"{YELLOW}{self.hero_name} attacked {monster.monster_name}!{RESET}")

    def defend(self) -> None:
        self.defending = True
        print(f"{MAGENTA}{self.hero_name} is defending against the next attack!{RESET}")

    def reduce_health(self, monster) -> None:
        damage_taken = monster.damage * 0.2 if self.defending else monster.damage
        self.hp = max(0, self.hp - damage_taken)
        self.defending = False

    def coins_increase(self, amount: int) -> None:
        self.coins += amount