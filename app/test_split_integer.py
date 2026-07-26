import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (100, 7),
        (3, 5),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value and len(parts) == number_of_parts


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(1, 1) == [1]
    assert split_integer(42, 1) == [42]


@pytest.mark.parametrize(
    "value,number_of_parts",
    [(17, 4), (32, 6), (10, 3)],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int
) -> None:
    parts = split_integer(value, number_of_parts)
    assert parts == sorted(parts) and max(parts) - min(parts) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
