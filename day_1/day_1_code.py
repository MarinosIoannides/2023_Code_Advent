"""
Day 1 code
-----------

Part 1
--------
    In each string, there will be at least 1 number
    Find the first and last number in the string
    Combine them to form a two digit number
    Sum these two digit numbers and return them
"""
import re

file_path = "./day_1/"
file_name = "day_1_input.txt"

file_string = file_path + file_name

with open(file_string) as open_file:
    lines = [line for line in open_file]


def find_numbers(input_string):
    for character in input_string:
        if character.isdigit():
            first_digit = character
            break
    for character in input_string[::-1]:
        if character.isdigit():
            second_digit = character
            break
    return int(first_digit + second_digit)


# Neater solution
def find_numbers_neat(input_string):
    numbers_in_string = [match for match in re.findall(r"\d", input_string)]
    return int(numbers_in_string[0] + numbers_in_string[-1])


def sum_numbers(input_list):
    return sum(find_numbers_neat(single_line) for single_line in input_list)


"""
Part 2
--------
    In some strings, there are words like "one"
    They also count as digits
"""
words_num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def words_to_numb(input_string):
    for key in words_num.keys():
        input_string = input_string.replace(key, words_num[key])
    return input_string


def sum_words_numbers(input_list):
    return sum(find_numbers_neat(words_to_numb(line)) for line in input_list)
