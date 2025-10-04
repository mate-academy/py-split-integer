from app.split_integer import split_integer
import pytest


@pytest.mark.parametrize(
    "value, parts",
    [
        (1, 1),
        (6, 2),
        (8, 3),
        (17, 4),
        (32, 6),
        (100, 7),
        (3, 3),  # boundary: value == number_of_parts
    ],
)
def test_sum_len_and_types(value: int, parts: int) -> None:
    """Sum equals value; length equals parts; all items are ints."""
    result = split_integer(value, parts)
    assert sum(result) == value
    assert len(result) == parts
    assert all(isinstance(x, int) for x in result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(8, 4) == [2, 2, 2, 2]
    # boundary: value == parts -> all ones
    assert split_integer(3, 3) == [1, 1, 1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(1, 1) == [1]
    assert split_integer(123, 1) == [123]


@pytest.mark.parametrize(
    "value, parts",
    [
        (17, 4),   # expected [4, 4, 4, 5]
        (32, 6),   # expected [5, 5, 5, 5, 6, 6]
        (7, 3),    # expected [2, 2, 3]
        (5, 2),    # expected [2, 3]
        (3, 5),    # expected [0, 0, 1, 1, 1]
    ],
)
def test_sorted_and_remainder_distribution(value: int, parts: int) -> None:
    result = split_integer(value, parts)

    # basic shape constraints
    assert len(result) == parts
    assert all(isinstance(x, int) for x in result)
    assert sum(result) == value

    # sorted ascending
    assert result == sorted(result)

    # tight spread
    if result:
        assert max(result) - min(result) <= 1

    # remainder distribution check:
    base = value // parts
    remainder = value % parts
    min_val = min(result) if result else 0

    assert min_val == base
    assert result.count(base + 1) == remainder
    assert result.count(base) == parts - remainder


@pytest.mark.parametrize(
    "value, parts, expected",
    [
        (1, 4, [0, 0, 0, 1]),
        (2, 5, [0, 0, 0, 1, 1]),
        (3, 5, [0, 0, 1, 1, 1]),
    ],
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int, parts: int, expected: list[int]
) -> None:
    """When value < parts, zeros must appear and array remains sorted."""
    result = split_integer(value, parts)
    assert result == expected
    assert len(result) == parts
    assert all(isinstance(x, int) for x in result)
