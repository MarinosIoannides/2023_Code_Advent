import pytest

""" Day 11 Part 1 """
from day_11_code import double_spaces, sum_pair_distance, sum_distance_with_gap

big_galaxy_path = "./day_11/day_11_test_answer.txt"
small_galaxy_path = "./day_11/day_11_test.txt"

with open(big_galaxy_path) as open_file:
    big_galaxy = [list(string) for string in open_file.read().splitlines()]

@pytest.mark.parametrize(
    "small_galaxy, big_galaxy",
    [
        (small_galaxy_path, big_galaxy)
    ]
)
def test_spread_galaxy(small_galaxy, big_galaxy):
    assert big_galaxy == double_spaces(small_galaxy)

@pytest.mark.parametrize(
    "small_galaxy, sum",
    [
        (small_galaxy_path, 374)
    ]
)
def test_sum_distance(small_galaxy, sum):
    assert sum == sum_pair_distance(small_galaxy)

""" Day 11 Part 2 """

@pytest.mark.parametrize(
    "small_galaxy, multiplier, sum",
    [
        (small_galaxy_path, 2, 374),
        (small_galaxy_path, 10, 1030),
        (small_galaxy_path, 100, 8410),
    ]
)
def test_space_mutliplication(small_galaxy, multiplier, sum):
    assert sum == sum_distance_with_gap(small_galaxy, multiplier)