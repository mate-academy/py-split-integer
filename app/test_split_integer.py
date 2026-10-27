from app.split_integer import split_integer


def test_split_into_one_part() -> None:
    """Test when parts is 1, returns the value in a list."""
    assert split_integer(8, 1) == [8]


def test_split_evenly() -> None:
    """Test when value is evenly divisible by parts."""
    assert split_integer(6, 2) == [3, 3]


def test_split_with_remainder() -> None:
    """Test when value leaves a remainder and distributes."""
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_with_larger_remainder() -> None:
    """Test with a larger number of parts and remainder."""
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_result_length_matches_number_of_parts() -> None:
    """Test that the length matches number of parts."""
    number_of_parts = 5
    result = split_integer(20, number_of_parts)
    assert len(result) == number_of_parts


def test_elements_are_sorted_ascending() -> None:
    """Test that the resulting array is sorted ascending."""
    result = split_integer(17, 4)
    assert result == sorted(result)


def test_difference_between_max_and_min_is_at_most_one() -> None:
    """Test that max and min difference is at most 1."""
    result = split_integer(32, 6)
    assert max(result) - min(result) <= 1
