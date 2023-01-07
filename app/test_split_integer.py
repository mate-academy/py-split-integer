from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4

    result_list = split_integer(value, number_of_parts)

    assert sum(result_list) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2

    result_list = split_integer(value, number_of_parts)

    assert result_list[0] == result_list[1]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 10
    number_of_parts = 1

    result_list = split_integer(value, number_of_parts)

    assert result_list[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    numbers_of_parts = 4

    result_list = split_integer(value, numbers_of_parts)

    assert result_list == sorted(result_list)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 2
    number_of_parts = 3

    result_list = split_integer(value, number_of_parts)

    expected_list = [0, 1, 1]

    assert result_list == expected_list
