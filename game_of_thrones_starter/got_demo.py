from pprint import pprint
from characters import characters
from houses import houses

# This exercise was to simulate calling an API and accessing the data to answer questions about said data


character_name_a_count = 0

for character in characters:
    if character['name'].startswith('A'):
        character_name_a_count += 1

print(character_name_a_count)


character_name_z_count = 0

for character in characters:
    if character['name'].startswith('Z'):
        character_name_z_count += 1

print(character_name_z_count)


# How many characters are dead

dead_characters = 0

for character in characters:
    if len(character["died"]) > 0:
        dead_characters += 1

print(dead_characters)


# Who has the most titles?
list_of_title_length = []
dictionary = {}

for character in characters:
    title_length = len(character["titles"])
    list_of_title_length.append(title_length)
    dictionary.update({title_length: character["name"]})


look_up = max(list_of_title_length)
print(dictionary[look_up])

# How many are Valyrian?

valyrian_count = 0

for character in characters:
    if character['culture'] == 'Valyrian':
        valyrian_count += 1

print(valyrian_count)


# What actor plays "Hot Pie" (and don't use IMDB)?
for character in characters:

    if character['name'] == 'Hot Pie':
        print(character['playedBy'])

# How many characters are "not" in the TV Show?

count_not_in_show = 0

for character in characters:

    if len(character['tvSeries']) == 1:
        count_not_in_show += 1

print(count_not_in_show)

# Produce a list of characters with the last name "Targaryen"

targar = []

for character in characters:

    if 'Targaryen' in character['name']:
        targar.append(character['name'])

print(targar)

# Create a histogram of the houses (it's the allegiances key)

houses_dict = {}  # {House Link:  Count of Characters}
histogram_dict = {}  # This will where we store our answer

for character in characters:  # Loop through the whole array

    # Loop through all the character allegiance values of each character since there are some that are more than 0
    for i in character['allegiances']:
        # If a House Link key is inside the dictionary, increment its value by 1
        if i in houses_dict:
            houses_dict[i] += 1
        # If not, then set it's value to 1 since it doesn't show up in the list yet
        else:
            houses_dict[i] = 1
# So right now, houses_dict contains each unique allegiance value as the key. The value is how often it appeared in characters
print(houses_dict)

# Reminder to myself of the format of the houses and houses_dict dictionaries. It got confusing to keep these two dictionaries straight.

# Houses {House Link: House Name}
# Houses_Dict {House Link: Frequency Count}

for i in houses_dict:  # need to loop over every value in houses_dict to do a comparison

    if i in houses:  # if the house link from houses_dict matches a key in the houses dictionary

        name = houses[i]  # set name equal to the name of the house
        # set count equal to the the frequency of how often the house is represented
        count = houses_dict[i]
        # use the name and count variables that were just defined to establish new key value pairs in histogram_dict
        histogram_dict[name] = count

# outputs a dictionary with House Name as key. The value is how many characters belong to that house.
print(histogram_dict)
