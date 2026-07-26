from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    """The sum of all parts should be equal to the original value."""
    assert sum(split_integer(10, 3)) == 10
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    """If the value is evenly divisible, all parts should be equal."""
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    """If splitting into one part, return the value as is."""
    assert split_integer(8, 1) == [8]
    assert split_integer(100, 1) == [100]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    """Ensure the resulting parts are sorted in ascending order."""
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(20, 6) == [3, 3, 3, 3, 4, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    """If value is less than the number of parts, zeros should be added."""
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]


def test_difference_between_max_and_min_should_be_at_most_one() -> None:
    """Ensure that max and min values in the result differ by at most 1."""
    for value, parts in [(10, 3), (17, 4), (32, 6)]:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_result_should_be_sorted_ascending() -> None:
    """Ensure the resulting list is sorted in ascending order."""
    for value, parts in [(10, 3), (17, 4), (32, 6)]:
        result = split_integer(value, parts)
        assert result == sorted(result)
