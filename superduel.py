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
        pass

    def fight(self, opponent):
        self.opponent = opponent
        print(self.name + " fights " + opponent)
        

if __name__ == "__main__":
    another_ability = Ability("Kamehameha", 120)
    hero = Hero("Goku", 200)
    shield = Armor("Shield", 50)
    hero.add_armor(shield)
    hero.take_damage(60)
    print(hero.current_health)

