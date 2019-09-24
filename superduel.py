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

    def attack(self):
        total_damage = 0
        add_to_stack = 0
        for ability in self.abilities:
            add_to_stack = Ability.attack(ability)
            total_damage += add_to_stack
        return total_damage
    
    def defend(self, incoming_damage):
        self.incoming_damage = incoming_damage

    def take_damage(self, damage):
        self.damage = damage

    def is_alive(self):
        pass

    def fight(self, opponent):
        self.opponent = opponent
        print(self.name + " fights " + opponent)
        

if __name__ == "__main__":
    ability = Ability("Test Beam", 50)
    another_ability = Ability("Kamehameha", 120)
    hero = Hero("Goku", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())

