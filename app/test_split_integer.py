import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (8, 1),
        (0, 3),
        (6, 2),
        (5, 7),
        (32, 6)
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, \
        f"Expected sum to be {value}, but got {sum(result)}"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (10, 2),
        (100, 10),
        (9, 3),
        (0, 5)
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert all(part == result[0] for part in result), \
        f"Not all parts are equal: {result}"


@pytest.mark.parametrize(
    "value",
    [0, 1, 5, 100, 999]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int) -> None:
    result = split_integer(value, 1)
    assert result == [value], f"Expected [{value}], but got {result}"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),  # [4, 4, 4, 5]
        (32, 6),  # [5, 5, 5, 5, 6, 6]
        (7, 3),   # [2, 2, 3]
        (5, 2)    # [2, 3]
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int, number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result), f"Result is not sorted: {result}"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (0, 3),  # [0, 0, 0]
        (2, 5),  # [0, 0, 0, 1, 1]
        (3, 7),  # [0, 0, 0, 0, 1, 1, 1]
        (1, 4)   # [0, 0, 0, 1]
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int, number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert len(result) == number_of_parts, \
        f"Expected {number_of_parts} parts, got {len(result)}"
    assert sum(result) == value, \
        f"Sum mismatch: expected {value}, got {sum(result)}"
    assert result == sorted(result), \
        f"Result not sorted: {result}"
    assert max(result) - min(result) <= 1, \
        f"Max-min difference too large: {result}"
