import pytest
from day_7_code import determine_kind, with_jokers

""" Day 7 Part 1 """
@pytest.mark.parametrize(
    "cards, kind",
    [
        ("AAAAA", 0),
        ("AA8AA", 1),
        ("23332", 2),
        ("TTT98", 3),
        ("23432", 4),
        ("A23A4", 5),
        ("23456", 6),
        ("32T3K", 5),
        ("T55J5", 3),
        ("KK677", 4),
        ("KTJJT", 4),
        ("QQQJA", 3),
    ]
)
def test_wins(cards, kind):
    assert kind == determine_kind(cards)

""" Day 7 Part 2 """
@pytest.mark.parametrize(
    "cards, kind",
    [
        ("32T3K", 5),
        ("T55J5", 1),
        ("KK677", 4),
        ("KTJJT", 1),
        ("QQQJA", 1),
    ]
)
def test_wins_j(cards, kind):
    assert kind == with_jokers(cards)