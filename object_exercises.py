# Python Object Exercises


class Person:

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_people_greeted = []

    # greets another person. Keeps track of how many times each Person object greets another Person
    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count += 1

        # refer to num_unique_people_greeted
        if other_person.name not in self.unique_people_greeted:
            self.unique_people_greeted.append(other_person.name)

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}")

    # Hiding implementation details from users. Implement an add_friend method. The user can do jordan.add_friend(sonny) instead of jordan.friends.append(sonny)
    def add_friend(self, other_person):
        self.friends.append(other_person.name)

    # Counting how many friends each Person object has since friends is a list attribute
    def num_friends(self):
        print(len(self.friends))

    # When printing the instantiated object, print(sonny), this method returns formatted information rather than the default Python output.
    def __str__(self):
        return f"Person: {self.name}, {self.email}, {self.phone}"

    # Bonus Challenge: Keep track of the number of unique people a person has greeted and be able to report that number
    # Created empty list/array attribute n the __init__ method called unique_people_greeted
    # Whenever the greet method is called, I'll add the name of the person we are greeting into self.unique_people_greeted, as long as that person is not in the list.
    # Then when we call num_unique_people_greeted, we just count the length of the list of unique people.
    def num_unique_people_greeted(self):
        num_uniques = len(self.unique_people_greeted)
        print(num_uniques)


# Instantiating Person objects
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@email.com', '495-586-3456')
dee_ann = Person('DeeAnn', 'email', 'number')

# testing out greet method

sonny.greet(jordan)
jordan.greet(sonny)

# accessing attributes
print(sonny.email, sonny.phone)
print(jordan.email, jordan.phone)

# calling the print contact info method
sonny.print_contact_info()

# The cumbersome way to add a name to a person object
sonny.friends.append(jordan.name)
jordan.friends.append(sonny.name)

# Calling the add_friend method

jordan.add_friend(sonny)
print(jordan.friends)
jordan.num_friends()

# Testing out how many times an object uses the greet method
jordan.greet(sonny)
print(jordan.greeting_count)
jordan.greet(sonny)
print(jordan.greeting_count)

# Testing out the str method
print(sonny)
print(jordan)

# Testing out the unique_people attribute and making sure it's working
sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(dee_ann)
sonny.num_unique_people_greeted()

# practicing creating a vehicle class


class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)


car = Vehicle('Honda', 'CRV', 2016)

car.print_info()
