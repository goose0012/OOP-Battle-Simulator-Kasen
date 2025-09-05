from enemy import Enemy
import random

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 500

    def flamethrower(self):
        damage = random.randint(20, 50)
        print(f"The dragon used Flamethrower and did {damage} damage!")
        return damage