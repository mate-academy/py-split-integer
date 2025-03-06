from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    pass
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(6, 2)) == 6
    assert sum(split_integer(17, 4)) == 17
    assert sum(split_integer(32, 6)) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    pass
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    pass
    assert split_integer(10, 1) == [10]
    assert split_integer(25, 1) == [25]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    pass
    assert split_integer(7, 3) == [2, 2, 3]
    assert split_integer(10, 4) == [2, 2, 3, 3]
    assert split_integer(32, 6) == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    pass
    assert split_integer(3, 5) == [0, 0, 1, 1, 1]
    assert split_integer(2, 4) == [0, 0, 1, 1]
