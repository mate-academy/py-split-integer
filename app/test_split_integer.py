from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(10, 3)) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 40
    number_of_parts = 8
    assert sum(value, number_of_parts(40, 8)) == [5, 5, 5, 5, 5, 5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 20
    number_of_parts = 1
    assert sum(value, number_of_parts(20, 1)) == [20]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 7
    number_of_parts = 3
    assert sum(value, number_of_parts(7, 3)) == [2, 2, 3]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 3
    number_of_parts = 5
    assert sum(value, number_of_parts(3, 5)) == [0, 0, 1, 1, 1]
