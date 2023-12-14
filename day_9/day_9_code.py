"""
Day 9 Code
----------

Part 1
-------
    Extrapolate the next value in the sequence
    What is the sum of the extrapolated values?
"""

file_path = "./day_9/"
file_name = "day_9_input.txt"

with open(f"{file_path}{file_name}") as open_file:
    lines = open_file.read().splitlines()
    lines = [list(map(int, line.split(" ")))for line in lines]

def get_differences(sequence):
    difference_list = []
    for index, digit in enumerate(sequence):
        if index < len(sequence)-1:
            difference_list.append(sequence[index +1] - digit)
    return difference_list

def make_difference_dictionary(sequence):
    difference_dict = {0:sequence}
    for x in range(999):
        difference_dict[x + 1] = get_differences(difference_dict[x])
        if all(v == 0 for v in get_differences(difference_dict[x])):
            return difference_dict

def predict_next(sequence):
    difference = make_difference_dictionary(sequence)
    lasts = [value[-1] for value in list(difference.values())][::-1]
    return(sum(lasts))

# We can also do this by working out f(n)
# np has Polynomial.fit which will just give us the f(n)
# From https://www.reddit.com/r/adventofcode/comments/18e5ytd/2023_day_9_solutions/

from numpy.polynomial.polynomial import Polynomial
import numpy as np

answer = [0, 0]
for line in lines:
    y = [int(x) for x in line]
    poly = Polynomial.fit(np.arange(len(y)), y, deg=len(y)-1)
    answer[0] += round(poly(len(y)))
    answer[1] += round(poly(-1))
print("Part 1: {}\nPart 2: {}".format(*answer))

"""
Part 2
-------
    Extrapolate backwards and sum

"""

def predict_first(sequence):
    difference = make_difference_dictionary(sequence)
    firsts = [value[0] for value in list(difference.values())][::-1]
    working_num = firsts[0]
    for first in firsts[1:]:
        working_num = first - working_num
    return working_num