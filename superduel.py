import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        damage_done = random.randint(0, self.max_damage)
        return damage_done

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        damage_blocked = random.randint(0, self.max_block)
        return damage_blocked

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armor = []
        self.starting_health = starting_health
        self.current_health = 100
        self.name = name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armor.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            add_to_stack = Ability.attack(ability)
            total_damage += add_to_stack
        return total_damage
    
    def defend(self, damage_amt = 0):
        total_blocked = 0 
        for armor in self.armor:
            add_to_block = int(armor.block())
            total_blocked += add_to_block
        return abs(damage_amt - total_blocked)

    def take_damage(self, damage):
        current_hp = self.current_health
        damage_received = self.defend(damage)
        self.current_health = current_hp - damage_received

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        while True:
            if self.is_alive():
                self_damage = self.attack()
                opponent.take_damage(self_damage)
            else:
                print(
                    f'{opponent.name} knocked out {self.name}!')
                break

            if opponent.is_alive():
                enemy_damage = opponent.attack()
                self.take_damage(enemy_damage)
            else:
                print(f'{self.name} knocked out {opponent.name}!')
                break

if __name__ == "__main__":
    another_ability = Ability("Kamehameha", 120)
    hero = Hero("Goku")
    hero.take_damage(50)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
