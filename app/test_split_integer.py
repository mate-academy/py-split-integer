import pytest
from typing import List
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int, expected: List[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 4, [2, 2, 2, 2]),
        (10, 2, [5, 5]),
        (9, 3, [3, 3, 3]),
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int, expected: List[int]
) -> None:
    assert split_integer(value, number_of_parts) == expected


if __name__ == "__main__":
    pytest.main()
