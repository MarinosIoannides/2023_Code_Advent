"""
Day 6 Code
----------

Part 1
-------
    Input has distance traveled in given time
    We need to go farther in every race than the current record to be sure to win
    Boats are powered by pressing a button, charging the boat.
    The time spent pressing is included in the race time.
    For each milisecond spent holding the button down, the speed increases by one millimiter per second
    
    You can therefore beat many records though calculation in many ways
    Work out how many ways you could beat each race
    What is the product of these numbers?
"""
import re
import numpy as np

file_path = "./day_6/"
file_name = "day_6_input.txt"

file_string = file_path + file_name

with open(file_string) as open_file:
    lines = [line for line in open_file.read().splitlines()]

times = lines[0]
distances = lines[1]

digit_patern = re.compile(r"\d+")
time_distance = list(zip(digit_patern.findall(times), digit_patern.findall(distances)))

def calc_times(time_distance_tup):
    time, distance = time_distance_tup
    distance_list = [int(pressed_time) * (int(time) - int(pressed_time)) for pressed_time in range(int(time))]
    distance_list = [dist for dist in distance_list if dist > int(distance)]
    return len(distance_list)

p = 1
for pair in time_distance:
    p = p * calc_times(pair)
"""
Part 2
------
    The nummbers from before are actually just one massive number
    There must be a faster way of doing this but this works for now
"""
time = ''.join(digit_patern.findall(times))
distance = "".join(digit_patern.findall(distances))

print(calc_times((time, distance)))