import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (6, 2, [3, 3]),
        (17, 4, [4, 4, 4, 5]),
        (32, 6, [5, 5, 5, 5, 6, 6])
    ]
)
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (6, 2, [3, 3]),
        (12, 4, [3, 3, 3, 3]),
    ]
)
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize(
    "value, number_of_parts, expected",
    [
        (8, 1, [8]),
        (15, 1, [15]),
    ]
)
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (17, 4),
        (32, 6),
    ]
)
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result),\
        f"Parts should be sorted, but got {result}"


@pytest.mark.parametrize(
    "value, number_of_parts",
    [
        (3, 5, [0, 0, 1, 1, 1]),
        (0, 3, [0, 0, 0]),
    ]
)
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        number_of_parts: int,
        expected: list[int]
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected,\
        f"Expected {expected}, but got {result}"
