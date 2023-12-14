"""
Day 5 Code
-----------

Part 1
-------
    Find the lowest location number that corresponds to any of the initial seeds
    What is the lowest location number that corresponds to any of the initial seed numbers?
"""
from collections import defaultdict 
import math

file_path = "./day_5/"
file_name = "day_5_input.txt"

file_string = file_path + file_name

with open(file_string) as open_file:
    lines = [line for line in open_file.read().splitlines()]

category_dict = defaultdict(list)

for line in lines:
    if "seeds" in line:
        seeds = [int(value) for value in line.split(": ")[1].split(" ")]
    elif "map" in line:
        working_key = line.split(" ")[0]
    elif line == '':
        working_key = ''
    else:
        location, source, interval = line.split(" ")
        difference = int(location) - int(source)
        start = int(source)
        end = int(source) + int(interval)
        category_dict[working_key].append([start, end, difference])

def find_locations(list_of_seeds):
    old_input = list_of_seeds
    for key in category_dict.keys():
        new_input = []
        for seed in old_input:
            lowest_conversion = math.inf
            for choice in category_dict[key]:
                if seed in range(choice[0], choice[1]):
                    lowest_conversion = min(lowest_conversion, seed + choice[2])
            if lowest_conversion == math.inf:
                lowest_conversion = seed
            new_input.append(lowest_conversion)
        old_input = new_input
    old_input.sort()
    return old_input[0]
"""
Part 2
------
    seeds: is range of seeds
    seeds is actually pairs of values with (start, interval)
"""


def generate_true_seeds(seeds):
    for index in range(0, len(seeds), 2):
        start, interval = int(seeds[index]), int(seeds[index + 1])
        for new_seed in range(start, start + interval):
            yield new_seed

# Runs out of memory
"""true_seeds = []
for index in range(0, len(seeds), 2):
    start, interval = int(seeds[index]), int(seeds[index + 1])
    for new_seed in range(start, start+interval):
        true_seeds.append(new_seed)"""

true_seeds_generator = generate_true_seeds(seeds)
def find_locations_2():
    smallest_location = math.inf
    for seed in true_seeds_generator:
        for key in category_dict.keys():
            lowest_conversion = math.inf
            for choice in category_dict[key]:
                if seed in range(choice[0], choice[1]):
                    lowest_conversion = min(lowest_conversion, seed + choice[2])
            if lowest_conversion == math.inf:
                lowest_conversion = seed
            seed = lowest_conversion
        smallest_location = min(lowest_conversion, smallest_location)
    return smallest_location

print(find_locations_2())