N = 20  
M = 10 
K = 5  

class Hero:
    def __init__(self, hero_name: str) -> None:
        self.hero_name = hero_name
        self.hp = 10
        self.damage = 2
        self.level = 1
        self.coins = 0
        self.defending = False

    def heal(self) -> None:
        self.hp += self.hp * N / 100

    def level_up(self) -> None:
        cost = self.level * K
        if self.coins >= cost:
            self.coins -= cost
            self.level += 1
            self.damage += self.damage * M / 100
            self.hp = 10 + self.level * M / 100
        else:
            print("Not enough coins to level up!")

    def attack(self, monster) -> None:
        monster.reduce_health(self.damage)
        if monster.hp <= 0:
            self.coins += self.level
            print(f"{self.hero_name} defeated {monster.monster_name} and earned {self.level} coins!")

    def defend(self) -> None:
        self.defending = True

    def reduce_health(self, monster) -> None:
        damage_taken = monster.damage * 0.2 if self.defending else monster.damage
        self.hp = max(0, self.hp - damage_taken)
        self.defending = False

    def coins_increase(self, amount: int) -> None:
        self.coins += amount

