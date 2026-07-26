from app.split_integer import split_integer


def test_single_part_returns_value() -> None:
    """Splitting into one part returns the original value"""
    assert split_integer(8, 1) == [8]


def test_even_division() -> None:
    """Value divisible by number_of_parts splits evenly"""
    assert split_integer(6, 2) == [3, 3]


def test_uneven_division() -> None:
    """Value not divisible evenly splits correctly"""
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_larger_case() -> None:
    """Larger value split into multiple parts"""
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_value_less_than_parts() -> None:
    """When value < number_of_parts, zeros are added and sum matches value"""
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]
    assert sum(result) == 3


def test_max_minus_min_less_equal_one() -> None:
    """Difference between max and min in the list is <= 1"""
    for value, parts in [(17, 4), (32, 6), (3, 5), (10, 3), (1, 1)]:
        result = split_integer(value, parts)
        assert max(result) - min(result) <= 1


def test_sorted_ascending() -> None:
    """Result list is always sorted ascending"""
    for value, parts in [(17, 4), (32, 6), (3, 5), (10, 3)]:
        result = split_integer(value, parts)
        assert result == sorted(result)


def test_length_matches_number_of_parts() -> None:
    """Length of result equals number_of_parts"""
    for value, parts in [(17, 4), (32, 6), (3, 5), (10, 3), (8, 1)]:
        assert len(split_integer(value, parts)) == parts


def test_sum_of_parts_equals_value() -> None:
    """Sum of returned parts equals the original value"""
    for value, parts in [(17, 4), (32, 6), (3, 5), (10, 3), (8, 1)]:
        assert sum(split_integer(value, parts)) == value
