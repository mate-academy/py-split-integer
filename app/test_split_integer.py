from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 10
    number_of_parts = 3
    return_list = split_integer(value, number_of_parts)
    assert sum(return_list) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 15
    number_of_parts = 5
    return_list = split_integer(value, number_of_parts)
    assert return_list == [3, 3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 100
    number_of_parts = 1
    return_list = split_integer(value, number_of_parts)
    assert return_list == [value]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    return_list = split_integer(value, number_of_parts)
    assert return_list == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 3
    return_list = split_integer(value, number_of_parts)
    assert return_list == [0, 1, 1]
