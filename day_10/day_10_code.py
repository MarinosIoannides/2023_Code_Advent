"""
Day 10 Code
-----------

Part 1
-------
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

    Find the point in the loop furthest from the start point.
"""
import logging
from matplotlib.path import Path

file_path = "./day_10/"
file_name = "day_10_input.txt"

with open(f"{file_path}{file_name}") as open_file:
    lines = open_file.read().splitlines()

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s-  %(message)s')

NORTH = (0, -1)
SOUTH =  (0, 1)
EAST = (1, 0)
WEST =  (-1, 0)

orthogonal_list = [NORTH, SOUTH, EAST, WEST]

pipe_map = {
    "|": (NORTH, SOUTH),
    "-": (EAST, WEST),
    "L": (NORTH, EAST),
    "J": (NORTH, WEST),
    "7": (SOUTH, WEST),
    "F": (SOUTH, EAST),
}
def find_start(input_file):
    """
    Finds the start point (S) in the input file and returns the x y coordinates

    Parameters
    ----------
        input_file: list[strings]
    The input file read in as a list of strings

    Returns
    --------
        tup : tuple(int, int)
    Returns a tuplpe in the format (x, y) coordinates
    """
    for index, line in enumerate(input_file):
        if "S" in line:
            return (line.index("S"), index)
def valid_s(input_file):
    """
    There are only some directions from S that will be valid starts.
    This identifies which they are and returns them in a list.

    Parameters
    -----------
        input_file: list[strings]
    The input file read in as a list of strings

    Returns
    --------
        valid_directions: list[tuples(int, int)]
    A list of directions which join to valid pipe shapes
    """
    start = find_start(input_file)
    valid_directions = []
    for direction in orthogonal_list:
        # If it joins to our start, it must be able to travel to our start
        # I.E. travel in the opposite direction we go in from the start to get to it.
        anti_direction = tuple([coord * -1 for coord in direction])
        neighbour = tuple(sum(x) for x in zip(direction, start))
        character = lines[neighbour[1]][neighbour[0]]
        if character != ".":
            if anti_direction in pipe_map[character]:
                valid_directions.append(direction)
    return valid_directions

def make_pipe_route(input, starting_move):
    """
    Travels in a loop from the start point (S) to itself again, recording how long this takes.
    
    Parameters
    -----------
        start_point: tuple(int, int)
    A tuple of the start coordinates (x, y)

        starting_move: tuple(int, int)
    The first move to set us off in our exploration. Saves us hard coding what S is.
    TODO: Make a method which works out which two are valid directions of travel.

    Returns
    --------
        pipe_list: list[tuple(int, int)]
    A list of all the coordinates the pipe follows
    """
    move = starting_move
    position = find_start(input)
    pipe_route = []
    while True:
        new_position = tuple(sum(x) for x in zip(move, position))
        character = lines[new_position[1]][new_position[0]]
        if character == ".":
            return "Not a loop"
        elif character == "S":
            pipe_route.append(position)
            return pipe_route
        else:
            pipe_route.append(position),
            moves= pipe_map[character]
            for attempt in moves:
                test_x = new_position[0] + attempt[0]
                test_y = new_position[1] + attempt[1]
                if tuple([test_x, test_y]) != position:
                    move = attempt
                    break    
            position = new_position

valid_list = valid_s(lines)
direction = valid_list[0]

pipe_map = make_pipe_route(lines, direction)

print(f"Part 1: {(len(pipe_map)/2):.0f}")

x_list, y_list = zip(*pipe_map)

max_x = max(x_list)
min_x = min(x_list)

max_y = max(y_list)
min_y = min(y_list)

internal = 0
p = Path(pipe_map)
for y in range(min_y, max_y):
    for x in range(min_x, max_x):
        if tuple([x, y]) in pipe_map:
            continue
        if p.contains_point((x, y)):
            internal += 1

print(f"Part 2: {internal}")