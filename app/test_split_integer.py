import pytest

from app import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (100, 7, [14, 14, 14, 14, 14, 15, 15]),
        (17, 4, [4, 4, 4, 5]),
    ],
)
def test_should_return_expected_parts(
    value: int, number_of_parts: int, expected: list
) -> None:
    assert split_integer.split_integer(value, number_of_parts) == expected


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer.split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]
