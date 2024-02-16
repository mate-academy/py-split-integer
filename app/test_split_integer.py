from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, number_of_parts = 6, 2
    result = split_integer(value, number_of_parts)
    assert value == sum(result)


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, number_of_parts = 200, 4
    result = split_integer(value, number_of_parts)
    assert result == [50, 50, 50, 50]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 233, 1
    result = split_integer(value, number_of_parts)
    assert result == [233]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, number_of_parts = 189, 8
    result = split_integer(value, number_of_parts)
    assert result == [23, 23, 23, 24, 24, 24, 24, 24]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, number_of_parts = 3, 7
    result = split_integer(value, number_of_parts)
    assert result == [0, 0, 0, 0, 1, 1, 1]
