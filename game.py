import random
from goblin import Goblin
from hero import Hero
from boss import Dragon

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Sukuna")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]

    defeated_goblins = 0
    round_count = 0
    boss_triggered = False
    boss = Dragon("Dragon")

# Fight loop stuff 
    while hero.is_alive():
        round_count += 1
        print(f"\nNew Round! (Round {round_count})")
        if not boss_triggered:
            if not hasattr(hero, 'divine_flame_rounds') or hero.divine_flame_rounds == 0:
                if random.random() < 0.10:
                    print(hero.divine_flame())
            if hasattr(hero, 'divine_flame_rounds') and hero.divine_flame_rounds > 0:
                hero.divine_flame_rounds -= 1
            if any(goblin.is_alive() for goblin in goblins):
                target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
                damage = hero.strike()
                print(f"{hero.name} attacks {target_goblin.name} for {damage} damage!")
                target_goblin.take_damage(damage)
                if not target_goblin.is_alive():
                    defeated_goblins += 1
                    hero.total_damage_dealt += damage
                    hero.rounds_survived += 1
                    print(f"{target_goblin.name} has been defeated!")
                for goblin in goblins:
                    if goblin.is_alive():
                        damage = goblin.attack()
                        print(f"{goblin.name} attacks {hero.name} for {damage} damage!")
                        hero.receive_damage(damage)
            if defeated_goblins == len(goblins):
                print("Boss time!")
                boss_triggered = True
        else:
            damage = hero.strike()
            boss.take_damage(damage)
            print(f"{hero.name} attacks {boss.name} for {damage} damage!")
            if not boss.is_alive():
                print(f"Boss {boss.name} defeated!")
                break
            damage = boss.flamethrower() if random.random() < 0.5 else boss.tail_swipe()
            hero.receive_damage(damage)
            print(f"{boss.name} attacks {hero.name} for {damage} damage!")

    if hero.is_alive():
        print(f"\n{hero.name} survived! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\n{hero.name} has been defeated. Game Over. (｡•́︿•̀｡)")

    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    print(f"Total damage dealt by hero: {hero.total_damage_dealt}")
    print(f"Rounds Survived: {hero.rounds_survived}")

if __name__ == "__main__":
    main()
