
class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        print('attack')

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

    def add_ability(ability):
        print('ability')

    def attack(self):
        print('attack')
    
    def defend(self, incoming_damage):
        self.incoming_damage = incoming_damage

    def take_damage(self, damage):
        self.damage = damage

    def is_alive():

    def fight(self, opponent):
        
