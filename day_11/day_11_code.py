"""
Day 11 Code
------------

Part 1
-------
    Galaxy map provided
    Rows / columns without galaxies in them are doubled
    What is the sum of distances between all pairs of galaxies?
"""
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s-  %(message)s')

file_path = "./day_11/"
file_name = "day_11_input.txt"

def find_spaces(input_path):
    with open(input_path) as open_file:
        original = [list(string) for string in open_file.read().splitlines()]
    
    blank_rows = []
    for line_index, line in enumerate(original):
        if "#" not in line:
            blank_rows.append(line_index)

    blank_columns = []
    for column in range(len(original[0])):
        column_values = []
        for row in original:
            column_values.append(row[column])
        if "#" not in column_values:
            blank_columns.append(column)

    return (blank_rows, blank_columns)


def double_spaces(input_path):
    blank_rows, blank_columns = find_spaces(input_path)
    with open(input_path) as open_file:
        original = [list(string) for string in open_file.read().splitlines()]
    new = []

    for row_num, row in enumerate(original):
        new.append(row)
        if row_num in blank_rows:
            new.append(row.copy())

    for row in range(len(new)):
        adjustment = 0
        for column in blank_columns:
            new[row].insert(column + adjustment, ".")
            adjustment += 1
    
    return new

# For easy visualisation
lines = double_spaces(file_path+file_name)
with open('./day_11/corrected_galaxy.txt', 'w') as f:
    for line in lines:
        f.write(f"{''.join(line)}\n")

def get_coordinates(galaxy_list):
    coords_list = []
    for line_index, line in enumerate(galaxy_list):
        x_axis = [index for index, character in enumerate(line) if character == "#"]
        coords_list.extend((x, line_index) for x in x_axis)

    return coords_list

def sum_pair_distance(input_path):
    coordinates = get_coordinates(double_spaces(input_path))
    final_sum = 0
    for co_index, co in enumerate(coordinates):
        remaining_co = coordinates[co_index:]
        for comparator in remaining_co:
            final_sum += abs(co[0] - comparator[0]) + abs(co[1] - comparator[1])
    return final_sum

logging.debug(f"Part 1: {sum_pair_distance(f'{file_path}{file_name}')}")
"""
Part 2
-------
    Rows / columns without galaxies in them are 1,000,000 times further apart than expected
"""

# Not going to create a file with millions of lines

def sum_distance_with_gap(input_path, multiplier):
    with open(input_path) as open_file:
        galaxy_map = [list(string) for string in open_file.read().splitlines()]
    coordinates = get_coordinates(galaxy_map)
    blank_rows, blank_columns = find_spaces(input_path)
    final_sum = 0
    for co_index, co in enumerate(coordinates):
        remaining_co = coordinates[co_index:]
        for comparator in remaining_co:
            start_x, start_y = co
            end_x, end_y = comparator
            max_x = max(start_x, end_x)
            min_x = min(start_x, end_x)
            max_y = max(start_y, end_y)
            min_y = min(start_y, end_y)
            final_sum += max_x + max_y - min_x - min_y

            # Why -1?
            # Because the row itself is included in the multiplier
            for col in blank_columns:
                if col in range(min_x, max_x):
                    final_sum += multiplier -1
            for row in blank_rows:
                if row in range(min_y, max_y):
                    final_sum += multiplier -1
    return final_sum
logging.debug(f"Part 2: {sum_distance_with_gap(f'{file_path}{file_name}', 1000000)}")