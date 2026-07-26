from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert sum(result) == value and (max(result) - min(result) <= 1)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 6
    number_of_parts = 2
    num = value // number_of_parts
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert len(result) == number_of_parts and set(result) == {num}


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert len(result) == number_of_parts and result[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 32
    number_of_parts = 6
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 4
    number_of_parts = 6
    result = split_integer(value=value, number_of_parts=number_of_parts)
    assert value < number_of_parts and sum(result[:(number_of_parts - value) - 1]
                                           ) == 0 and sum(result[(number_of_parts - value):]) == value
