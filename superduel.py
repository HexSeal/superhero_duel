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

class Weapon(Ability):
    def attack(self):
        half_dmg = self.max_damage // 2
        return random.randint(half_dmg, self.max_damage)

class Team:
    def __init__(self, name):
        self.name = []
        self.heroes = []

    def add_hero(self, hero): 
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                break
            else:
                return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        ''' battle each team against each other. '''
        while len(self.heroes) > 0 and len(other_team.heroes) > 0:
            Hero.fight(random.choice(self.heroes), random.choice(other_team.heroes))

    def revive_heroes(self, starting_health=100):
        ''' Resets a hero back to starting health'''
        for hero in self.heroes:
            hero.current_health = starting_health

    def stats(self):
        for hero in self.heroes:
            print(f'{hero.name} K/D ratio: ', (hero.kills)/(hero.deaths))

            print('Survivors: ')
            if hero.is_alive():
                print(hero.name, self.name)
                

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armor = []
        self.starting_health = starting_health
        self.current_health = 100
        self.name = name
        self.kills = 0
        self.deaths = 0

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
        '''I got damage_amt = 0 from Ben Lafferty. It's supposed to fix the weird pytest errors but it doesn't really'''
        total_blocked = 0 
        for armor in self.armor:
            add_to_block = int(armor.block())
            total_blocked += add_to_block
        return total_blocked + damage_amt

    def take_damage(self, damage):
        current_hp = self.current_health
        damage_received = self.defend(damage)
        self.current_health = current_hp - damage_received

    def is_alive(self):
        return self.current_health > 0

    def add_kills(self, kill_count):
        self.kills += kill_count

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
 

    def fight(self, opponent):
        while True:
            if self.is_alive():
                self_damage = self.attack()
                opponent.take_damage(self_damage)
            else:
                print(
                    f'{opponent.name} knocked out {self.name}!')   
                self.add_deaths(1)
                opponent.add_kills(1)
                break

            if opponent.is_alive():
                enemy_damage = opponent.attack()
                self.take_damage(enemy_damage)
            else:
                print(f'{self.name} knocked out {opponent.name}!')
                self.add_kills(1)

                break

class Arena:
    def __init__(self):
        print('\nWelcome to the Arena.\n')
        t1_name = input('What do you want the first team to be called? ')
        self.team_one = Team(t1_name)
        t2_name = input('What do you want the second team to be called? ')
        self.team_two = Team(t2_name)

    def create_ability(self):
        ability_name = input("Ability name: ")
        max_damage = input("Max damage: ")
        return Ability(ability_name, max_damage)

    def create_weapon(self):
        weapon_name = input("Weapon name: ")
        max_damage = input("Max weapon damage: ")
        return Weapon(weapon_name, max_damage)

    def create_armor(self):
        armor_name = input("Armor name: ")
        armor_block = input("Max armor block: ")
        return Armor(armor_name, armor_block)

    def create_hero(self):
        hero_name = input('Choose a name for your hero: ')
        health = input('How about some hp? Default is 100: ')
        hero = Hero(hero_name, health)

        add_abilities = input('\nDoes your hero have any abilities? y/n ')
        if 'y' in add_abilities:
            while True:
                ability = self.create_ability()
                hero.add_ability(ability)

                more_abilities = input('Want to add another ability? y/n ')
                if 'y' not in more_abilities:
                    break
    
        add_weapons = input('\nDoes your hero have any weapons? y/n ')
        if 'y' in add_weapons:
            while True:
                ability = self.create_weapon()
                hero.add_ability(ability)

                more_weapons = input('Want to add another weapon? y/n ')
                if 'y' not in more_weapons:
                    break

        add_armor = input('\nDoes your hero have any armor? y/n ')
        if 'y' in add_armor:
            while True:
                ability = self.create_armor()
                hero.add_ability(Armor)

                more_armor = input('Want to add more armor? y/n ')
                if 'y' not in more_armor:
                    break
        return hero
                
    def build_team_one(self):
        t1_num = input('How many hero(es) do you want on team 1? ')
        if t1_num.isalnum():
            for _ in t1_num:
                hero = self.create_hero()
                self.team_one.add_hero(hero)

    def build_team_two(self):
        t2_num = input('How many hero(es) do you want on team 2? ')
        if t2_num.isalnum():
            for _ in t2_num:
                hero = self.create_hero()
                self.team_two.add_hero(hero)

    def team_battle(self):
        ''' Puts team one against team two '''
        Team.attack(self.team_one, self.team_two)

    def show_stats(self):
        self.team_one.stats()
        self.team_two.stats()
        
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print('Team One is Victorious!')
                break
            else:
                print('Team Two is Victorious!')
                break

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
    
