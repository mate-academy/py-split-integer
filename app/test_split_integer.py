from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 32
    number_of_parts = 6
    sum_of_numbers = sum(split_integer(value, number_of_parts))
    assert sum_of_numbers == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 30
    number_of_parts = 6
    result = split_integer(value, number_of_parts)
    assert result == [5, 5, 5, 5, 5, 5]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 8
    number_of_parts = 1
    result = split_integer(value, number_of_parts)
    assert result == [8]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value = 17
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 5
    number_of_parts = 6
    result = split_integer(value, number_of_parts)
    assert result == [0, 1, 1, 1, 1, 1]
