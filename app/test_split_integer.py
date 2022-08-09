from app.split_integer import split_integer


def test_sum_or_the_parts_should_be_equal_to_value():
    value, number_of_parts = 8, 1

    result = split_integer(value, number_of_parts)

    assert sum(result) == 8


def test_should_split_into_equal_parts_when_value_is_divisible_by_parts():
    value, number_of_parts = 6, 2

    result = split_integer(value, number_of_parts)

    assert result == [3, 3]


def test_should_return_part_equals_to_a_value_when_slitting_into_one_part():
    value, number_of_parts = 8, 1

    result = split_integer(value, number_of_parts)

    assert result[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal():
    value, number_of_parts = 17, 4

    result = split_integer(value, number_of_parts)

    assert result == [4, 4, 4, 5]


def test_should_add_zeros_when_value_is_less_than_number_of_parts():
    value, number_of_parts = 2, 4

    result = split_integer(value, number_of_parts)

    assert result == [0, 0, 1, 1]
