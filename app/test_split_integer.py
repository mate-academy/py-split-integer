from app.split_integer import split_integer


def test_single_part() -> None:
    """Test splitting into 1 part returns original number"""
    assert split_integer(8, 1) == [8]


def test_two_equal_parts() -> None:
    """Test splitting a number evenly into two parts"""
    assert split_integer(6, 2) == [3, 3]


def test_split_with_remainder() -> None:
    """Test splitting with remainder distributes +1 to largest parts"""
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_even_distribution() -> None:
    """Test splitting into parts where some numbers need to be +1"""
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_length_matches_number_of_parts() -> None:
    """Ensure the returned array has exactly number_of_parts elements"""
    assert len(split_integer(17, 4)) == 4


def test_difference_between_max_and_min() -> None:
    """Ensure the difference between max and min is <= 1"""
    result = split_integer(17, 4)
    assert max(result) - min(result) <= 1


def test_sorted_ascending() -> None:
    """Ensure the result array is sorted in ascending order"""
    result = split_integer(17, 4)
    assert result == sorted(result)
