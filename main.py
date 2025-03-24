from hero import Hero
from monster import Monster

def choose_action(hero, monster):
    print(f"{hero.hero_name} HP: {hero.hp}, Coins: {hero.coins}, Level: {hero.level}")
    valid_actions = ["attack", "level up", "heal", "defend"]
    action = input("Choose action (attack/level up/heal/defend): ").strip().lower()

    if action not in valid_actions:
        print("Invalid action!")
        return False  

    hero.coins += 1 

    if action == "attack":
        hero.attack(monster)
    elif action == "level up":
        hero.level_up()
    elif action == "heal":
        hero.heal()
    elif action == "defend":
        hero.defend()
    return True 

def main():
    hero_name = input("Enter hero name: ")
    hero = Hero(hero_name)
    monster = Monster("Goblin", hero.level)

    while hero.hp > 0:
        if choose_action(hero, monster): 
            if monster.hp <= 0:
                monster = Monster("Orc", hero.level)
            monster.attack(hero)
            if hero.hp <= 0:
                print("Game Over!")
                break
        else:
            print("Please enter a valid action.") 

if __name__ == "__main__":
    main()