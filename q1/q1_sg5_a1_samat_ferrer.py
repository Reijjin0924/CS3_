"""
#05, Reginald Andrei D. Ferrer
9-SAMAT
"""

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

hero = Hero("Arthur", 100)
hero2 = Hero("Morgana", 100)

hero.take_damage(10)

print(f"{hero.name} HP: {hero.hp}")
print(f"{hero2.name} HP: {hero2.hp}")
