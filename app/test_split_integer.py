import pytest
from typing import List

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        pytest.param(
            32,
            6,
            [5, 5, 5, 5, 6, 6],
            id="parts_should_be_sorted_when_they_are_not_equal",
        ),
        pytest.param(
            6,
            2,
            [3, 3],
            id="Should_split_into_equal_parts_when_value_divisible_by_parts",
        ),
        pytest.param(
            8,
            1,
            [8],
            id="should_return_part_equals_to_value_when_split_into_one_part",
        ),
        pytest.param(
            3,
            6,
            [0, 0, 0, 1, 1, 1],
            id="should_add_zeros_when_value_is_less_than_number_of_parts",
        ),
    ],
)
def test_split_integer(value: int, parts: int, expected: List[int]) -> None:
    assert split_integer(value, parts) == expected
