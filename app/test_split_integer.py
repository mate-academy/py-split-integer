import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (11, 4, [2, 3, 3, 3]),
        (2, 3, [0, 1, 1]),
        (10, 3, [3, 3, 4]),
        (5, 5, [1, 1, 1, 1, 1]),
    ]
)
def test_split_integer_cases(
    value: int,
    number_of_parts: int,
    expected: list
) -> None:
    assert split_integer(value, number_of_parts) == expected


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = 4
    assert sum(split_integer(value, parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)
    assert result == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
