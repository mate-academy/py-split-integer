import pytest

from app import split_integer


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (8, 1),
        (6, 2),
        (17, 4),
        (32, 6),
        (11, 3),
        (100, 7),
    ],
)
def test_sum_of_the_parts_should_be_equal_to_value(
    value: int, number_of_parts: int
) -> None:
    result = split_integer.split_integer(value, number_of_parts)
    assert sum(result) == value


@pytest.mark.parametrize(
    "value,number_of_parts,expected",
    [
        (6, 2, [3, 3]),
        (9, 3, [3, 3, 3]),
        (32, 8, [4, 4, 4, 4, 4, 4, 4, 4]),
    ],
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int, number_of_parts: int, expected: list
) -> None:
    assert split_integer.split_integer(value, number_of_parts) == expected


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (17, 4),
        (32, 6),
        (11, 3),
        (100, 7),
    ],
)
def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int, number_of_parts: int
) -> None:
    result = split_integer.split_integer(value, number_of_parts)
    assert result == sorted(result)


@pytest.mark.parametrize(
    "value,number_of_parts",
    [
        (17, 4),
        (32, 6),
        (11, 3),
        (100, 7),
        (3, 5),
    ],
)
def test_difference_between_max_and_min_should_not_exceed_one(
    value: int, number_of_parts: int
) -> None:
    result = split_integer.split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]
