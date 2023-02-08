from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    result_list_of_function = split_integer(value, number_of_parts)
    assert (sum(result_list_of_function) == value)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 18
    number_of_parts = 9
    result_list_of_function = split_integer(value, number_of_parts)
    assert (result_list_of_function[0] == result_list_of_function[1])


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 17
    number_of_parts = 1
    result_list_of_function = split_integer(value, number_of_parts)
    assert (result_list_of_function == [value])


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    result_list_of_function = split_integer(value, number_of_parts)
    assert (result_list_of_function == sorted(result_list_of_function))


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 4
    result_list_of_function = split_integer(value, number_of_parts)
    actual_list = [0, 0, 1, 1]
    assert (result_list_of_function == actual_list)
