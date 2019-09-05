from pprint import pprint
from characters import characters
from houses import houses

# Todo Need to use f statements when displaying the answer
# Todo also need to map the house api links to the house name in houses.py

# character_name_a_count = 0

# for character in characters:
#     if character['name'].startswith('A'):
#         character_name_a_count += 1
#     else:
#         pass

# print(character_name_a_count)


# character_name_z_count = 0

# for character in characters:
#     if character['name'].startswith('Z'):
#         character_name_z_count += 1
#     else:
#         pass

# print(character_name_z_count)


# # How many characters are dead

# dead_characters = 0

# for character in characters:
#     if len(character["died"]) > 0:
#         dead_characters += 1

# print(dead_characters)


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

# valyrian_count = 0

# for character in characters:
#     if character['culture'] == 'Valyrian':
#         valyrian_count += 1

# print(valyrian_count)


# # What actor plays "Hot Pie" (and don't use IMDB)?
# for character in characters:

#     if character['name'] == 'Hot Pie':
#         print(character['playedBy'])

# How many characters are "not" in the TV Show?

# count_not_in_show = 0

# for character in characters:

#     if len(character['tvSeries']) == 1:
#         count_not_in_show += 1

# print(count_not_in_show)

# Produce a list of characters with the last name "Targaryen"

# targar = []

# for character in characters:

#     if 'Targaryen' in character['name']:
#         targar.append(character['name'])

# print(targar)

# Create a histogram of the houses (it's the allegiances key)


houses_dict = {}  # {House Link:  Count of Characters}

for character in characters:  # Loop through the whole array

    # Loop through all the character allegiance values of each character since there are some that are more than 0
    for i in character['allegiances']:
        # If a House Link is inside the dictionary, increment its value by 1
        if i in houses_dict:
            houses_dict[i] += 1
        # Else, set it's value to 1 since it doesn't show up in the list yet
        else:
            houses_dict[i] = 1
# So right now, houses_dict contains each unique allegiance value as the key. The value is how often it appeared in characters
print(houses_dict)
