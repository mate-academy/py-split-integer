from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert split_integer(8, 2) == [4, 4]
    assert split_integer(6, 3) == [2, 2, 2]
    assert split_integer(17, 5) == [3, 3, 3, 4, 4]
    assert split_integer(32, 8) == [4, 4, 4, 4, 4, 4, 4, 4]


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert split_integer(8, 5) == [1, 1, 2, 2, 2]
    assert split_integer(9, 6) == [1, 1, 1, 2, 2, 2]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(6, 1) == [6]
    assert split_integer(17, 1) == [17]
    assert split_integer(32, 1) == [32]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(10, 3) == [3, 3, 4]
    assert split_integer(12, 4) == [3, 3, 3, 3]
    assert split_integer(8, 5) == [1, 1, 2, 2, 2]
    assert split_integer(9, 6) == [1, 1, 1, 2, 2, 2]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(8, 5) == [1, 1, 2, 2, 2]
    assert split_integer(9, 6) == [1, 1, 1, 2, 2, 2]
