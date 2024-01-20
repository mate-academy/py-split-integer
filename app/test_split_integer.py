from app.split_integer import split_integer
import pytest


def test_sum_of_the_parts_should_be_equal_to_value() \
        -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert sum(result) == value, ("The sum of the parts should equal the "
                                  "original value")


def test_should_split_into_equal_parts_when_value_divisible_by_parts() \
        -> None:
    value, parts = 20, 5
    result = split_integer(value, parts)
    assert result == [value // parts] * parts, \
        ("Should split into equal parts when value is "
         "divisible by number of parts")


def test_should_return_part_equals_to_value_when_split_into_one_part() \
        -> None:
    value = 10
    result = split_integer(value, 1)
    assert result == [value], ("Should return a single part equal to value "
                               "when split into one part")


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, parts = 17, 4
    result = split_integer(value, parts)
    assert result == sorted(result), ("Parts should be sorted in ascending "
                                      "order")


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, parts = 3, 5
    result = split_integer(value, parts)
    expected_zeros = parts - value
    assert result.count(0) == expected_zeros, ("Should add zeros when "
                                               "value is less than number"
                                               " of parts")
    assert len(result) == parts, ("The number of parts should be equal"
                                  " to the requested number of parts")
    assert sum(result) == value, ("The sum of the parts should equal"
                                  " the original value")


# This is an optional step to run all tests if you run this script directly
if __name__ == "__main__":
    pytest.main()
