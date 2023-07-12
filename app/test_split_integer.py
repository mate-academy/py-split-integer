from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    sum_of_result_of_function = sum(split_integer(17, 4))

    assert sum_of_result_of_function == 17


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    result_of_list = split_integer(32, 6)

    assert len(result_of_list) == 6


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result_of_list = split_integer(8, 0)

    assert len(result_of_list) == 0


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result_of_list = split_integer(32, 6)
    sorted_list = sorted(result_of_list)

    assert sorted_list == result_of_list


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result_of_list = split_integer(3, 4)

    assert 0 in result_of_list
