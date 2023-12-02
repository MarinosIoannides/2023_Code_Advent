import pytest
from day_1_code import find_numbers, sum_numbers, find_numbers_neat, words_to_numb, sum_words_numbers

""" Day 1 Part 1 """
@pytest.mark.parametrize(
    "string, number",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
    ]
)
def test_number_detection(string, number):
    assert number == find_numbers(string) and number == find_numbers_neat(string)


@pytest.mark.parametrize(
    "string_list, sum",
    [
        (["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], 142)
    ]
)
def test_sum_numbers(string_list, sum):
    assert sum == sum_numbers(string_list)


""" Day 1 Part 2 """
@pytest.mark.parametrize(
    "string, number",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        ("slconeightfoureight557m38", 18)
    ]
)
def test_number_creation(string, number):
    assert number == find_numbers(words_to_numb(string))


@pytest.mark.parametrize(
    "string_list, sum",
    [
        (["two1nine", "eightwothree", "abcone2threexyz",
          "xtwone3four", "4nineeightseven2", "zoneight234",
          "7pqrstsixteen"], 281)
    ]
)
def test_number_creation_sum(string_list, sum):
    assert sum == sum_words_numbers(string_list)
