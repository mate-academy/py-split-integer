import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert sum(result) == value


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (6, 2, [3, 3]),
        (12, 4, [3, 3, 3, 3]),
        (20, 5, [4, 4, 4, 4, 4])
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int, parts: int, expected: int
) -> None:
    assert split_integer(value, parts) == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    parts = 1
    expected = [8]
    result = split_integer(value, parts)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    parts = 4
    result = split_integer(value, parts)
    assert result == sorted(result), f"Result {result} should be sorted"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    parts = 5
    result = split_integer(value, parts)
    assert result == [0, 0, 1, 1, 1], \
        f"Expected [0, 0, 1, 1, 1], but got {result}"
