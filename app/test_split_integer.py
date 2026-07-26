from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    assert sum(split_integer(value, 4)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    res_list = [4, 4, 4, 4]
    value = 16
    parts = 4
    assert split_integer(value, parts) == res_list


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    parts = 1
    res_list = [8]
    assert split_integer(value, parts) == res_list


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    parts = 6
    res_list = [5, 5, 5, 5, 6, 6]
    assert split_integer(value, parts) == res_list


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 1
    parts = 2
    res_list = [0, 1]
    assert split_integer(value, parts) == res_list
