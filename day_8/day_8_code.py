"""
Day 8 Code
-----------

Part 1
-------
    Each line has a start point and two desitinations
    L = Destination 1, R = Desitination 2
    Must follow the LR instructions in line 1
    How many steps does it take to get from AAA to ZZZ?
"""
import re
import numpy as np
file_path = "./day_8/"
file_name = "day_8_input.txt"

with open(f"{file_path}{file_name}") as open_file:
    lines = open_file.readlines()

orders = list(lines[0])[:-1]
routes = lines[2:]

patern = re.compile(r"\w+")

routes_dictionary = {patern.findall(route)[0]: (patern.findall(route)[1], patern.findall(route)[2]) for route in routes}

def solve_steps(start, end):
    steps = 0
    current = start
    while not current.endswith(end):
        order = orders[steps % len(orders)]
        current = routes_dictionary[current][0 if order == "L" else 1]
        steps += 1
    return steps
"""
Part 2
------
    Number of nodes ending in A == Number of nodes ending in Z
    Simultaneously start on every node that ends with A.
    How many steps does it take before you're only on nodes that end with Z?
"""

# np.lcm has overflow error becuase the number is too large so we have to turn it to 64bit int
print(np.lcm.reduce([np.int64(solve_steps(start, "Z")) for start in routes_dictionary.keys() if start.endswith("A")]))


