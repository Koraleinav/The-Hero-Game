from hero import Hero
from monster import Monster
from colors import RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, BOLD, RESET

def choose_action(hero, monster):
    print(f"\n{CYAN}{'-' * 40}{RESET}")
    hero_name_display = f"{BOLD}{BLUE}[ {hero.hero_name} ]{RESET}"
    print(f"{hero_name_display}'s Turn:")
    print(f"  HP: {YELLOW}{hero.hp:.2f}{RESET}, Coins: {YELLOW}{hero.coins}{RESET}, Level: {BLUE}{hero.level}{RESET}")
    print(f"  Monster: {RED}{monster.monster_name}{RESET}, HP: {monster.hp}, Level: {monster.level}")
    print(f"{CYAN}{'-' * 40}{RESET}")

    print(f"{MAGENTA}Choose your action:{RESET}")
    print("1. Attack (Deal damage to the monster)")
    print("2. Level Up (Increase stats, costs coins)")
    print("3. Heal (Restore HP)")
    print("4. Defend (Reduce damage from next attack)")

    while True:
        try:
            action_choice = int(input(f"\n{GREEN}Enter action number: {RESET}{YELLOW}>> {RESET}"))
            if 1 <= action_choice <= 4:
                break
            else:
                print(f"{BOLD}{RED}Invalid choice. Please enter a number between 1 and 4.{RESET}")
        except ValueError:
            print(f"{BOLD}{RED}Invalid input. Please enter a number.{RESET}")

    if action_choice == 1:
        hero.attack(monster)
        return True
    elif action_choice == 2:
        if hero.level_up():
            return True
        else:
            print(f"{BOLD}{YELLOW}Not enough coins to level up!{RESET}")
            return True
    elif action_choice == 3:
        hero.heal()
        return True
    elif action_choice == 4:
        hero.defend()
        return True

def main():
    print(f"\n{YELLOW}{'=' * 40}{RESET}")
    hero_name = input(f"{BOLD}{MAGENTA}  Enter your Hero's name:  {RESET}")
    print(f"{YELLOW}{'=' * 40}{RESET}")
    hero = Hero(hero_name)
    monster = Monster("Goblin", hero.level)

    while hero.hp > 0:
        if choose_action(hero, monster):
            if monster.hp <= 0:
                monster = Monster("Orc", hero.level)
            monster.attack(hero)
            if hero.hp <= 0:
                print(f"\n{RED}{'=' * 40}{RESET}")
                print(f"{RED}GAME OVER!{RESET}")
                print(f"{RED}{'=' * 40}{RESET}")
                break

if __name__ == "__main__":
    main()