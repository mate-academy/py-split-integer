from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value = 6
    number_of_parts = 2
    result = split_integer(value, number_of_parts)
    assert sum(result) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value = 16
    number_of_parts = 4
    result = split_integer(value, number_of_parts)
    assert result == [4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value = 6
    result = split_integer(value, 1)
    assert result == [6]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(32, 6) == [5, 5, 5, 5, 6, 6]
    assert result, "Should be sorted when they are not equal"


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value = 16
    number_of_parts = 17
    result = split_integer(value, number_of_parts)
    assert result == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
