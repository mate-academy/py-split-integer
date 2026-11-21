import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts, expected",
                         [
                             (1, 1, [1]),
                             (8, 1, [8]),
                             (2, 2, [1, 1]),
                             (3, 2, [1, 2]),
                             (4, 3, [1, 1, 2]),
                             (5, 2, [2, 3]),
                             (6, 2, [3, 3]),
                             (7, 3, [2, 2, 3]),
                             (10, 3, [3, 3, 4]),
                             (17, 4, [4, 4, 4, 5]),
                             (32, 6, [5, 5, 5, 5, 6, 6]),
                             (2, 5, [0, 0, 0, 1, 1]),
                             (1, 3, [0, 0, 1]),
                             (11, 4, [2, 3, 3, 3]),
                             (20, 7, [2, 3, 3, 3, 3, 3, 3]),
                             (9, 4, [2, 2, 2, 3]),
                             (3, 5, [0, 0, 1, 1, 1]),
                         ]
)

def test_split_integer(value, number_of_parts, expected):
    assert split_integer(value, number_of_parts) == expected