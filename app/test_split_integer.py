from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    return_list = split_integer(10, 3)
    assert sum(return_list) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    return_list = split_integer(15, 5)
    assert return_list == [3, 3, 3, 3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    return_list = split_integer(100, 1)
    assert return_list == [100]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    return_list = split_integer(17, 4)
    assert return_list == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 3
    return_list = split_integer(value, number_of_parts)
    assert return_list == [0, 1, 1]
