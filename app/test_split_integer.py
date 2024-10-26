from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    integer = split_integer(8, 2)
    assert sum(integer) == 8


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    integer = split_integer(32, 6)
    assert integer == [5, 5, 5, 5, 6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    integer = split_integer(6, 1)
    assert integer == [6]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    integer = split_integer(28, 6)
    assert integer == sorted(integer)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    integer = split_integer(3, 6)
    assert integer == [0, 0, 0, 1, 1, 1]
