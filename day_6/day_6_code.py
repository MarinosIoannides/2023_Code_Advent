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

file_path = "./day_6/"
file_name = "day_6_test.txt"

file_string = file_path + file_name

with open(file_string) as open_file:
    lines = [line for line in open_file.read().splitlines()]

times = lines[0]
distances = lines[1]

digit_patern = re.compile(r"\d+")
time_distance = list(zip(digit_patern.findall(times), digit_patern.findall(distances)))

def calc_times(time_distance_tup):
    time, distance = time_distance_tup
    
