from app.split_integer import (
    split_integer
)  # Adjust import according to your structure


def test_single_part_returns_value() -> None:
    # When number_of_parts=1, result is just [value]
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]


def test_equal_parts_when_divisible() -> None:
    # When value divisible by number_of_parts, all parts equal
    result = split_integer(6, 2)
    assert result == [3, 3]
    assert all(isinstance(x, int) for x in result)

    result = split_integer(10, 5)
    assert result == [2, 2, 2, 2, 2]
    assert all(isinstance(x, int) for x in result)


def test_difference_between_max_and_min_is_at_most_one() -> None:
    # Result parts differ at most by 1
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1
    assert all(isinstance(x, int) for x in result)


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


# New critical tests added per review feedback:


def test_value_less_than_parts_distributes_zeros_and_ones() -> None:
    # e.g. value=3, parts=5 → [0,0,0,1,2] or similar
    result = split_integer(3, 5)
    assert len(result) == 5
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == 3
    assert all(isinstance(x, int) for x in result)


def test_value_equals_number_of_parts_all_ones() -> None:
    # e.g. value=5, parts=5 → [1,1,1,1,1]
    result = split_integer(5, 5)
    assert result == [1, 1, 1, 1, 1]
    assert len(result) == 5
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == 5
    assert all(isinstance(x, int) for x in result)


def test_large_input_smoke_test() -> None:
    # Check correctness properties with large input (not benchmarking)
    value = 10**6
    parts = 10**5
    result = split_integer(value, parts)
    assert len(result) == parts
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert sum(result) == value
    assert all(isinstance(x, int) for x in result)
