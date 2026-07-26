import pytest
from app import split_integer


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (10, 3, [3, 3, 4]),
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (3, 5, [0, 0, 1, 1, 1]),
        (1, 4, [0, 0, 0, 1]),
        (2, 4, [0, 0, 1, 1]),
        (7, 3, [2, 2, 3]),
        (11, 4, [2, 3, 3, 3]),
        (14, 4, [3, 3, 4, 4]),
    ],
)
def test_split_integer_expected_outputs(
    value: int,
    parts: int,
    expected: list,
) -> None:
    assert split_integer.split_integer(value, parts) == expected


def test_sum_of_parts_equals_value() -> None:
    assert sum(split_integer.split_integer(17, 4)) == 17
    assert sum(split_integer.split_integer(32, 6)) == 32
    assert sum(split_integer.split_integer(6, 2)) == 6
    assert sum(split_integer.split_integer(12, 4)) == 12


def test_number_of_parts_is_correct() -> None:
    assert len(split_integer.split_integer(32, 6)) == 6
    assert len(split_integer.split_integer(3, 5)) == 5
    assert len(split_integer.split_integer(6, 2)) == 2


def test_parts_are_sorted_ascending() -> None:
    result = split_integer.split_integer(12, 4)
    assert result == sorted(result)

    result = split_integer.split_integer(32, 6)
    assert result == sorted(result)


def test_difference_between_max_and_min_is_at_most_one() -> None:
    result = split_integer.split_integer(12, 4)
    assert max(result) - min(result) <= 1

    result = split_integer.split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_split_into_equal_parts_when_divisible() -> None:
    assert split_integer.split_integer(6, 2) == [3, 3]
    assert split_integer.split_integer(20, 5) == [4, 4, 4, 4, 4]


def test_parts_greater_than_value() -> None:
    assert split_integer.split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_split_into_one_part() -> None:
    assert split_integer.split_integer(8, 1) == [8]
