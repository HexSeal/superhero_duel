import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        damage_done = random.randint(0, self.max_damage)
        return damage_done

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        print('block')

class Hero:
    def __init__(self, name, starting_health):
        self.name = name
        self.starting_health = starting_health

    def add_ability(self, ability):
        print('ability')

    def attack(self):
        print('attack')
    
    def defend(self, incoming_damage):
        self.incoming_damage = incoming_damage

    def take_damage(self, damage):
        self.damage = damage

    def is_alive(self):
        pass

    def fight(self, opponent):
        self.opponent = opponent
        print(self.name + " fights " + opponent)


        
