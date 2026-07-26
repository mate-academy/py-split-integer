import pytest
from app.split_integer import split_integer


def test_sum_of_parts_should_equal_value() -> None:
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(100, 7)) == 100
    assert sum(split_integer(5, 5)) == 5
    assert sum(split_integer(0, 3)) == 0  # edge case


def test_parts_sorted_and_difference_at_most_one() -> None:
    result = split_integer(10, 3)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1

    result = split_integer(100, 6)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1

    result = split_integer(25, 4)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1


def test_should_return_single_part_when_number_of_parts_is_one() -> None:
    assert split_integer(15, 1) == [15]
    assert split_integer(42, 1) == [42]
    assert split_integer(7, 1) == [7]


def test_should_add_zeros_when_value_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]
    assert split_integer(1, 3) == [0, 0, 1]


@pytest.mark.parametrize(
    "value,parts,expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6]),
        (0, 3, [0, 0, 0]),
        (1, 1, [1]),
    ]
)
def test_parametrized_examples(
    value: int,
    parts: int,
    expected: list[int]
) -> None:
    assert split_integer(value, parts) == expected
