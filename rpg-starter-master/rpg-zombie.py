"""
In this simple RPG game, the hero fights a zombie that cannot die. He has the options to:

1. fight zombie
2. do nothing - in which case the zombie will attack him anyway
3. flee

"""


class Character(object):

    def __init__(self, health, power):

        self.health = health
        self.power = power

    def attack(self, enemy):

        enemy.health -= self.power

    def alive(self):

        if self.health > 0:
            return True

    def print_status(self):

        if self.__class__.__name__ == 'Hero':
            print(f"You have {self.health} health and {self.power} power.")
        elif self.__class__.__name__ == 'Zombie':
            print(
                f"The Zombie has {self.health} health and {self.power} power.")


class Hero(Character):
    pass

# Step 8 Bonus Challenge:  Create a zombie character that cannot die and have it fight the hero instead of the goblin
# My take on the "never die" requirement is that although the zombie can lose health from the hero, it simply just regenerates it right back so it can never die.


class Zombie(Character):
    def never_die(self, enemy):
        self.health += enemy.power


# Global Variables. Makes it easy to tinker with character values if need be.
hero_health = 10
hero_power = 5
zombie_health = 6
zombie_power = 3

our_hero = Hero(hero_health, hero_power)
zombie = Zombie(zombie_health, zombie_power)


def main():
    while zombie.alive() and our_hero.alive():
        our_hero.print_status()
        zombie.print_status()

        print()
        print("What do you want to do?")
        print("1. fight zombie")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()

        if user_input == "1":
            our_hero.attack(zombie)
            print("You do %d damage to the zombie." % our_hero.power)
            zombie.never_die(our_hero)
            print(f"The zombie immediately regenerates health.")

        elif user_input == "2":
            pass

        elif user_input == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid input %r" % user_input)

        if zombie.alive():

            zombie.attack(our_hero)
            print("The zombie does %d damage to you." % zombie.power)
            if not our_hero.alive():
                print("You are dead.")


main()
