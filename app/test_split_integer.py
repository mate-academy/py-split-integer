import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected_parts",
    [
        (10, 2, [5, 5]),
        (15, 3, [5, 5, 5]),
        (20, 4, [5, 5, 5, 5]),
        (10, 1, [10]),
        (25, 2, [12, 13]),
        (30, 5, [6, 6, 6, 6, 6]),
        (7, 4, [2, 2, 2, 1]),
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    number_of_parts: int,
    expected_parts: list[int]
) -> None:
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 2),
        (15, 3),
        (20, 4),
        (25, 5),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    expected_part_value = value // number_of_parts
    assert all(part == expected_part_value for part in parts)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 10
    number_of_parts = 1
    parts = split_integer(value, number_of_parts)
    assert parts == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 25
    number_of_parts = 2
    parts = split_integer(value, number_of_parts)
    assert parts == [12, 13]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 4
    number_of_parts = 5
    parts = split_integer(value, number_of_parts)
    assert parts == [0, 1, 1, 1, 1]
