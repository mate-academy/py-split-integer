from app.split_integer import (
    split_integer
)  # Adjust import according to your structure


def test_single_part_returns_value() -> None:
    # When number_of_parts=1, result is just [value]
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]


def test_equal_parts_when_divisible() -> None:
    # When value divisible by number_of_parts, all parts equal
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]


def test_difference_between_max_and_min_is_at_most_one() -> None:
    # Result parts differ at most by 1
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_result_sorted_ascending() -> None:
    # Result is always sorted ascending
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_parts_length_is_number_of_parts() -> None:
    # Result length equals number_of_parts
    parts = split_integer(32, 6)
    assert len(parts) == 6


def test_values_sum_up_to_original_value() -> None:
    # Sum of all parts equals value
    value = 32
    parts = split_integer(value, 6)
    assert sum(parts) == value


def test_example_cases() -> None:
    # Testing given examples explicitly
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
