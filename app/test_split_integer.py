import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(8, 1)) == 8, \
        "Sum of parts does not equal the original value"
    assert sum(split_integer(17, 4)) == 17, \
        "Sum of parts does not equal the original value"
    assert sum(split_integer(32, 6)) == 32, \
        "Sum of parts does not equal the original value"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(8, 4) == [2, 2, 2, 2], "Parts are not equal"
    assert split_integer(12, 6) == [2, 2, 2, 2, 2, 2], "Parts are not equal"
    assert split_integer(9, 3) == [3, 3, 3], "Parts are not equal"


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], \
        "Result does not equal the original value"
    assert split_integer(5, 1) == [5], \
        "Result does not equal the original value"


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result), "Parts are not sorted"
    result = split_integer(32, 6)
    assert result == sorted(result), "Parts are not sorted"


def test_difference_between_max_and_min_should_be_at_most_1() -> None:
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1, \
        "Difference between max and min parts is greater than 1"
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1, \
        "Difference between max and min parts is greater than 1"
    result = split_integer(5, 3)
    assert max(result) - min(result) <= 1, \
        "Difference between max and min parts is greater than 1"


if __name__ == "__main__":
    pytest.main()
