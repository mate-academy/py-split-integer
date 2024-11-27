from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 32
    number_of_parts = 6
    output_list = split_integer(value, number_of_parts)
    assert sum(output_list) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 32
    number_of_parts = 6
    output_list = split_integer(value, number_of_parts)

    for element in output_list:
        assert element == value // number_of_parts


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    output_list = split_integer(value, number_of_parts)
    assert sum(output_list) == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    output_list = split_integer(value, number_of_parts)
    for index in range(len(output_list) - 1):
        assert output_list[index] <= output_list[index + 1]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    number_of_parts = 8
    output_list = split_integer(value, number_of_parts)
    count_of_zeros = number_of_parts - value
    assert output_list.count(0) == count_of_zeros
