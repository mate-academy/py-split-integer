import pytest

from app import split_integer as si


@pytest.mark.parametrize(
    ("value", "num_of_parts"),
    [
        (0, 1),
        (1, 1),
        (6, 2),
        (17, 4),
        (1, 2),
        (25, 7),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        num_of_parts: int
) -> None:
    assert sum(si.split_integer(value, num_of_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert si.split_integer(6, 2) == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert si.split_integer(17, 1) == [17]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert si.split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert si.split_integer(1, 2) == [0, 1]
