import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, parts, expected_sum", [
    (10, 3, 10),
    (7, 2, 7),
    (0, 5, 0),
    (100, 7, 100),
])
def test_sum_of_the_parts_should_be_equal_to_value(value: int,
                                                   parts: int,
                                                   expected_sum: int) -> None:
    assert sum(split_integer(value, parts)) == expected_sum


@pytest.mark.parametrize("value, parts, expected", [
    (12, 3, [4, 4, 4]),
    (10, 5, [2, 2, 2, 2, 2]),
    (0, 4, [0, 0, 0, 0]),
])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int,
        parts: int,
        expected: list) -> None:
    assert split_integer(value, parts) == expected


@pytest.mark.parametrize("value, expected", [
    (7, [7]),
    (0, [0]),
    (100, [100]),
])
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int,
        expected: list) -> None:
    assert split_integer(value, 1) == expected


@pytest.mark.parametrize("value, parts", [
    (10, 3),
    (7, 4),
    (100, 6),
])
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int,
        parts: int) -> None:
    result = split_integer(value, parts)
    assert result == sorted(result)
    assert result[-1] - result[0] <= 1


@pytest.mark.parametrize("value, parts, expected", [
    (2, 5, [0, 0, 0, 1, 1]),
    (1, 4, [0, 0, 0, 1]),
    (0, 3, [0, 0, 0]),
])
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int,
        parts: int,
        expected: list) -> None:
    assert split_integer(value, parts) == expected
