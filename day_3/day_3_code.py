"""
Day 3 Code
-----------

Part 1
-------
    If a number is adjacent to a symbol, even diagonally it is considered valid.
    What is the sum of valid numbers?
"""
import numpy as np
import re

file_path = "./day_3/"
file_name = "day_3_input.txt"

file_string = file_path + file_name

with open(file_string) as open_file:
    array = [s + '.' for s in open_file.read().strip().split('\n')]

from collections import defaultdict
from math import prod
import re

parts = defaultdict(list)
board = list(open(file_string))
def find_chars(board):
    chars = {(r, c) for r in range(140)
                    for c in range(140)
                    if board[r][c] not in '01234566789.'}
    return chars

def find_valids(board):
    for r, row in enumerate(board):
        for m in re.finditer(r'\d+', row):
            nexts = {(r+s, c+d) for s in (-1, 0, 1) 
                                for d in (-1, 0, 1)
                                for c in range(*m.span())}
            for c in nexts & find_chars(board):
                parts[c].append(int(m[0]))
    return parts

print(sum(sum(p)  for p in find_valids(board).values()),
      sum(prod(p) for p in find_valids(board).values() if len(p)==2))