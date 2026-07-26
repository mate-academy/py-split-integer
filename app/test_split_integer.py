from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    """Ensure that the sum of parts equals the original value."""
    for value, parts in [(8, 1), (6, 2), (17, 4), (32, 6), (3, 5)]:
        assert sum(split_integer(value, parts)) == value, \
            f"Sum mismatch for {value} {parts}"


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    """When value is evenly divisible, all parts should be equal."""
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    """Splitting into one part should return a list with the original value."""
    assert split_integer(8, 1) == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    """Ensure parts are always sorted ascending."""
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    """When parts > value, result should contain zeros and ones."""
    result = split_integer(3, 5)

    assert result == [0, 0, 1, 1, 1]
    assert len(result) == 5
    assert sum(result) == 3
