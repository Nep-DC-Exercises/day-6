"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
'''
Step 1

Make a Hero class to store the health and power of the hero, and make a Goblin class to store the health and power of the goblin. Use a hero object in place of the variables hero_health and hero_power and use a goblin object in place of the variables goblin_health and goblin_power all through out the app.
'''


class Hero:

    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power


class Goblin:

    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power


hero_health = 10
hero_power = 5
goblin_health = 6
goblin_power = 2

our_hero = Hero(hero_health, hero_power)
the_goblin = Goblin(goblin_health, goblin_power)


def main():

    while the_goblin.health > 0 and our_hero.health > 0:
        print("You have %d health and %d power." %
              (our_hero.health, our_hero.power))
        print("The goblin has %d health and %d power." %
              (the_goblin.health, the_goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Step 2: Replace the hero attack code with an attack method within hero class
            # Hero attacks goblin
            our_hero.attack(the_goblin)  # new attack code
            # the_goblin.health -= our_hero.power  # old attack code
            print("You do %d damage to the goblin." % our_hero.power)
            if the_goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if the_goblin.health > 0:
            # Step 3: Replace the goblin attack code with an attack method within goblin class
            # Goblin attacks hero
            # our_hero.health -= the_goblin.power # old goblin attack
            the_goblin.attack(our_hero)  # new goblin attack method
            print("The goblin does %d damage to you." % the_goblin.power)
            if our_hero.health <= 0:
                print("You are dead.")


main()
