from enemy import Enemy
import random

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500
        self.attack_power = 30

    def flamethrower(self):
        damage = random.randint(20, 50)
        print(f"The dragon used Flamethrower and did {damage} damage!")
        return damage
    
    def tail_swipe(self):
        damage = random.randint(20, 100)
        print(f"The dragon used Tail Swipe and did {damage} damage!")
        return damage