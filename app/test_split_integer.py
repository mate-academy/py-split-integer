from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(11, 5)) == 11
    assert sum(split_integer(8, 1)) == 8
    assert sum(split_integer(1, 8)) == 1


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(8, 4) == [2, 2, 2, 2]
    assert split_integer(24, 6) == [4, 4, 4, 4, 4, 4]
    assert split_integer(100, 4) == [25, 25, 25, 25]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(1, 1) == [1]
    assert split_integer(22, 1) == [22]
    assert split_integer(0, 1) == [0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert sorted(split_integer(31, 5)) == [6, 6, 6, 6, 7]
    assert sorted(split_integer(73, 5)) == [14, 14, 15, 15, 15]
    assert sorted(split_integer(45, 5)) == [9, 9, 9, 9, 9]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(0, 5) == [0, 0, 0, 0, 0]
    assert split_integer(5, 6) == [0, 1, 1, 1, 1, 1]
    assert split_integer(2, 5) == [0, 0, 0, 1, 1]
