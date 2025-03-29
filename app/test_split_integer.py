import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (9, 3, [3, 3, 3]),
        (10, 3, [3, 3, 4]),
        (7, 3, [2, 2, 3]),
        (5, 5, [1, 1, 1, 1, 1]),
        (4, 5, [0, 1, 1, 1, 1]),
    ],
)
def test_various_scenarios(value: int,
                           number_of_parts: int,
                           expected: list) -> None:
    parts = split_integer(value, number_of_parts)
    assert parts == expected
