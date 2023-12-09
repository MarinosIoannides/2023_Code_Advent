import pytest
from day_9_code import predict_next, predict_first
""" Day 9 Tests """

@pytest.mark.parametrize(
    "sequence, next",
    [
        ([0, 3, 6, 9, 12, 15], 18),
        ([1, 3, 6, 10, 15, 21], 28),
        ([10, 13, 16, 21, 30, 45], 68),
    ]
)
def test_last_prediction(sequence, next):
    assert next == predict_next(sequence)

@pytest.mark.parametrize(
    "sequence, next",
    [
        ([0, 3, 6, 9, 12, 15], -3),
        ([1, 3, 6, 10, 15, 21], 0),
        ([10, 13, 16, 21, 30, 45], 5),
    ]
)
def test_first_prediction(sequence, next):
    assert next == predict_first(sequence)