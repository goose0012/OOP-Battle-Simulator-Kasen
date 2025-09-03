import random


class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.defense = random.randint(5, 15)
        self.attack_power = random.randint(10, 20)
        self.ultimate_ability = "Thank you king!"
        #TODO Set the hero's name.
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
    

    def strike(self):
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
        return random.randint(1, self.attack_power)

    def receive_damage(self, damage):
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
        net_damage = damage - self.defense
        if net_damage > 0:
            self.health -= net_damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0
