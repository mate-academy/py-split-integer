import pytest

from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (10, 3, [3, 3, 4]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
    (6, 2, [3, 3])
])
def test_sum_of_the_parts_should_be_equal_to_value(
        value: int, number_of_parts: int, expected: list[int]
) -> None:
    result = split_integer(value, number_of_parts)
    assert sum(result) == value, (f"Sum of parts {result} does not "
                                  f"equal original value {value}")
    assert result == expected, (f"Result {result} does not "
                                f"match expected {expected}")


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (6, 2, [3, 3]),
    (12, 3, [4, 4, 4]),
    (9, 3, [3, 3, 3])
])
def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        value: int, number_of_parts: int, expected: list[int]
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected, (f"Expected equal parts "
                                f"{expected}, but got {result}")


@pytest.mark.parametrize("value, expected", [
    (8, [8]),
    (15, [15])
])
def test_should_return_part_equals_to_value_when_split_into_one_part(
        value: int, expected: list[int]
) -> None:
    result = split_integer(value, 1)
    assert result == expected, (f"Expected {expected} when splitting "
                                f"into one part, but got {result}")


@pytest.mark.parametrize("value, number_of_parts", [
    (17, 4),
    (32, 6)
])
def test_parts_should_be_sorted_when_they_are_not_equal(
        value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result), f"Parts {result} are not sorted"


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (3, 5, [0, 0, 1, 1, 1]),
    (2, 4, [0, 0, 1, 1])
])
def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        value: int, number_of_parts: int, expected: list[int]
) -> None:
    result = split_integer(value, number_of_parts)
    assert result == expected, (f"Expected {expected} but got {result} when "
                                f"value is less than number_of_parts")


@pytest.mark.parametrize("value, number_of_parts", [
    (10, 3),
    (17, 4),
    (32, 6),
    (6, 2)
])
def test_difference_between_max_and_min_should_be_less_than_or_equal_to_one(
        value: int, number_of_parts: int
) -> None:
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1, (f"Difference between max and min "
                                            f"in {result} is greater than 1")
