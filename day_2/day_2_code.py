"""
Day 2 Code
-----------

Part 1
-------
    A bag contains cubes that are either red, green or blue.
    Each "set", a random handful of cubes are taken out, shown and replaced
    Many sets comprise a "game"
    Which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
    What is the sum of the IDs of those games?
"""

file_path = "./day_2/"
file_name = "day_2_input.txt"

file_string = file_path + file_name

with open(file_string) as open_file:
    lines = [line for line in open_file]

MAX_POSSIBLE = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def blocks_possible(string):
    sets = string.split(":")[1]
    rounds = sets.split(";")
    max_colours = {color: 0 for color in MAX_POSSIBLE}

    for round in rounds:
        cubes = round.split(",")
        for cube in cubes:
            space, num, colour = cube.replace("\n" ,"").split(" ")
            num  = int(num)
            max_colours[colour] = max(num, max_colours[colour])

    for key in max_colours:
        if max_colours[key] > MAX_POSSIBLE[key]:
            return False
    return True

def sum_possible_id(list):
    id_total = 0
    for index, value in enumerate(list):
        if blocks_possible(value):
            id_total += index + 1
    return id_total

"""
Part 2
-------
    What is the fewest number of cubes of each color that could have been in the bag to make the game possible?
    The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
    For each game, find the minimum set of cubes that must have been present. 
    What is the sum of the power of these sets?
"""

def blocks_power(string):
    sets = string.split(":")[1]
    rounds = sets.split(";")
    max_colours = {color: 0 for color in MAX_POSSIBLE}

    for round in rounds:
        cubes = round.split(",")
        for cube in cubes:
            space, num, colour = cube.replace("\n" ,"").split(" ")
            num  = int(num)
            max_colours[colour] = max(num, max_colours[colour])
            
    power = 1
    for key in max_colours:
        power = power * max_colours[key]
    return power


def sum_powers(list):
    return sum(blocks_power(string) for string in list)
