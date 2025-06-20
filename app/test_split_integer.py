from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    parts = split_integer(value, number_of_parts)
    assert sum(parts) == value, f"Sum of parts {parts} should equal {value}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    # Evenly divisible cases
    assert split_integer(6, 2) == [3, 3]
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    # Splitting into one part returns the value itself
    assert split_integer(8, 1) == [8]
    assert split_integer(123, 1) == [123]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parts = split_integer(17, 4)
    # The list should be sorted ascending
    assert parts == sorted(parts), f"Parts {parts} are not sorted"
    # And the difference between max and min should be <= 1
    assert max(parts) - min(parts) <= 1, \
        f"Difference between max and min in {parts} is greater than 1"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    # When value < number_of_parts, zeros should appear for parts
    parts = split_integer(3, 5)
    assert parts == [0, 0, 1, 1, 1], f"Expected [0, 0, 1, 1, 1], got {parts}"
    # Also check a different scenario
    parts_small = split_integer(2, 5)
    assert parts_small.count(0) == 3 and parts_small.count(1) == 2, \
        f"Expected three zeros and two ones in {parts_small}"
