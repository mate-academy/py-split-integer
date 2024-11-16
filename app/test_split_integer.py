from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    """Ensure the sum of parts is equal to the input value."""
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    """Ensure parts are equal when the value is divisible ."""
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(10, 2) == [5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    """Ensure the function returns a single part equal to the value..."""
    assert split_integer(8, 1) == [8]
    assert split_integer(15, 1) == [15]
    assert split_integer(0, 1) == [0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    """Ensure the parts are sorted in ascending order."""
    assert split_integer(17, 4) == [4, 4, 4, 5]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert split_integer(9, 2) == [4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    """Ensure the function adds zeros when the value is less than..."""
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]
    assert split_integer(0, 3) == [0, 0, 0]
