import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(17, 4)) == 17, (
        "Sum of the parts should be equal to the value"
    )


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3], (
        "Should split into equal parts when value is divisible by parts"
    )


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8], (
        "Should return part equals to value when split into one part"
    )


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5], (
        "Parts should be sorted when they are not equal"
    )


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1], (
        "Should add zeros when value is less than number of parts"
    )


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    parts = split_integer(32, 6)
    assert max(parts) - min(parts) <= 1, (
        "Difference between max and min parts should be at most 1"
    )


def test_edge_case_large_number_of_parts() -> None:
    assert split_integer(10, 100) == [0] * 90 + [1] * 10, (
        "Should handle cases where number_of_parts is much larger than value"
    )


def test_edge_case_large_value() -> None:
    assert split_integer(1000000, 3) == [333333, 333333, 333334], (
        "Should handle cases with large value"
    )


if __name__ == "__main__":
    pytest.main()
