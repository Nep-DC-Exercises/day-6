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


class Character(object):  # Step 6:  Since Hero and Goblin have almost the exact attributes and methods, create a Character class that they inherit their attributes from

    def __init__(self, health, power):

        self.health = health
        self.power = power

    def attack(self, enemy):

        enemy.health -= self.power

    # Step 7: Move alive methods on Hero and Goblin into Character. This was done in Step 6 already. Whoops.
    def alive(self):

        if self.health > 0:
            return True

    def print_status(self):
        print(f"You have {self.health} health and {self.power} power.")


class Hero(Character):
    pass


class Goblin(Character):

    # For the goblin's health status, we want to say "The Goblin has" rather than "You Have"
    def print_status(self):
        print(f"The Goblin has {self.health} health and {self.power} power.")


# Global Variables. Makes it easy to tinker with character values if need be.
hero_health = 10
hero_power = 5
goblin_health = 6
goblin_power = 2

our_hero = Hero(hero_health, hero_power)
the_goblin = Goblin(goblin_health, goblin_power)


def main():
    # Step 4
    # while the_goblin.health > 0 and our_hero.health > 0:  Old while loop condition
    # New alive methods to check and see if they're both... alive
    while the_goblin.alive() and our_hero.alive():
        # Step 5: Replace code for printing the health status of the hero and move it into a method called print_status and do the same for the Goblin
            # print("You have %d health and %d power." %
            #     (our_hero.health, our_hero.power))
            # print("The goblin has %d health and %d power." %
            #     (the_goblin.health, the_goblin.power))
        our_hero.print_status()
        the_goblin.print_status()

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
            if not the_goblin.alive():  # replaced goblin health check. if the goblin is not alive.
                print("The goblin is dead.")

        elif user_input == "2":
            pass

        elif user_input == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid input %r" % user_input)

        if the_goblin.alive():
            # Step 3: Replace the goblin attack code with an attack method within goblin class
            # Goblin attacks hero
            # our_hero.health -= the_goblin.power # old goblin attack
            the_goblin.attack(our_hero)  # new goblin attack method
            print("The goblin does %d damage to you." % the_goblin.power)
            if not our_hero.alive():  # replaced health check. if our hero is not alive.
                print("You are dead.")


main()
