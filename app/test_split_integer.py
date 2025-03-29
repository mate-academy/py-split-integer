from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, number_of_parts = 6, 2
    result = sum(split_integer(value, number_of_parts))
    assert result == 6


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, number_of_parts = 6, 2
    result = split_integer(value, number_of_parts)
    assert result == [3, 3]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 6, 1
    result = split_integer(value, number_of_parts)
    assert result == [6]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, number_of_parts = 17, 4
    result = split_integer(value, number_of_parts)
    assert result == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, number_of_parts = 2, 3
    result = split_integer(value, number_of_parts)
    assert result == [0, 1, 1]
