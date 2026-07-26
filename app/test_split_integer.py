import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (10, 3, [3, 3, 4]),
        (16, 4, [4, 4, 4, 4]),
        (17, 5, [3, 3, 3, 4, 4]),
        (3, 4, [0, 1, 1, 1]),
        (0, 5, [0, 0, 0, 0, 0]),
        (100, 1, [100]),
    ]
)
def test_split_integer_basic_constraints(
        value: int,
        parts: int,
        expected: list) -> None:
    result = split_integer(value, parts)

    assert result == expected
    assert len(result) == parts
    assert sum(result) == value
    assert result == sorted(result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(16, 4) == [4, 4, 4, 4]


def test_uneven_split_distribution_logic() -> None:
    result = split_integer(10, 3)
    assert max(result) - min(result) <= 1
    assert result.count(max(result)) == 10 % 3


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_different_number_of_parts_produce_different_lengths() -> None:
    assert len(split_integer(10, 3)) == 3
    assert len(split_integer(10, 4)) == 4
    assert split_integer(10, 3) != split_integer(10, 4)
