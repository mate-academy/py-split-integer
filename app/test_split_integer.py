import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,expectation",
    [
        (17, 4, [4, 4, 4, 5]),
        (6, 2, [3, 3]),
        (8, 1, [8]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (5, 8, [0, 0, 0, 1, 1, 1, 1, 1]),
    ],
    ids=[
        "test_sum_of_the_parts_should_be_equal_to_value",
        "test_should_split_into_equal_parts_when_value_divisible_by_parts",
        "test_should_return_part_equals_to_value_when_split_into_one_part",
        "test_parts_should_be_sorted_when_they_are_not_equal",
        "test_should_add_zeros_when_value_is_less_than_number_of_parts"
    ]
)
def test_split_integer(
        value: int,
        number_of_parts: int,
        expectation: str
) -> None:
    assert split_integer(value, number_of_parts) == expectation
