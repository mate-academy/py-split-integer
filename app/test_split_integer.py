from app.split_integer import split_integer


def test_split_into_one_part_returns_original_value():
    assert split_integer(8, 1) == [8]


def test_split_one_into_one_part():
    assert split_integer(1, 1) == [1]


def test_split_evenly_when_value_is_divisible():
    assert split_integer(6, 2) == [3, 3]


def test_split_when_remainder_is_one():
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_split_when_remainder_is_more_than_one():
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_split_when_remainder_is_one_less_than_parts():
    assert split_integer(19, 5) == [3, 4, 4, 4, 4]


def test_split_when_value_equals_number_of_parts():
    assert split_integer(4, 4) == [1, 1, 1, 1]


def test_split_when_value_is_less_than_number_of_parts():
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]


def test_split_one_into_multiple_parts():
    assert split_integer(1, 4) == [0, 0, 0, 1]
