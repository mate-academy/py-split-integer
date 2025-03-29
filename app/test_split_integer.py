from app.split_integer import split_integer


import pytest


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17, \
        "Sum of parts is not equal to value"


@pytest.mark.parametrize(
    "value, parts_number, result",
    [
        (8, 2, [4, 4]),
        (9, 3, [3, 3, 3])
    ],
    ids=[
        "evens",
        "odds"
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        parts_number: int,
        result: list
) -> None:
    assert split_integer(value, parts_number) == result, \
        f"Parts are not equal, despite {value} is divisible by {parts_number}"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], \
        "Part is not equal to value when split into one part"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == sorted(split_integer(17, 4)), \
        "Parts are not sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 4) == [0, 0, 1, 1], \
        "Zeroes are not added when value < number of parts"
