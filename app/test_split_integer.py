from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    value, number_of_parts = 17, 4
    assert value == sum(split_integer(value, number_of_parts))


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    value, number_of_parts = 18, 3
    assert split_integer(value, number_of_parts) == [6, 6, 6]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    value, number_of_parts = 8, 1
    assert [value] == split_integer(value, number_of_parts)


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    value, number_of_parts = 32, 6
    # created a new variable 'result' to simplify the readability of code
    # in assert section
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    value, number_of_parts = 4, 6
    assert split_integer(value, number_of_parts) == [0, 0, 1, 1, 1, 1]
