import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        damage_done = random.randint(0, int(self.max_damage))
        return damage_done

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    
    def block(self):
        damage_blocked = random.randint(0, int(self.max_block))
        return damage_blocked

class Weapon(Ability):
    def attack(self):
        half_dmg = self.max_damage // 2
        return random.randint(half_dmg, int(self.max_damage))

class Relic(Armor):
    def block(self, opponent):
        if opponent.activate_relic == True:
            damage_blocked = random.randint(0, int(self.max_block))
        else:
            damage_blocked = 0

        return damage_blocked

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armor = []
        self.relics = []
        self.starting_health = starting_health
        self.current_health = 100
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.activate_relic = False

    def add_ability(self, ability):
        self.abilities.append(ability)
        self.activate_relic = True

    def add_armor(self, armor):
        self.armor.append(armor)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            add_to_stack = Ability.attack(ability)
            total_damage += add_to_stack
        return total_damage
    
    def defend(self):
        '''I got damage_amt = 0 from Ben Lafferty. It's supposed to fix the weird pytest errors but it doesn't really'''
        total_blocked = 0 
        total_relic = 0
        for armor in self.armor:
            add_to_block = armor.block()
            total_blocked += add_to_block

        if self.activate_relic == True:
            for relic in self.relics:
                add_to_relic = relic.block()
                total_relic += add_to_relic
        return total_blocked + total_relic

    def take_damage(self, damage):
        current_hp = self.current_health
        damage_received = self.defend()
        self.current_health = current_hp - damage_received

    def is_alive(self):
        return self.current_health > 0

    def add_kills(self, kill_count):
        self.kills += kill_count
        return self.kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths
        return self.deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_relic(self, relic):
        self.relics.append(relic)

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            self_damage = self.attack()
            enemy_damage = opponent.attack()

        if opponent.abilities != 0:
            opponent.activate_relic = True

            self.take_damage(enemy_damage)
            opponent.take_damage(self_damage)

        if self.is_alive() == False:
            print(f'{opponent.name} knocked out {self.name}!')   
            self.add_deaths(1)
            opponent.add_kills(1)

        else: 
            print(f'{self.name} knocked out {opponent.name}!')
            self.add_kills(1)
            opponent.add_deaths(1)

class Team:
    def __init__(self, name):
        self.name = name
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
        ''' Got from this comment to the next from github.com/soundreaper/superheroteamdueler. This is so that the code can recognize that the fight is over because heroes can't be
        removed from heroes but we need to know which are done '''
        ''' github.com/soundreaper/superheroteamdueler --start-- '''
        alive_hero_list_1 = []
        alive_hero_list_2 = []

        for hero_1 in self.heroes:
                if hero_1.is_alive() == True:
                    alive_hero_list_1.append(self.heroes.index(hero_1))
        
        for hero_2 in other_team.heroes:
                if hero_2.is_alive() == True:
                    alive_hero_list_2.append(other_team.heroes.index(hero_2))

        ''' battle each team against each other. '''
        while len(alive_hero_list_1) > 0 and len(alive_hero_list_2) > 0:
            random_hero_1 = self.heroes[random.choice(alive_hero_list_1)]
            random_hero_2 = other_team.heroes[random.choice(alive_hero_list_2)]

            random_hero_1.fight(random_hero_2)

            for hero_alivecheck_1 in self.heroes:
                if hero_alivecheck_1.is_alive() == False:
                    alive_hero_list_1.pop(self.heroes.index(hero_alivecheck_1))
            
            for hero_alivecheck_2 in other_team.heroes:
                if hero_alivecheck_2.is_alive() == False:
                    alive_hero_list_2.pop(other_team.heroes.index(hero_alivecheck_2))

        if len(alive_hero_list_1) > 0:
            return self.name
        elif len(alive_hero_list_2) > 0:
            return other_team.name
        elif len(alive_hero_list_1) == len(alive_hero_list_2):
            return "Draw!"
        ''' --end-- '''

    def revive_heroes(self, starting_health=100):
        ''' Resets a hero back to starting health'''
        for hero in self.heroes:
            hero.current_health = starting_health

    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                print('{}:\nK/D ratio: {}'.format((hero.name), (hero.kills)), 'with {} kills and 0 deaths'.format(hero.kills))
            else:
                print('{}:\nK/D ratio: {}'.format((hero.name), (hero.kills) // (hero.deaths)), 'with {} kills and {} deaths'.format(hero.kills, hero.deaths))
                   
class Arena:
    def __init__(self):
        self.winning_team = None
        print('\nWelcome to the Arena.\n')
        t1_name = input('What do you want the first team to be called? ')
        self.team_one = Team(t1_name)
        t2_name = input('What do you want the second team to be called? ')
        self.team_two = Team(t2_name)

    def create_ability(self):
        self.activate_relic = True
        ability_name = input("Ability name: ")
        max_damage = input("Max damage: ")
        if max_damage > 100:
            max_damage = input("That's hardly a fair number. Please keep it below 100: ")

        return Ability(ability_name, max_damage)

    def create_weapon(self):
        weapon_name = input("Weapon name: ")
        max_damage = input("Max weapon damage: ")
        if max_damage > 100:
            max_damage = input("That's hardly a fair number. Please keep it below 100: ")
        
        return Weapon(weapon_name, max_damage)

    def create_armor(self):
        armor_name = input("Armor name: ")
        armor_block = input("Max armor block: ")
        if armor_block > 100:
            armor_block = input("That's hardly a fair number. Please keep it below 100: ")

        return Armor(armor_name, armor_block)

    def create_relic(self):
        relic_name = input("Relic name: ")
        relic_block = input("Max relic block: ")
        if relic_block > 100:
            relic_block = input("That's hardly a fair number. Please keep it below 100: ")
        
        return Relic(relic_name, relic_block)

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
                weapon = self.create_weapon()
                hero.add_weapon(weapon)

                more_weapons = input('Want to add another weapon? y/n ')
                if 'y' not in more_weapons:
                    break

        add_armor = input('\nDoes your hero have any armor? y/n ')
        if 'y' in add_armor:
            while True:
                armor = self.create_armor()
                hero.add_armor(armor)

                more_armor = input('Want to add more armor? y/n \n')
                if 'y' not in more_armor:
                    break

        add_relic = input('\nDoes your hero have any relics(Only blocks against abilities)? y/n ')
        if 'y' in add_relic:
            while True:
                relic = self.create_relic()
                hero.add_relic(relic)

                more_relics = input('Want to add more relics? y/n \n')
                if 'y' not in more_relics:
                    break
        return hero
                
    def build_team_one(self):
        t1_num = input('How many hero(es) do you want on team 1? ')
        if t1_num.isalnum():
            for _ in range(0, int(t1_num)):
                hero = self.create_hero()
                self.team_one.add_hero(hero)
        else:
            t1_num = input('Incorrect input. Please enter a number: ')

    def build_team_two(self):
        t2_num = input('How many hero(es) do you want on team 2? ')
        if t2_num.isalnum():
            for _ in range(0, int(t2_num)):
                hero = self.create_hero()
                self.team_two.add_hero(hero)
        else:
            t2_num = input('Incorrect input. Please enter a number: ')
            
    def team_battle(self):
        ''' Puts team one against team two '''
        self.winning_team = self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\nStats: ")
        self.team_one.stats()
        self.team_two.stats()
        
        print("\nThe winning team is: \n" + self.winning_team)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ").lower()

        #Check for Player Input
        if play_again == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
