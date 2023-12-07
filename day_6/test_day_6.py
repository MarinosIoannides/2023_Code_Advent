import pytest
from day_6_code import calc_times

""" Day 1 Part 1 """
@pytest.mark.parametrize(
    "time_distance, beats",
    [
        (("7", "9"), 4),
        (("15", "40"), 8),
        (("30", "200"), 9),
    ]
)
def test_wins(time_distance, beats):
    assert beats == calc_times(time_distance)