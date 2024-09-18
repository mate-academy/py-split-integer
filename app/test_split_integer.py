from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 9
    sum_of_the_parts = sum(split_integer(value, 2))
    assert sum_of_the_parts == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 10
    actual_list = split_integer(value, 2)
    assert actual_list == [5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 3
    actual_list = split_integer(value, 1)
    assert actual_list == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 13
    actual_list = split_integer(value, 3)
    assert actual_list == [5, 4, 4]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    actual_list = split_integer(value, 2)
    assert actual_list == [0, 1]
