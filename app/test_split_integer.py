from app.split_integer import split_integer


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(6, 2) == [3, 3]


def test_should_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]


def test_should_split_when_value_not_divisible_by_parts() -> None:
    assert split_integer(17, 4) == [4, 4, 4, 5]


def test_should_split_with_difference_not_greater_than_one() -> None:
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_split_when_number_of_parts_equals_value() -> None:
    assert split_integer(5, 5) == [1, 1, 1, 1, 1]


def test_should_split_when_number_of_parts_greater_than_value() -> None:
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
