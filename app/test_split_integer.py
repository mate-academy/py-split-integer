from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
    (10, 3, [3, 3, 4]),
    (9, 4, [2, 2, 2, 3]),
    (15, 5, [3, 3, 3, 3, 3]),
    (20, 4, [5, 5, 5, 5]),
    (7, 2, [3, 4]),
    (14, 3, [4, 5, 5])
])
def test_split_integer(value: int,
                       number_of_parts: int,
                       expected: list) -> None:
    assert split_integer(value, number_of_parts) == expected
