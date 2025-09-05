from enemy import Enemy

class Baby_Elf(Enemy):
    def cry(self):
        print("WAHH! WAHH!")

    def take_damage(self, damage):
        print("YOU HIT A BABY! YOU MONSTER!")
        return super().take_damage(damage)